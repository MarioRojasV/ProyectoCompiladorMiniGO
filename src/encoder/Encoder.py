import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generated.MiniGOVisitor import MiniGOVisitor
from generated.MiniGOParser import MiniGOParser
from typechecker.Decoraciones import Decoraciones
from encoder.Cuadrupla import Cuadrupla


class MiniGOEncoder(MiniGOVisitor):

    def __init__(self, decoraciones: Decoraciones):
        self.instrucciones: list[Cuadrupla] = []
        self.decoraciones = decoraciones
        self._temp_count = 0
        self._label_count = 0

    def _newTemp(self) -> str:
        self._temp_count += 1
        return f"t{self._temp_count}"

    def _newLabel(self) -> str:
        self._label_count += 1
        return f"L{self._label_count}"

    def emit(self, op: str, arg1=None, arg2=None, result=None):
        self.instrucciones.append(Cuadrupla(op, arg1, arg2, result))

    def printIR(self):
        print("=== Código Intermedio ===")
        for instr in self.instrucciones:
            print(instr)

    def write(self, source_path: str):
        ir_path = os.path.splitext(source_path)[0] + ".ir"
        with open(ir_path, "w", encoding="utf-8") as f:
            for instr in self.instrucciones:
                f.write(str(instr) + "\n")

    def visitRoot(self, ctx: MiniGOParser.RootContext):
        return self.visitChildren(ctx)

    # ── Pass-through (nodos que delegan al hijo) ──────────────────────────

    def visitTopDeclarationList(self, ctx):
        return self.visitChildren(ctx)

    def visitVariableDecl(self, ctx):
        return self.visitChildren(ctx)

    def visitInnerVarDecls(self, ctx):
        return self.visitChildren(ctx)

    def visitTypeDecl(self, ctx):
        return None  # tipos/structs: fuera de alcance del encoder

    def visitSingleTypeDecl(self, ctx):
        return None

    def visitStatementList(self, ctx):
        return self.visitChildren(ctx)

    def visitPrimaryExpr(self, ctx: MiniGOParser.PrimaryExprContext):
        return self.visit(ctx.primaryExpression())

    def visitOperandExpr(self, ctx: MiniGOParser.OperandExprContext):
        return self.visit(ctx.operand())

    def visitLiteralOperand(self, ctx: MiniGOParser.LiteralOperandContext):
        return self.visit(ctx.literal())

    def visitGroupedExpr(self, ctx: MiniGOParser.GroupedExprContext):
        return self.visit(ctx.expression())

    def visitExpressionList(self, ctx: MiniGOParser.ExpressionListContext):
        return [self.visit(e) for e in ctx.expression()]

    # ── Literales (retornan el valor como string, sin emitir instrucción) ─

    def visitIntLit(self, ctx: MiniGOParser.IntLitContext):
        return ctx.INTLITERAL().getText()

    def visitFloatLit(self, ctx: MiniGOParser.FloatLitContext):
        return ctx.FLOATLITERAL().getText()

    def visitRuneLit(self, ctx: MiniGOParser.RuneLitContext):
        return ctx.RUNELITERAL().getText()

    def visitRawStringLit(self, ctx: MiniGOParser.RawStringLitContext):
        return ctx.RAWSTRINGLITERAL().getText()

    def visitInterpretedStringLit(self, ctx: MiniGOParser.InterpretedStringLitContext):
        return ctx.INTERPRETEDSTRINGLITERAL().getText()

    # ── Identificadores ───────────────────────────────────────────────────

    def visitIdentifierOperand(self, ctx: MiniGOParser.IdentifierOperandContext):
        return ctx.IDENTIFIER().getText()

    # ── Declaraciones de variables ────────────────────────────────────────

    _DEFAULT_VALUES = {
        "int": "0", "float64": "0.0", "bool": "false",
        "string": '""', "rune": "'\\x00'",
    }

    def _defaultValue(self, tipo: str) -> str:
        return self._DEFAULT_VALUES.get(tipo, "0")

    def _emitVarDeclAssigns(self, ctx):
        exprs = self.visit(ctx.expressionList())
        for i, id_node in enumerate(ctx.identifierList().IDENTIFIER()):
            val = exprs[i] if i < len(exprs) else "0"
            self.emit("ASSIGN", val, None, id_node.getText())

    def visitVarDeclWithTypeAndValue(self, ctx: MiniGOParser.VarDeclWithTypeAndValueContext):
        self._emitVarDeclAssigns(ctx); return None

    def visitVarDeclWithValue(self, ctx: MiniGOParser.VarDeclWithValueContext):
        self._emitVarDeclAssigns(ctx); return None

    def visitVarDeclNoExps(self, ctx: MiniGOParser.VarDeclNoExpsContext):
        self.visit(ctx.singleVarDeclNoExps())
        return None

    def visitSingleVarDeclNoExps(self, ctx: MiniGOParser.SingleVarDeclNoExpsContext):
        tipo_str = ctx.declType().getText()
        default  = self._defaultValue(tipo_str)
        for id_node in ctx.identifierList().IDENTIFIER():
            self.emit("ASSIGN", default, None, id_node.getText())
        return None

    # ── Expresiones binarias aritméticas ─────────────────────────────────

    def _emitBinOp(self, op: str, ctx) -> str:
        left  = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        t = self._newTemp()
        self.emit(op, left, right, t)
        return t

    def visitAddExpr(self, ctx: MiniGOParser.AddExprContext):
        return self._emitBinOp("ADD", ctx)

    def visitSubExpr(self, ctx: MiniGOParser.SubExprContext):
        return self._emitBinOp("SUB", ctx)

    def visitMultExpr(self, ctx: MiniGOParser.MultExprContext):
        return self._emitBinOp("MUL", ctx)

    def visitDivExpr(self, ctx: MiniGOParser.DivExprContext):
        return self._emitBinOp("DIV", ctx)

    def visitModExpr(self, ctx: MiniGOParser.ModExprContext):
        return self._emitBinOp("MOD", ctx)

    # ── Comparaciones ─────────────────────────────────────────────────────

    def visitEqExpr(self, ctx: MiniGOParser.EqExprContext):
        return self._emitBinOp("EQ", ctx)

    def visitNeqExpr(self, ctx: MiniGOParser.NeqExprContext):
        return self._emitBinOp("NEQ", ctx)

    def visitLtExpr(self, ctx: MiniGOParser.LtExprContext):
        return self._emitBinOp("LT", ctx)

    def visitLeqExpr(self, ctx: MiniGOParser.LeqExprContext):
        return self._emitBinOp("LEQ", ctx)

    def visitGtExpr(self, ctx: MiniGOParser.GtExprContext):
        return self._emitBinOp("GT", ctx)

    def visitGeqExpr(self, ctx: MiniGOParser.GeqExprContext):
        return self._emitBinOp("GEQ", ctx)

    # Operadores bitwise: fuera del alcance del encoder, ignorar
    def visitAmpExpr(self, ctx):    return self._newTemp()
    def visitAmpxorExpr(self, ctx): return self._newTemp()
    def visitPipeExpr(self, ctx):   return self._newTemp()
    def visitXorExpr(self, ctx):    return self._newTemp()
    def visitLshiftExpr(self, ctx): return self._newTemp()
    def visitRshiftExpr(self, ctx): return self._newTemp()

    # ── Expresiones unarias ───────────────────────────────────────────────

    def visitUnaryMinusExpr(self, ctx: MiniGOParser.UnaryMinusExprContext):
        operand = self.visit(ctx.expression())
        t = self._newTemp()
        self.emit("UMINUS", operand, None, t)
        return t

    def visitUnaryPlusExpr(self, ctx: MiniGOParser.UnaryPlusExprContext):
        return self.visit(ctx.expression())

    def visitXorUnaryExpr(self, ctx):
        return self._newTemp()

    # ── Lógicas ───────────────────────────────────────────────────────────

    def visitAndExpr(self, ctx: MiniGOParser.AndExprContext):
        return self._emitBinOp("AND", ctx)

    def visitOrExpr(self, ctx: MiniGOParser.OrExprContext):
        return self._emitBinOp("OR", ctx)

    def visitNotExpr(self, ctx: MiniGOParser.NotExprContext):
        operand = self.visit(ctx.expression())
        t = self._newTemp()
        self.emit("NOT", operand, None, t)
        return t

    # ── Helper para obtener el nombre del lvalue ──────────────────────────

    def _visitLValue(self, expr_ctx):
        """Retorna str (nombre de var) o tuple ('array', arr_name, idx)."""
        if isinstance(expr_ctx, MiniGOParser.PrimaryExprContext):
            inner = expr_ctx.primaryExpression()
            return self._visitLValue(inner)
        if isinstance(expr_ctx, MiniGOParser.IndexExprContext):
            arr_name = self.visit(expr_ctx.primaryExpression())
            idx      = self.visit(expr_ctx.index().expression())
            return ("array", arr_name, idx)
        if isinstance(expr_ctx, MiniGOParser.OperandExprContext):
            return self._visitLValue(expr_ctx.operand())
        if isinstance(expr_ctx, MiniGOParser.IdentifierOperandContext):
            return expr_ctx.IDENTIFIER().getText()
        return expr_ctx.getText()

    # ── Sentencias simples ────────────────────────────────────────────────

    def visitSimpleAssign(self, ctx: MiniGOParser.SimpleAssignContext):
        right_temps = self.visit(ctx.expressionList(1))
        left_exprs  = ctx.expressionList(0).expression()
        for i, lctx in enumerate(left_exprs):
            rtemp = right_temps[i] if i < len(right_temps) else "0"
            lval  = self._visitLValue(lctx)
            if isinstance(lval, tuple):
                _, arr_name, idx = lval
                self.emit("ARRAY_STORE", rtemp, idx, arr_name)
            else:
                self.emit("ASSIGN", rtemp, None, lval)
        return None

    def visitShortVarDecl(self, ctx: MiniGOParser.ShortVarDeclContext):
        right_temps = self.visit(ctx.expressionList(1))
        left_exprs  = ctx.expressionList(0).expression()
        for i, lctx in enumerate(left_exprs):
            rtemp = right_temps[i] if i < len(right_temps) else "0"
            name  = lctx.getText()
            self.emit("ASSIGN", rtemp, None, name)
        return None

    def _emitCompoundAssign(self, ctx, op: str):
        lname = self._visitLValue(ctx.expression(0))
        rtemp = self.visit(ctx.expression(1))
        t = self._newTemp()
        self.emit(op, lname, rtemp, t)
        self.emit("ASSIGN", t, None, lname)

    def visitPlusAssign(self, ctx: MiniGOParser.PlusAssignContext):
        self._emitCompoundAssign(ctx, "ADD"); return None

    def visitMinusAssign(self, ctx: MiniGOParser.MinusAssignContext):
        self._emitCompoundAssign(ctx, "SUB"); return None

    def visitMultAssign(self, ctx: MiniGOParser.MultAssignContext):
        self._emitCompoundAssign(ctx, "MUL"); return None

    def visitDivAssign(self, ctx: MiniGOParser.DivAssignContext):
        self._emitCompoundAssign(ctx, "DIV"); return None

    def visitModAssign(self, ctx: MiniGOParser.ModAssignContext):
        self._emitCompoundAssign(ctx, "MOD"); return None

    def visitAmpAssign(self, ctx):    return None
    def visitPipeAssign(self, ctx):   return None
    def visitXorAssign(self, ctx):    return None
    def visitLshiftAssign(self, ctx): return None
    def visitRshiftAssign(self, ctx): return None
    def visitAmpxorAssign(self, ctx): return None

    def visitIncDecStatement(self, ctx: MiniGOParser.IncDecStatementContext):
        lname = self._visitLValue(ctx.expression())
        t = self._newTemp()
        op = "ADD" if ctx.INC() is not None else "SUB"
        self.emit(op, lname, "1", t)
        self.emit("ASSIGN", t, None, lname)
        return None

    def visitExpressionStatement(self, ctx: MiniGOParser.ExpressionStatementContext):
        self.visit(ctx.expression())
        return None

    def visitEmptyStatement(self, ctx):
        return None

    def visitBreakStatement(self, ctx):
        return None

    def visitContinueStatement(self, ctx):
        return None

    def visitVarDeclStatement(self, ctx: MiniGOParser.VarDeclStatementContext):
        return self.visit(ctx.variableDecl())

    def visitTypeDeclStatement(self, ctx):
        return None

    def visitBlockStatement(self, ctx: MiniGOParser.BlockStatementContext):
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: MiniGOParser.PrintStatementContext):
        if ctx.expressionList() is not None:
            temps = self.visit(ctx.expressionList())
            for t in temps:
                self.emit("PRINTLN", t, None, None)
        return None

    # ── Funciones ─────────────────────────────────────────────────────────

    def visitFuncDecl(self, ctx: MiniGOParser.FuncDeclContext):
        front = ctx.funcFrontDecl()
        nombre = front.IDENTIFIER().getText()
        self.emit("LABEL", None, None, nombre)
        self.visit(ctx.block())
        return None

    def visitCallExpr(self, ctx: MiniGOParser.CallExprContext):
        base = ctx.primaryExpression()
        func_name = None
        if isinstance(base, MiniGOParser.OperandExprContext):
            op = base.operand()
            if isinstance(op, MiniGOParser.IdentifierOperandContext):
                func_name = op.IDENTIFIER().getText()

        arg_temps = []
        if ctx.arguments().expressionList() is not None:
            arg_temps = self.visit(ctx.arguments().expressionList())
        for at in arg_temps:
            self.emit("PARAM", None, None, at)

        t = self._newTemp()
        self.emit("CALL", func_name, str(len(arg_temps)), t)
        return t

    # ── If statements ─────────────────────────────────────────────────────

    def visitSimpleIf(self, ctx: MiniGOParser.SimpleIfContext):
        cond  = self.visit(ctx.expression())
        lend  = self._newLabel()
        self.emit("JUMPF", cond, None, lend)
        self.visit(ctx.block())
        self.emit("LABEL", None, None, lend)
        return None

    def visitIfElse(self, ctx: MiniGOParser.IfElseContext):
        cond  = self.visit(ctx.expression())
        lelse = self._newLabel()
        lend  = self._newLabel()
        self.emit("JUMPF", cond, None, lelse)
        self.visit(ctx.block(0))
        self.emit("JUMP", None, None, lend)
        self.emit("LABEL", None, None, lelse)
        self.visit(ctx.block(1))
        self.emit("LABEL", None, None, lend)
        return None

    def visitIfElseIf(self, ctx: MiniGOParser.IfElseIfContext):
        cond  = self.visit(ctx.expression())
        lelse = self._newLabel()
        self.emit("JUMPF", cond, None, lelse)
        self.visit(ctx.block())
        self.emit("LABEL", None, None, lelse)
        self.visit(ctx.ifStatement())
        return None

    def visitIfWithInit(self, ctx: MiniGOParser.IfWithInitContext):
        self.visit(ctx.simpleStatement())
        cond = self.visit(ctx.expression())
        lend = self._newLabel()
        self.emit("JUMPF", cond, None, lend)
        self.visit(ctx.block())
        self.emit("LABEL", None, None, lend)
        return None

    def visitIfWithInitElse(self, ctx: MiniGOParser.IfWithInitElseContext):
        self.visit(ctx.simpleStatement())
        cond  = self.visit(ctx.expression())
        lelse = self._newLabel()
        lend  = self._newLabel()
        self.emit("JUMPF", cond, None, lelse)
        self.visit(ctx.block(0))
        self.emit("JUMP", None, None, lend)
        self.emit("LABEL", None, None, lelse)
        self.visit(ctx.block(1))
        self.emit("LABEL", None, None, lend)
        return None

    def visitIfWithInitElseIf(self, ctx: MiniGOParser.IfWithInitElseIfContext):
        self.visit(ctx.simpleStatement())
        cond  = self.visit(ctx.expression())
        lelse = self._newLabel()
        self.emit("JUMPF", cond, None, lelse)
        self.visit(ctx.block())
        self.emit("LABEL", None, None, lelse)
        self.visit(ctx.ifStatement())
        return None

    # ── Arrays ────────────────────────────────────────────────────────────

    def visitIndexExpr(self, ctx: MiniGOParser.IndexExprContext):
        base  = self.visit(ctx.primaryExpression())
        index = self.visit(ctx.index().expression())
        t = self._newTemp()
        self.emit("ARRAY_LOAD", base, index, t)
        return t

    # ── Builtins ──────────────────────────────────────────────────────────

    def visitPrintlnStatement(self, ctx: MiniGOParser.PrintlnStatementContext):
        if ctx.expressionList() is not None:
            temps = self.visit(ctx.expressionList())
            for t in temps:
                self.emit("PRINTLN", t, None, None)
        return None

    def visitLengthExpr(self, ctx: MiniGOParser.LengthExprContext):
        operand = self.visit(ctx.lengthExpression().expression())
        t = self._newTemp()
        self.emit("LEN", operand, None, t)
        return t

    def visitCapExpr(self, ctx):
        return self._newTemp()

    def visitAppendExpr(self, ctx):
        return self._newTemp()

    def visitSelectorExpr(self, ctx):
        return self._newTemp()

    # ── Loops ─────────────────────────────────────────────────────────────

    def visitInfiniteLoop(self, ctx: MiniGOParser.InfiniteLoopContext):
        lstart = self._newLabel()
        self.emit("LABEL", None, None, lstart)
        self.visit(ctx.block())
        self.emit("JUMP", None, None, lstart)
        return None

    def visitWhileLoop(self, ctx: MiniGOParser.WhileLoopContext):
        lstart = self._newLabel()
        lend   = self._newLabel()
        self.emit("LABEL", None, None, lstart)
        cond = self.visit(ctx.expression())
        self.emit("JUMPF", cond, None, lend)
        self.visit(ctx.block())
        self.emit("JUMP", None, None, lstart)
        self.emit("LABEL", None, None, lend)
        return None

    def visitForLoop(self, ctx: MiniGOParser.ForLoopContext):
        self.visit(ctx.simpleStatement(0))   # init
        lstart = self._newLabel()
        lend   = self._newLabel()
        self.emit("LABEL", None, None, lstart)
        cond = self.visit(ctx.expression())
        self.emit("JUMPF", cond, None, lend)
        self.visit(ctx.block())
        self.visit(ctx.simpleStatement(1))   # post
        self.emit("JUMP", None, None, lstart)
        self.emit("LABEL", None, None, lend)
        return None

    def visitForLoopNoCondition(self, ctx: MiniGOParser.ForLoopNoConditionContext):
        self.visit(ctx.simpleStatement(0))   # init
        lstart = self._newLabel()
        self.emit("LABEL", None, None, lstart)
        self.visit(ctx.block())
        self.visit(ctx.simpleStatement(1))   # post
        self.emit("JUMP", None, None, lstart)
        return None

    # ── Switch: fuera del alcance — ignorar silenciosamente ───────────────

    def visitSwitchWithExpr(self, ctx):         return None
    def visitSwitchWithInitAndExpr(self, ctx):  return None
    def visitSwitchWithInit(self, ctx):         return None
    def visitSwitchEmpty(self, ctx):            return None
    def visitExpressionCaseClause(self, ctx):   return None
    def visitCaseClause(self, ctx):             return None
    def visitDefaultClause(self, ctx):          return None

    # ── Statements ────────────────────────────────────────────────────────

    def visitReturnStatement(self, ctx: MiniGOParser.ReturnStatementContext):
        if ctx.expression() is not None:
            val = self.visit(ctx.expression())
            self.emit("RETURN", val, None, None)
        else:
            self.emit("RETURN", None, None, None)
        return None
