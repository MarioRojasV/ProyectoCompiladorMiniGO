import sys
sys.path.insert(0, 'src/generated')

from antlr4 import *
from MiniGOLexer import MiniGOLexer
from MiniGOParser import MiniGOParser

def main():
    input_stream = FileStream('tests/test1.mgo')
    lexer = MiniGOLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGOParser(stream)
    tree = parser.root()
    print(tree.toStringTree(recog=parser))

main()
