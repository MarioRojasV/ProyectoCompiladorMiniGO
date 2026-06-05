import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def compile_file(source_path):
    """Compila un .mgo. Retorna (éxito, errores, ll_path)."""
    import subprocess
    from antlr4 import FileStream, CommonTokenStream
    from generated.MiniGOLexer import MiniGOLexer
    from generated.MiniGOParser import MiniGOParser
    from syntaxchecker.ErrorListener import MiniGOErrorListener
    from typechecker.TypeChecker import MiniGOTypeChecker
    from typechecker.Decoraciones import Decoraciones
    from encoder.LLVMEncoder import LLVMEncoder

    try:
        input_stream = FileStream(source_path, encoding="utf-8")
    except IOError as e:
        return False, [f"Error al leer el archivo: {e}"], None

    lexer  = MiniGOLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGOParser(stream)

    errors = MiniGOErrorListener()
    lexer.removeErrorListeners();  lexer.addErrorListener(errors)
    parser.removeErrorListeners(); parser.addErrorListener(errors)

    tree = parser.root()

    if errors.hasErrors():
        return False, errors.getErrorList(), None

    decoraciones = Decoraciones()
    checker = MiniGOTypeChecker(decoraciones)
    checker.visit(tree)

    if checker.hasErrors():
        return False, checker.getErrorList(), None

    encoder = LLVMEncoder(decoraciones)
    encoder.visit(tree)
    ll_path = encoder.write_ir(source_path)

    return True, [], ll_path


if __name__ == "__main__":
    from gui.editor import MiniGOEditor
    app = MiniGOEditor()
    app.mainloop()
