import sys
import os
import subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from antlr4 import *
from generated.MiniGOLexer import MiniGOLexer
from generated.MiniGOParser import MiniGOParser
from syntaxchecker.ErrorListener import MiniGOErrorListener
from typechecker.TypeChecker import MiniGOTypeChecker
from typechecker.Decoraciones import Decoraciones

def compile_file(source_path):
    """Compila un archivo .mgo. Retorna (éxito, lista_de_errores, ll_path, bin_path)."""
    try:
        input_stream = FileStream(source_path, encoding="utf-8")
    except IOError as e:
        return False, [f"Error al leer el archivo: {e}"], None, None

    lexer  = MiniGOLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGOParser(stream)

    errors = MiniGOErrorListener()
    lexer.removeErrorListeners();  lexer.addErrorListener(errors)
    parser.removeErrorListeners(); parser.addErrorListener(errors)

    tree = parser.root()

    if errors.hasErrors():
        return False, errors.getErrorList(), None, None

    decoraciones = Decoraciones()
    checker = MiniGOTypeChecker(decoraciones)
    checker.visit(tree)

    if checker.hasErrors():
        return False, checker.getErrorList(), None, None

    from encoder.LLVMEncoder import LLVMEncoder
    encoder = LLVMEncoder(decoraciones)
    encoder.visit(tree)
    ll_path = encoder.write_ir(source_path)

    # Intentar compilar con clang
    base = os.path.splitext(source_path)[0]
    bin_path = base + (".exe" if sys.platform == "win32" else "")
    try:
        result = subprocess.run(
            ["clang", ll_path, "-o", bin_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            return True, [], ll_path, None
    except FileNotFoundError:
        return True, [], ll_path, None

    return True, [], ll_path, bin_path


def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py <archivo.mgo>")
        sys.exit(1)

    source = sys.argv[1]
    ok, errs, ll_path, bin_path = compile_file(source)

    if not ok:
        print("\033[38;5;166m")
        for e in errs:
            print(e)
        print("\033[31mCompilation failed!\033[0m")
        sys.exit(1)

    if bin_path:
        print(f"\033[32mCompilado exitosamente → {bin_path}\033[0m")
        print(f"LLVM IR guardado en: {ll_path}")
    else:
        print(f"\033[32mLLVM IR generado: {ll_path}\033[0m")
        print(f"Para ejecutar: python src/runner.py {ll_path}")


if __name__ == "__main__":
    main()
