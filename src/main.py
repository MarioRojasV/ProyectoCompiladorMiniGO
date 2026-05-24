from antlr4 import FileStream
from antlr4 import FileStream
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from antlr4 import *
from generated.MiniGOLexer import MiniGOLexer
from generated.MiniGOParser import MiniGOParser
from syntaxchecker.ErrorListener import MiniGOErrorListener
from typechecker.TypeChecker import MiniGOTypeChecker
from typechecker.Decoraciones import Decoraciones

def main():
    try:
        if len(sys.argv) < 2:
            print("Uso: python3 src/main.py <archivo.mgo>")
            sys.exit(1)
        input_stream = FileStream(sys.argv[1])
        #input_stream = FileStream("tests/test_func_calls.mgo")

        # Lexer
        lexer = MiniGOLexer(input_stream)

        # Tokens
        stream = CommonTokenStream(lexer)

        # Parser
        parser = MiniGOParser(stream)

        # Error listener
        errors = MiniGOErrorListener()
        lexer.removeErrorListeners()
        parser.removeErrorListeners()
        lexer.addErrorListener(errors)
        parser.addErrorListener(errors)

        # Regla inicial
        tree = parser.root()

        if errors.hasErrors():
            print("\033[38;5;166m")
            for error in errors.getErrorList():
                print(error)
            print("\033[31mCompilation failed!" + "\033[0m")
        else:
            # Type checker
            decoraciones = Decoraciones()
            typeChecker = MiniGOTypeChecker(decoraciones)
            typeChecker.visit(tree)

            if typeChecker.hasErrors():
                print("\033[31mCompilation failed!")
                for error in typeChecker.getErrorList():
                    print(error)
                print("\033[0m")
            else:
                print("\033[32mCompilation successful!")
                print("\033[36m" +tree.toStringTree(recog=parser) + "\033[0m")

    except IOError as e:
        print(f"\033[31mError al leer el archivo: {e}\033[0m")

main()