import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generated.MiniGOVisitor import MiniGOVisitor
from generated.MiniGOParser import MiniGOParser
from typechecker.Decoraciones import Decoraciones
from encoder.Cuadrupla import Cuadrupla


def _is_literal(val: str | None) -> bool:
    """True si el valor es un literal y no un nombre de temp."""
    if val is None:
        return False
    if val in ("true", "false"):
        return True
    if val.startswith('"') or val.startswith("'") or val.startswith("`"):
        return True
    try:
        float(val)
        return True
    except ValueError:
        return False


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
        nombre = ctx.IDENTIFIER().getText()
        # true y false son literales bool tratados como identificadores
        if nombre in ("true", "false"):
            return nombre
        return nombre

    # ── Declaraciones de variables ────────────────────────────────────────

    _DEFAULT_VALUES = {
        "int": "0", "float64": "0.0", "bool": "false",
        "string": '""', "rune": "'\\x00'",
    }

    def _defaultValue(self, tipo: str) -> str:
        return self._DEFAULT_VALUES.get(tipo, "0")

    def visitVarDeclWithTypeAndValue(self, ctx: MiniGOParser.VarDeclWithTypeAndValueContext):
        exprs = self.visit(ctx.expressionList())
        ids   = ctx.identifierList().IDENTIFIER()
        for i, id_node in enumerate(ids):
            val  = exprs[i] if i < len(exprs) else "0"
            name = id_node.getText()
            self.emit("ASSIGN", val, None, name)
        return None

    def visitVarDeclWithValue(self, ctx: MiniGOParser.VarDeclWithValueContext):
        exprs = self.visit(ctx.expressionList())
        ids   = ctx.identifierList().IDENTIFIER()
        for i, id_node in enumerate(ids):
            val  = exprs[i] if i < len(exprs) else "0"
            name = id_node.getText()
            self.emit("ASSIGN", val, None, name)
        return None

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

    def _visitLValue(self, expr_ctx) -> str:
        """Extrae el nombre de variable del lado izquierdo de una asignación.
        Retorna str (nombre de var). En Task 10 se extiende para arrays."""
        if isinstance(expr_ctx, MiniGOParser.PrimaryExprContext):
            inner = expr_ctx.primaryExpression()
            return self._visitLValue(inner)
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
            lname = self._visitLValue(lctx)
            self.emit("ASSIGN", rtemp, None, lname)
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

    # ── Statements ────────────────────────────────────────────────────────

    def visitReturnStatement(self, ctx):
        if ctx.expression() is not None:
            self.visit(ctx.expression())
        return None
