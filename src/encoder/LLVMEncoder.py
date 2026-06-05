import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import llvmlite.ir as ir
import llvmlite.binding as llvm_binding

from generated.MiniGOVisitor import MiniGOVisitor
from generated.MiniGOParser import MiniGOParser
from typechecker.Decoraciones import Decoraciones

_I64  = ir.IntType(64)
_F64  = ir.DoubleType()
_I1   = ir.IntType(1)
_I8   = ir.IntType(8)
_I32  = ir.IntType(32)
_I8P  = ir.PointerType(_I8)
_VOID = ir.VoidType()

_ESCAPES = {'n': 10, 't': 9, 'r': 13, '\\': 92, "'": 39, '"': 34, '0': 0, 'a': 7, 'b': 8}


class LLVMEncoder(MiniGOVisitor):

    def __init__(self, decoraciones: Decoraciones):
        self.decoraciones = decoraciones
        self.module = ir.Module(name="miniGO")
        self.module.triple = llvm_binding.get_default_triple()
        self.builder = None          # válido sólo dentro de una función
        self.func_map = {}           # nombre → ir.Function
        self.var_scopes = [{}]       # pila de dicts: nombre → (ptr, ir_type)
        self._str_count = 0
        self._printf = None
        self._current_ret_type = None

    # ── Scopes ────────────────────────────────────────────────────────────

    def _push_scope(self):  self.var_scopes.append({})
    def _pop_scope(self):   self.var_scopes.pop()

    def _lookup(self, name):
        for scope in reversed(self.var_scopes):
            if name in scope:
                return scope[name]
        return None

    def _define(self, name, ptr, ir_type):
        self.var_scopes[-1][name] = (ptr, ir_type)

    # ── Tipos ─────────────────────────────────────────────────────────────

    _STR_TO_IR = {"int": _I64, "float64": _F64, "bool": _I1,
                  "string": _I8P, "rune": _I64}

    def _str_to_ir(self, s):
        return self._STR_TO_IR.get(s, _I64)

    def _resolve_ir_type(self, ctx):
        """declType parse-tree node → llvmlite ir.Type."""
        if isinstance(ctx, MiniGOParser.SimpleTypeContext):
            return self._str_to_ir(ctx.IDENTIFIER().getText())
        if isinstance(ctx, MiniGOParser.ArrayTypeContext):
            size = int(ctx.arrayDeclType().INTLITERAL().getText())
            elem = self._resolve_ir_type(ctx.arrayDeclType().declType())
            return ir.ArrayType(elem, size)
        if isinstance(ctx, MiniGOParser.SliceTypeContext):
            elem = self._resolve_ir_type(ctx.sliceDeclType().declType())
            return ir.PointerType(elem)
        if isinstance(ctx, MiniGOParser.GroupedTypeContext):
            return self._resolve_ir_type(ctx.declType())
        if isinstance(ctx, MiniGOParser.StructTypeContext):
            return _I64   # structs: representación simplificada
        return _I64

    def _tipo_to_ir(self, tipo):
        """Tipo de decoraciones (str o tupla) → ir.Type."""
        if isinstance(tipo, str):
            return self._str_to_ir(tipo)
        if isinstance(tipo, tuple):
            if tipo[0] == "array":
                return ir.ArrayType(self._tipo_to_ir(tipo[2]), tipo[1])
            if tipo[0] == "slice":
                return ir.PointerType(self._tipo_to_ir(tipo[1]))
        return _I64

    def _default(self, ir_type):
        if isinstance(ir_type, ir.DoubleType):
            return ir.Constant(ir_type, 0.0)
        if isinstance(ir_type, ir.PointerType):
            return ir.Constant(ir_type, None)
        if isinstance(ir_type, ir.ArrayType):
            return ir.Constant(ir_type, None)
        return ir.Constant(ir_type, 0)

    # ── Strings constantes ────────────────────────────────────────────────

    def _global_str(self, text):
        """Crea @.strN global y retorna la variable LLVM."""
        encoded = (text + '\0').encode('utf-8')
        typ = ir.ArrayType(_I8, len(encoded))
        name = f".str{self._str_count}"; self._str_count += 1
        g = ir.GlobalVariable(self.module, typ, name=name)
        g.global_constant = True
        g.linkage = 'private'
        g.unnamed_addr = True
        g.initializer = ir.Constant(typ, bytearray(encoded))
        return g

    def _str_ptr(self, text):
        """Crea global string y retorna un gep i8* (sólo dentro de funciones)."""
        g = self._global_str(text)
        zero = ir.Constant(_I32, 0)
        return self.builder.gep(g, [zero, zero], inbounds=True)

    # ── printf ────────────────────────────────────────────────────────────

    def _get_printf(self):
        if self._printf is None:
            ty = ir.FunctionType(_I32, [_I8P], var_arg=True)
            self._printf = ir.Function(self.module, ty, name="printf")
        return self._printf

    # ── alloca ────────────────────────────────────────────────────────────

    def _alloca(self, ir_type, name=""):
        """Alloca en el bloque de entrada de la función actual."""
        with self.builder.goto_entry_block():
            return self.builder.alloca(ir_type, name=name)

    # ── coerce ────────────────────────────────────────────────────────────

    def _coerce(self, val, target):
        if val is None or val.type == target:
            return val
        if isinstance(val.type, ir.IntType) and isinstance(target, ir.IntType):
            if val.type.width < target.width:
                return self.builder.zext(val, target)
            return self.builder.trunc(val, target)
        return val

    # ── Guardar IR ───────────────────────────────────────────────────────

    def write_ir(self, source_path):
        ll_path = os.path.splitext(source_path)[0] + ".ll"
        with open(ll_path, "w") as f:
            f.write(str(self.module))
        return ll_path

    # ── Root ──────────────────────────────────────────────────────────────

    def visitRoot(self, ctx: MiniGOParser.RootContext):
        # Pre-declarar todas las funciones para soportar forward references
        for decl in ctx.topDeclarationList().funcDecl():
            self._pre_declare_func(decl)
        return self.visitChildren(ctx)

    def _pre_declare_func(self, ctx):
        front = ctx.funcFrontDecl()
        nombre = front.IDENTIFIER().getText()
        if nombre in self.func_map:
            return
        ret_ir = _I32 if nombre == "main" else (
            self._resolve_ir_type(front.declType()) if front.declType() else _VOID
        )
        param_types = []
        if front.funcArgDecls():
            for arg in front.funcArgDecls().singleVarDeclNoExps():
                t = self._resolve_ir_type(arg.declType())
                for _ in arg.identifierList().IDENTIFIER():
                    param_types.append(t)
        ftype = ir.FunctionType(ret_ir, param_types)
        func = ir.Function(self.module, ftype, name=nombre)
        self.func_map[nombre] = func

    # ── Pass-through ──────────────────────────────────────────────────────

    def visitTopDeclarationList(self, ctx): return self.visitChildren(ctx)
    def visitVariableDecl(self, ctx):       return self.visitChildren(ctx)
    def visitInnerVarDecls(self, ctx):      return self.visitChildren(ctx)
    def visitTypeDecl(self, ctx):           return None
    def visitSingleTypeDecl(self, ctx):     return None
    def visitStatementList(self, ctx):      return self.visitChildren(ctx)
    def visitPrimaryExpr(self, ctx):        return self.visit(ctx.primaryExpression())
    def visitOperandExpr(self, ctx):        return self.visit(ctx.operand())
    def visitLiteralOperand(self, ctx):     return self.visit(ctx.literal())
    def visitGroupedExpr(self, ctx):        return self.visit(ctx.expression())
    def visitExpressionList(self, ctx):     return [self.visit(e) for e in ctx.expression()]

    # ── Literales ─────────────────────────────────────────────────────────

    def visitIntLit(self, ctx):
        return ir.Constant(_I64, int(ctx.INTLITERAL().getText()))

    def visitFloatLit(self, ctx):
        return ir.Constant(_F64, float(ctx.FLOATLITERAL().getText()))

    def visitRuneLit(self, ctx):
        text = ctx.RUNELITERAL().getText()[1:-1]
        val = _ESCAPES.get(text[1], ord(text[1])) if text.startswith('\\') else ord(text[0])
        return ir.Constant(_I64, val)

    def visitRawStringLit(self, ctx):
        text = ctx.RAWSTRINGLITERAL().getText()[1:-1]
        if self.builder is None:
            return ir.Constant(_I8P, None)
        return self._str_ptr(text)

    def visitInterpretedStringLit(self, ctx):
        text = ctx.INTERPRETEDSTRINGLITERAL().getText()[1:-1]
        if self.builder is None:
            return ir.Constant(_I8P, None)
        # Procesar secuencias de escape básicas
        text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r')
        return self._str_ptr(text)

    # ── Identificadores ───────────────────────────────────────────────────

    def visitIdentifierOperand(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name == "true":  return ir.Constant(_I1, 1)
        if name == "false": return ir.Constant(_I1, 0)
        if self.builder is None: return None
        entry = self._lookup(name)
        if entry is None: return ir.Constant(_I64, 0)
        ptr, ir_type = entry
        if isinstance(ir_type, ir.ArrayType):
            return ptr   # arrays: retornar puntero, no cargar
        return self.builder.load(ptr, name=name)

    # ── Declaraciones de variables ────────────────────────────────────────

    def _decl_var(self, name, ir_type, init_val=None):
        if self.builder is None:
            # Scope global
            g = ir.GlobalVariable(self.module, ir_type, name=name)
            g.linkage = 'internal'
            if isinstance(init_val, ir.Constant):
                g.initializer = init_val
            else:
                g.initializer = self._default(ir_type)
            self._define(name, g, ir_type)
        else:
            ptr = self._alloca(ir_type, name)
            val = init_val if init_val is not None else self._default(ir_type)
            if not isinstance(ir_type, ir.ArrayType):
                self.builder.store(self._coerce(val, ir_type) if val else self._default(ir_type), ptr)
            self._define(name, ptr, ir_type)

    def visitVarDeclWithTypeAndValue(self, ctx):
        ir_type = self._resolve_ir_type(ctx.declType())
        vals = self.visit(ctx.expressionList())
        for i, id_node in enumerate(ctx.identifierList().IDENTIFIER()):
            val = vals[i] if i < len(vals) else None
            self._decl_var(id_node.getText(), ir_type, val)
        return None

    def visitVarDeclWithValue(self, ctx):
        vals = self.visit(ctx.expressionList())
        for i, id_node in enumerate(ctx.identifierList().IDENTIFIER()):
            val = vals[i] if i < len(vals) else ir.Constant(_I64, 0)
            if val is None: val = ir.Constant(_I64, 0)
            self._decl_var(id_node.getText(), val.type, val)
        return None

    def visitVarDeclNoExps(self, ctx):
        return self.visit(ctx.singleVarDeclNoExps())

    def visitSingleVarDeclNoExps(self, ctx):
        ir_type = self._resolve_ir_type(ctx.declType())
        for id_node in ctx.identifierList().IDENTIFIER():
            self._decl_var(id_node.getText(), ir_type)
        return None

    # ── Aritmética ────────────────────────────────────────────────────────

    def _binop(self, ctx, iop, fop=None):
        if self.builder is None: return ir.Constant(_I64, 0)
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if l is None or r is None: return ir.Constant(_I64, 0)
        if isinstance(l.type, ir.DoubleType):
            return getattr(self.builder, fop or iop)(l, r)
        return getattr(self.builder, iop)(l, r)

    def visitAddExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I64, 0)
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if l is None or r is None: return ir.Constant(_I64, 0)
        return self.builder.fadd(l, r) if isinstance(l.type, ir.DoubleType) else self.builder.add(l, r)

    def visitSubExpr(self, ctx):  return self._binop(ctx, 'sub', 'fsub')
    def visitMultExpr(self, ctx): return self._binop(ctx, 'mul', 'fmul')
    def visitDivExpr(self, ctx):  return self._binop(ctx, 'sdiv', 'fdiv')
    def visitModExpr(self, ctx):  return self._binop(ctx, 'srem')

    def visitAmpExpr(self, ctx):    return self._binop(ctx, 'and_')
    def visitPipeExpr(self, ctx):   return self._binop(ctx, 'or_')
    def visitXorExpr(self, ctx):    return self._binop(ctx, 'xor')
    def visitLshiftExpr(self, ctx): return self._binop(ctx, 'shl')
    def visitRshiftExpr(self, ctx): return self._binop(ctx, 'ashr')
    def visitAmpxorExpr(self, ctx): return ir.Constant(_I64, 0)

    # ── Comparaciones ─────────────────────────────────────────────────────

    def _cmp(self, ctx, iop, fop=None):
        if self.builder is None: return ir.Constant(_I1, 0)
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if l is None or r is None: return ir.Constant(_I1, 0)
        if isinstance(l.type, ir.DoubleType):
            return self.builder.fcmp_ordered(fop or iop, l, r)
        # Para punteros (strings) usar comparación sin signo
        if isinstance(l.type, ir.PointerType):
            return self.builder.icmp_unsigned(iop, l, r)
        return self.builder.icmp_signed(iop, l, r)

    def visitEqExpr(self, ctx):  return self._cmp(ctx, '==')
    def visitNeqExpr(self, ctx): return self._cmp(ctx, '!=')
    def visitLtExpr(self, ctx):  return self._cmp(ctx, '<')
    def visitLeqExpr(self, ctx): return self._cmp(ctx, '<=')
    def visitGtExpr(self, ctx):  return self._cmp(ctx, '>')
    def visitGeqExpr(self, ctx): return self._cmp(ctx, '>=')

    # ── Lógicas ───────────────────────────────────────────────────────────

    def visitAndExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I1, 0)
        l = self.visit(ctx.expression(0)); r = self.visit(ctx.expression(1))
        return self.builder.and_(l, r) if l and r else ir.Constant(_I1, 0)

    def visitOrExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I1, 0)
        l = self.visit(ctx.expression(0)); r = self.visit(ctx.expression(1))
        return self.builder.or_(l, r) if l and r else ir.Constant(_I1, 0)

    def visitNotExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I1, 0)
        v = self.visit(ctx.expression())
        return self.builder.not_(v) if v else ir.Constant(_I1, 0)

    def visitUnaryMinusExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I64, 0)
        v = self.visit(ctx.expression())
        if v is None: return ir.Constant(_I64, 0)
        return self.builder.fsub(ir.Constant(_F64, 0.0), v) if isinstance(v.type, ir.DoubleType) else self.builder.neg(v)

    def visitUnaryPlusExpr(self, ctx): return self.visit(ctx.expression())
    def visitXorUnaryExpr(self, ctx):
        if self.builder is None: return ir.Constant(_I64, 0)
        v = self.visit(ctx.expression())
        return self.builder.not_(v) if v else ir.Constant(_I64, 0)

    # ── lvalue helper ─────────────────────────────────────────────────────

    def _lvalue_ptr(self, expr_ctx):
        """Retorna (ptr, ir_type) del lvalue, o None."""
        if isinstance(expr_ctx, MiniGOParser.PrimaryExprContext):
            return self._lvalue_ptr(expr_ctx.primaryExpression())
        if isinstance(expr_ctx, MiniGOParser.OperandExprContext):
            return self._lvalue_ptr(expr_ctx.operand())
        if isinstance(expr_ctx, MiniGOParser.IdentifierOperandContext):
            return self._lookup(expr_ctx.IDENTIFIER().getText())
        if isinstance(expr_ctx, MiniGOParser.IndexExprContext):
            return self._array_elem_ptr(expr_ctx)
        if isinstance(expr_ctx, MiniGOParser.SelectorExprContext):
            return self._field_ptr(expr_ctx)
        return None

    def _arr_base_name(self, prim_ctx):
        if isinstance(prim_ctx, MiniGOParser.OperandExprContext):
            return self._arr_base_name(prim_ctx.operand())
        if isinstance(prim_ctx, MiniGOParser.IdentifierOperandContext):
            return prim_ctx.IDENTIFIER().getText()
        return None

    def _array_elem_ptr(self, ctx):
        base_name = self._arr_base_name(ctx.primaryExpression())
        idx = self.visit(ctx.index().expression())
        if base_name is None or idx is None: return None
        entry = self._lookup(base_name)
        if entry is None: return None
        ptr, ir_type = entry
        zero = ir.Constant(_I32, 0)
        if isinstance(ir_type, ir.ArrayType):
            ep = self.builder.gep(ptr, [zero, idx], inbounds=True)
            return (ep, ir_type.element)
        if isinstance(ir_type, ir.PointerType):
            loaded = self.builder.load(ptr)
            ep = self.builder.gep(loaded, [idx])
            return (ep, ir_type.pointee)
        return None

    def _field_ptr(self, ctx):
        # Struct field: simplificado — retorna None (sin codegen completo de structs)
        return None

    # ── Sentencias de asignación ──────────────────────────────────────────

    def visitSimpleAssign(self, ctx):
        rvals = self.visit(ctx.expressionList(1))
        for i, lctx in enumerate(ctx.expressionList(0).expression()):
            rval = rvals[i] if i < len(rvals) else ir.Constant(_I64, 0)
            entry = self._lvalue_ptr(lctx)
            if entry and rval:
                ptr, ir_type = entry
                self.builder.store(self._coerce(rval, ir_type), ptr)
        return None

    def visitShortVarDecl(self, ctx):
        rvals = self.visit(ctx.expressionList(1))
        for i, lctx in enumerate(ctx.expressionList(0).expression()):
            name = lctx.getText()
            rval = rvals[i] if i < len(rvals) else ir.Constant(_I64, 0)
            if rval is None: rval = ir.Constant(_I64, 0)
            existing = self.var_scopes[-1].get(name)
            if existing:
                ptr, t = existing
                self.builder.store(self._coerce(rval, t), ptr)
            else:
                ptr = self._alloca(rval.type, name)
                self.builder.store(rval, ptr)
                self._define(name, ptr, rval.type)
        return None

    def _compound(self, ctx, iop, fop=None):
        entry = self._lvalue_ptr(ctx.expression(0))
        rval = self.visit(ctx.expression(1))
        if entry is None or rval is None: return None
        ptr, ir_type = entry
        lval = self.builder.load(ptr)
        op = fop if (fop and isinstance(ir_type, ir.DoubleType)) else iop
        result = getattr(self.builder, op)(lval, self._coerce(rval, ir_type))
        self.builder.store(result, ptr)
        return None

    def visitPlusAssign(self, ctx):  self._compound(ctx, 'add', 'fadd')
    def visitMinusAssign(self, ctx): self._compound(ctx, 'sub', 'fsub')
    def visitMultAssign(self, ctx):  self._compound(ctx, 'mul', 'fmul')
    def visitDivAssign(self, ctx):   self._compound(ctx, 'sdiv', 'fdiv')
    def visitModAssign(self, ctx):   self._compound(ctx, 'srem')
    def visitAmpAssign(self, ctx):   return None
    def visitPipeAssign(self, ctx):  return None
    def visitXorAssign(self, ctx):   return None
    def visitLshiftAssign(self, ctx): return None
    def visitRshiftAssign(self, ctx): return None
    def visitAmpxorAssign(self, ctx): return None

    def visitIncDecStatement(self, ctx):
        entry = self._lvalue_ptr(ctx.expression())
        if entry is None: return None
        ptr, ir_type = entry
        val = self.builder.load(ptr)
        one = ir.Constant(ir_type, 1)
        new_val = self.builder.add(val, one) if ctx.INC() else self.builder.sub(val, one)
        self.builder.store(new_val, ptr)
        return None

    def visitExpressionStatement(self, ctx):
        self.visit(ctx.expression()); return None

    def visitEmptyStatement(self, ctx):   return None
    def visitBreakStatement(self, ctx):   return None
    def visitContinueStatement(self, ctx): return None

    def visitVarDeclStatement(self, ctx): return self.visit(ctx.variableDecl())
    def visitTypeDeclStatement(self, ctx): return None

    def visitBlockStatement(self, ctx):
        self._push_scope(); self.visitChildren(ctx); self._pop_scope(); return None

    # ── println / print ───────────────────────────────────────────────────

    def _println(self, val, tipo):
        pf = self._get_printf()
        if tipo == "float64" or isinstance(getattr(val, 'type', None), ir.DoubleType):
            self.builder.call(pf, [self._str_ptr("%f\n"), val])
        elif tipo == "bool" or (isinstance(getattr(val, 'type', None), ir.IntType) and val.type.width == 1):
            ts = self._str_ptr("true\n"); fs = self._str_ptr("false\n")
            self.builder.call(pf, [self.builder.select(val, ts, fs)])
        elif tipo == "string" or isinstance(getattr(val, 'type', None), ir.PointerType):
            self.builder.call(pf, [self._str_ptr("%s\n"), val])
        elif tipo == "rune":
            i32val = self.builder.trunc(val, _I32)
            self.builder.call(pf, [self._str_ptr("%c\n"), i32val])
        else:
            self.builder.call(pf, [self._str_ptr("%lld\n"), val])

    def visitPrintlnStatement(self, ctx):
        if ctx.expressionList() is None:
            self.builder.call(self._get_printf(), [self._str_ptr("\n")])
            return None
        exprs = ctx.expressionList().expression()
        vals = self.visit(ctx.expressionList())
        for i, val in enumerate(vals):
            if val is not None:
                tipo = self.decoraciones.getTipo(exprs[i])
                self._println(val, tipo)
        return None

    def visitPrintStatement(self, ctx):
        if ctx.expressionList() is None: return None
        exprs = ctx.expressionList().expression()
        vals = self.visit(ctx.expressionList())
        pf = self._get_printf()
        for i, val in enumerate(vals):
            if val is None: continue
            tipo = self.decoraciones.getTipo(exprs[i])
            if tipo == "float64":
                self.builder.call(pf, [self._str_ptr("%f"), val])
            elif tipo == "string" or isinstance(getattr(val, 'type', None), ir.PointerType):
                self.builder.call(pf, [self._str_ptr("%s"), val])
            elif tipo == "bool":
                ts = self._str_ptr("true"); fs = self._str_ptr("false")
                self.builder.call(pf, [self.builder.select(val, ts, fs)])
            else:
                self.builder.call(pf, [self._str_ptr("%lld"), val])
        return None

    # ── Funciones ─────────────────────────────────────────────────────────

    def visitFuncDecl(self, ctx):
        front = ctx.funcFrontDecl()
        nombre = front.IDENTIFIER().getText()
        func = self.func_map.get(nombre)
        if func is None: return None

        entry_bb = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_bb)
        self._push_scope()
        prev_ret = self._current_ret_type
        self._current_ret_type = func.ftype.return_type

        # Alloca para parámetros
        param_names = []
        if front.funcArgDecls():
            for arg in front.funcArgDecls().singleVarDeclNoExps():
                for id_node in arg.identifierList().IDENTIFIER():
                    param_names.append(id_node.getText())
        for i, param in enumerate(func.args):
            pname = param_names[i] if i < len(param_names) else f"p{i}"
            param.name = pname
            ptr = self._alloca(param.type, pname)
            self.builder.store(param, ptr)
            self._define(pname, ptr, param.type)

        self.visit(ctx.block())

        # Terminator de respaldo
        if not self.builder.block.is_terminated:
            ret_type = self._current_ret_type
            if isinstance(ret_type, ir.VoidType):
                self.builder.ret_void()
            elif nombre == "main":
                self.builder.ret(ir.Constant(_I32, 0))
            else:
                self.builder.ret(self._default(ret_type))

        self._pop_scope()
        self._current_ret_type = prev_ret
        self.builder = None
        return None

    def visitCallExpr(self, ctx):
        base = ctx.primaryExpression()
        func_name = None
        if isinstance(base, MiniGOParser.OperandExprContext):
            op = base.operand()
            if isinstance(op, MiniGOParser.IdentifierOperandContext):
                func_name = op.IDENTIFIER().getText()

        func = self.func_map.get(func_name) if func_name else None
        if func is None: return ir.Constant(_I64, 0)

        arg_vals = []
        if ctx.arguments().expressionList():
            arg_vals = self.visit(ctx.arguments().expressionList())

        coerced = []
        param_types = func.ftype.args
        for i, av in enumerate(arg_vals):
            if av is None: continue
            if i < len(param_types):
                coerced.append(self._coerce(av, param_types[i]))
            else:
                coerced.append(av)

        return self.builder.call(func, coerced)

    def visitReturnStatement(self, ctx):
        ret_type = self._current_ret_type
        if ctx.expression() is not None:
            val = self.visit(ctx.expression())
            if val is not None and ret_type is not None:
                self.builder.ret(self._coerce(val, ret_type))
        else:
            if isinstance(ret_type, ir.VoidType) or ret_type is None:
                self.builder.ret_void()
            else:
                self.builder.ret(self._default(ret_type))
        return None

    # ── If ────────────────────────────────────────────────────────────────

    def _cbranch(self, cond, then_bb, else_bb):
        if not self.builder.block.is_terminated:
            self.builder.cbranch(cond, then_bb, else_bb)

    def visitSimpleIf(self, ctx):
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb  = func.append_basic_block("then")
        merge_bb = func.append_basic_block("merge")
        self._cbranch(cond, then_bb, merge_bb)

        self.builder.position_at_end(then_bb)
        self._push_scope(); self.visit(ctx.block()); self._pop_scope()
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)

        self.builder.position_at_end(merge_bb)
        return None

    def visitIfElse(self, ctx):
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb  = func.append_basic_block("then")
        else_bb  = func.append_basic_block("else")
        merge_bb = func.append_basic_block("merge")
        self._cbranch(cond, then_bb, else_bb)

        self.builder.position_at_end(then_bb)
        self._push_scope(); self.visit(ctx.block(0)); self._pop_scope()
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)

        self.builder.position_at_end(else_bb)
        self._push_scope(); self.visit(ctx.block(1)); self._pop_scope()
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)

        self.builder.position_at_end(merge_bb)
        return None

    def visitIfElseIf(self, ctx):
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb = func.append_basic_block("then")
        else_bb = func.append_basic_block("else")
        self._cbranch(cond, then_bb, else_bb)

        self.builder.position_at_end(then_bb)
        self._push_scope(); self.visit(ctx.block()); self._pop_scope()
        after_then = self.builder.block

        self.builder.position_at_end(else_bb)
        self.visit(ctx.ifStatement())
        after_else = self.builder.block

        merge_bb = func.append_basic_block("merge")
        if not after_then.is_terminated:
            self.builder.position_at_end(after_then); self.builder.branch(merge_bb)
        if not after_else.is_terminated:
            self.builder.position_at_end(after_else); self.builder.branch(merge_bb)
        self.builder.position_at_end(merge_bb)
        return None

    def visitIfWithInit(self, ctx):
        self._push_scope()
        self.visit(ctx.simpleStatement())
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb  = func.append_basic_block("then")
        merge_bb = func.append_basic_block("merge")
        self._cbranch(cond, then_bb, merge_bb)
        self.builder.position_at_end(then_bb)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)
        self._pop_scope()
        self.builder.position_at_end(merge_bb)
        return None

    def visitIfWithInitElse(self, ctx):
        self._push_scope()
        self.visit(ctx.simpleStatement())
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb  = func.append_basic_block("then")
        else_bb  = func.append_basic_block("else")
        merge_bb = func.append_basic_block("merge")
        self._cbranch(cond, then_bb, else_bb)
        self.builder.position_at_end(then_bb)
        self.visit(ctx.block(0))
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)
        self.builder.position_at_end(else_bb)
        self.visit(ctx.block(1))
        if not self.builder.block.is_terminated: self.builder.branch(merge_bb)
        self._pop_scope()
        self.builder.position_at_end(merge_bb)
        return None

    def visitIfWithInitElseIf(self, ctx):
        self._push_scope()
        self.visit(ctx.simpleStatement())
        cond = self.visit(ctx.expression())
        func = self.builder.function
        then_bb = func.append_basic_block("then")
        else_bb = func.append_basic_block("else")
        self._cbranch(cond, then_bb, else_bb)
        self.builder.position_at_end(then_bb)
        self._push_scope(); self.visit(ctx.block()); self._pop_scope()
        after_then = self.builder.block
        self.builder.position_at_end(else_bb)
        self.visit(ctx.ifStatement())
        after_else = self.builder.block
        merge_bb = func.append_basic_block("merge")
        if not after_then.is_terminated:
            self.builder.position_at_end(after_then); self.builder.branch(merge_bb)
        if not after_else.is_terminated:
            self.builder.position_at_end(after_else); self.builder.branch(merge_bb)
        self._pop_scope()
        self.builder.position_at_end(merge_bb)
        return None

    # ── Loops ─────────────────────────────────────────────────────────────

    def visitInfiniteLoop(self, ctx):
        func = self.builder.function
        loop_bb = func.append_basic_block("loop")
        exit_bb = func.append_basic_block("after_loop")
        if not self.builder.block.is_terminated: self.builder.branch(loop_bb)
        self.builder.position_at_end(loop_bb)
        self._push_scope(); self.visit(ctx.block()); self._pop_scope()
        if not self.builder.block.is_terminated: self.builder.branch(loop_bb)
        self.builder.position_at_end(exit_bb)
        return None

    def visitWhileLoop(self, ctx):
        func = self.builder.function
        header_bb = func.append_basic_block("while_header")
        body_bb   = func.append_basic_block("while_body")
        exit_bb   = func.append_basic_block("while_exit")
        if not self.builder.block.is_terminated: self.builder.branch(header_bb)
        self.builder.position_at_end(header_bb)
        cond = self.visit(ctx.expression())
        self.builder.cbranch(cond, body_bb, exit_bb)
        self.builder.position_at_end(body_bb)
        self._push_scope(); self.visit(ctx.block()); self._pop_scope()
        if not self.builder.block.is_terminated: self.builder.branch(header_bb)
        self.builder.position_at_end(exit_bb)
        return None

    def visitForLoop(self, ctx):
        func = self.builder.function
        self._push_scope()
        self.visit(ctx.simpleStatement(0))
        header_bb = func.append_basic_block("for_header")
        body_bb   = func.append_basic_block("for_body")
        post_bb   = func.append_basic_block("for_post")
        exit_bb   = func.append_basic_block("for_exit")
        if not self.builder.block.is_terminated: self.builder.branch(header_bb)
        self.builder.position_at_end(header_bb)
        cond = self.visit(ctx.expression())
        self.builder.cbranch(cond, body_bb, exit_bb)
        self.builder.position_at_end(body_bb)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated: self.builder.branch(post_bb)
        self.builder.position_at_end(post_bb)
        self.visit(ctx.simpleStatement(1))
        if not self.builder.block.is_terminated: self.builder.branch(header_bb)
        self._pop_scope()
        self.builder.position_at_end(exit_bb)
        return None

    def visitForLoopNoCondition(self, ctx):
        func = self.builder.function
        self._push_scope()
        self.visit(ctx.simpleStatement(0))
        loop_bb = func.append_basic_block("for_body")
        exit_bb = func.append_basic_block("for_exit")
        if not self.builder.block.is_terminated: self.builder.branch(loop_bb)
        self.builder.position_at_end(loop_bb)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.visit(ctx.simpleStatement(1))
            self.builder.branch(loop_bb)
        self._pop_scope()
        self.builder.position_at_end(exit_bb)
        return None

    # ── Switch ────────────────────────────────────────────────────────────

    def _emit_switch(self, switch_val, clauses_ctx):
        func = self.builder.function
        merge_bb = func.append_basic_block("sw_merge")
        default_bb = merge_bb

        case_items = []   # (vals, body_bb, stmts_ctx)
        default_stmts = None

        for clause in clauses_ctx.expressionCaseClause():
            body_bb = func.append_basic_block("sw_case")
            sc = clause.expressionSwitchCase()
            if isinstance(sc, MiniGOParser.CaseClauseContext):
                vals = [self.visit(e) for e in sc.expressionList().expression()]
                case_items.append((vals, body_bb, clause.statementList()))
            else:
                default_bb = body_bb
                default_stmts = (body_bb, clause.statementList())

        # Emitir instrucción switch o cadena de comparaciones
        if (switch_val is not None and isinstance(switch_val.type, ir.IntType)
                and all(isinstance(v, ir.Constant) for vals, _, _ in case_items for v in vals)):
            sw = self.builder.switch(switch_val, default_bb)
            for vals, body_bb, _ in case_items:
                for v in vals:
                    sw.add_case(v, body_bb)
        else:
            for vals, body_bb, _ in case_items:
                cond = None
                for v in vals:
                    if switch_val is not None and v is not None:
                        c = self.builder.icmp_signed('==', switch_val, v)
                    else:
                        c = ir.Constant(_I1, 1)
                    cond = self.builder.or_(cond, c) if cond else c
                next_bb = func.append_basic_block("sw_next")
                if cond: self.builder.cbranch(cond, body_bb, next_bb)
                else:    self.builder.branch(body_bb)
                self.builder.position_at_end(next_bb)
            self.builder.branch(default_bb)

        # Cuerpos de casos
        for _, body_bb, stmts in case_items:
            self.builder.position_at_end(body_bb)
            self._push_scope(); self.visit(stmts); self._pop_scope()
            if not self.builder.block.is_terminated: self.builder.branch(merge_bb)

        if default_stmts:
            body_bb, stmts = default_stmts
            self.builder.position_at_end(body_bb)
            self._push_scope(); self.visit(stmts); self._pop_scope()
            if not self.builder.block.is_terminated: self.builder.branch(merge_bb)

        self.builder.position_at_end(merge_bb)

    def visitSwitchWithExpr(self, ctx):
        v = self.visit(ctx.expression())
        self._emit_switch(v, ctx.expressionCaseClauseList()); return None

    def visitSwitchWithInitAndExpr(self, ctx):
        self._push_scope()
        self.visit(ctx.simpleStatement())
        v = self.visit(ctx.expression())
        self._emit_switch(v, ctx.expressionCaseClauseList())
        self._pop_scope(); return None

    def visitSwitchWithInit(self, ctx):
        self._push_scope()
        self.visit(ctx.simpleStatement())
        self._emit_switch(None, ctx.expressionCaseClauseList())
        self._pop_scope(); return None

    def visitSwitchEmpty(self, ctx):
        self._emit_switch(None, ctx.expressionCaseClauseList()); return None

    def visitExpressionCaseClause(self, ctx): return None
    def visitCaseClause(self, ctx):           return None
    def visitDefaultClause(self, ctx):        return None

    # ── Arrays e índices ──────────────────────────────────────────────────

    def visitIndexExpr(self, ctx):
        entry = self._array_elem_ptr(ctx)
        if entry is None: return ir.Constant(_I64, 0)
        ep, elem_type = entry
        return self.builder.load(ep)

    # ── Builtins ──────────────────────────────────────────────────────────

    def visitLengthExpr(self, ctx):
        tipo = self.decoraciones.getTipo(ctx.lengthExpression().expression())
        if isinstance(tipo, tuple) and tipo[0] == "array":
            return ir.Constant(_I64, tipo[1])
        return ir.Constant(_I64, 0)

    def visitCapExpr(self, ctx):
        tipo = self.decoraciones.getTipo(ctx.capExpression().expression())
        if isinstance(tipo, tuple) and tipo[0] == "array":
            return ir.Constant(_I64, tipo[1])
        return ir.Constant(_I64, 0)

    def visitAppendExpr(self, ctx): return ir.Constant(_I64, 0)
    def visitSelectorExpr(self, ctx): return ir.Constant(_I64, 0)
