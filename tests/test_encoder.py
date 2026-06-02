import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from antlr4 import CommonTokenStream, InputStream
from generated.MiniGOLexer import MiniGOLexer
from generated.MiniGOParser import MiniGOParser
from typechecker.TypeChecker import MiniGOTypeChecker
from typechecker.Decoraciones import Decoraciones
from encoder.Encoder import MiniGOEncoder
from encoder.Cuadrupla import Cuadrupla

def get_encoder(source: str) -> MiniGOEncoder:
    stream = InputStream(source)
    lexer = MiniGOLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniGOParser(tokens)
    tree = parser.root()
    dec = Decoraciones()
    tc = MiniGOTypeChecker(dec)
    tc.visit(tree)
    enc = MiniGOEncoder(dec)
    enc.visit(tree)
    return enc

def ops(enc: MiniGOEncoder) -> list[str]:
    return [i.op for i in enc.instrucciones]

def find(enc: MiniGOEncoder, op: str):
    return next((i for i in enc.instrucciones if i.op == op), None)

def find_all(enc: MiniGOEncoder, op: str):
    return [i for i in enc.instrucciones if i.op == op]

def test_cuadrupla_fields():
    c = Cuadrupla("ADD", "t1", "t2", "t3")
    assert c.op == "ADD"
    assert c.arg1 == "t1"
    assert c.arg2 == "t2"
    assert c.result == "t3"

def test_cuadrupla_str():
    c1 = Cuadrupla("ADD", "t1", "t2", "t3")
    assert str(c1) == "(ADD, t1, t2, t3)"

    c2 = Cuadrupla("LABEL", None, None, "L1")
    assert str(c2) == "(LABEL, -, -, L1)"

def test_encoder_vacio():
    enc = get_encoder("package p;")
    assert enc.instrucciones == []
