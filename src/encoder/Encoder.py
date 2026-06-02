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
