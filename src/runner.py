"""
runner.py — ejecuta un .ll con el JIT de llvmlite (sin clang).
Uso: python src/runner.py <archivo.ll>
"""
import sys
import os
import ctypes


def run(ll_path):
    import llvmlite.binding as llvm

    with open(ll_path, encoding="utf-8") as f:
        ir_text = f.read()

    # Asegurar que el triple sea el nativo (no "unknown-unknown-unknown")
    native_triple = llvm.get_default_triple()
    ir_text = ir_text.replace(
        'target triple = "unknown-unknown-unknown"',
        f'target triple = "{native_triple}"'
    )

    try:
        mod = llvm.parse_assembly(ir_text)
        mod.verify()
    except Exception as e:
        print(f"Error en IR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target  = llvm.Target.from_triple(native_triple)
        tm      = target.create_target_machine()
        engine  = llvm.create_mcjit_compiler(mod, tm)
    except Exception as e:
        print(f"Error al crear JIT ({e})\n"
              "Instalá LLVM para usar clang:  winget install LLVM.LLVM",
              file=sys.stderr)
        sys.exit(2)

    engine.finalize_object()
    engine.run_static_constructors()

    try:
        func_ptr = engine.get_function_address("main")
    except Exception:
        print("ERROR: No hay función 'main'.\n"
              "MiniGO requiere  func main()  como punto de entrada.", file=sys.stderr)
        sys.exit(1)

    cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
    ret   = cfunc()
    sys.exit(ret)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python src/runner.py <archivo.ll>")
        sys.exit(1)
    run(sys.argv[1])
