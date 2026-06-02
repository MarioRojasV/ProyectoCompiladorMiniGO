import sys, os
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
