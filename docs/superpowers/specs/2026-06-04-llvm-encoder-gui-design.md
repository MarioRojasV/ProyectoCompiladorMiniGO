# Diseño: LLVMEncoder + Editor GUI — Compilador MiniGO

**Fecha:** 2026-06-04  
**Entrega:** Lunes 8 de junio de 2026 — Grupo 51

---

## Contexto

El compilador MiniGO ya tiene léxico, sintaxis y chequeo de tipos completos. El encoder actual produce cuádruplas (IR propio). El objetivo es reemplazarlo con un encoder LLVM real usando `llvmlite` y agregar un editor GUI con tkinter.

---

## Arquitectura General

```
Fuente (.mgo)
     │
     ▼
Lexer + Parser (ANTLR4) — sin cambios
     │
     ▼
TypeChecker — sin cambios
     │
     ▼
LLVMEncoder (reemplaza Encoder.py)
     │
     ▼
llvmlite → .ll (LLVM IR texto)
     │
     ▼
clang → binario ejecutable x86
```

---

## Archivos afectados

| Archivo | Acción |
|---|---|
| `src/encoder/LLVMEncoder.py` | Crear |
| `src/encoder/Encoder.py` | Eliminar |
| `src/encoder/Cuadrupla.py` | Eliminar |
| `src/main.py` | Modificar: usar LLVMEncoder, invocar clang |
| `src/gui/__init__.py` | Crear |
| `src/gui/editor.py` | Crear |
| `requirements.txt` | Crear con llvmlite |

---

## LLVMEncoder

### Estructura interna

```python
class LLVMEncoder(MiniGOVisitor):
    module: ir.Module          # módulo LLVM del programa
    builder: ir.IRBuilder      # emite instrucciones en bloque actual
    func_map: dict             # nombre → ir.Function
    var_map: dict              # nombre → alloca pointer (por scope)
    printf_func: ir.Function   # referencia a printf externa
```

### Mapeo de tipos MiniGO → LLVM IR

| MiniGO | LLVM IR |
|---|---|
| `int` | `i64` |
| `float64` | `double` |
| `bool` | `i1` |
| `string` / rawstring | `i8*` (ptr a global constante) |
| `[N]int` | `[N x i64]` |
| `[]int` (slice) | `i64*` + longitud como variable separada |

### Patrón de variables

```
declaración → builder.alloca(tipo, name)  → guarda ptr en var_map
asignación  → builder.store(valor, ptr)
uso         → builder.load(tipo, ptr, name)
```

### Control de flujo

- **if / if-else / if-else if:** bloques `then`, `else`, `merge` + `builder.cbranch`
- **for (loop):** bloques `header`, `body`, `exit` + back-edge con `builder.branch`
- **switch:** bloques por caso + bloque `default` + `builder.switch`

### Builtins

| Función | Implementación |
|---|---|
| `println(x)` | Declara `printf` externa; selecciona formato `%d\n`, `%f\n`, `%s\n` según tipo |
| `len(arr)` | Retorna constante `i64` del tamaño del array (conocido en compile-time) |
| `cap(arr)` | Igual que `len` para arrays de tamaño fijo |

### Features a incluir

- Variables globales y locales (int, float64, bool, string)
- Funciones con parámetros y retorno
- Arrays de enteros: declaración, acceso por índice, len
- Slices de enteros: declaración, acceso, len, cap (sin append en codegen)
- Structs: acceso a campos vía `getelementptr`
- If / for / switch
- Expresiones aritméticas (+, -, *, /, %) y lógicas (==, !=, <, <=, >, >=, &&, ||, !)
- println para tipos simples, len, cap

### Salida

`main.py` genera `output.ll`, luego invoca:
```
clang output.ll -o output
```
Si `clang` no está disponible, deja el `.ll` y reporta instrucciones al usuario.

---

## Editor GUI (tkinter)

### Layout

```
┌─────────────────────────────────────────────┐
│  [Abrir]  [Guardar]  [Compilar]  [Ejecutar] │
├──────────────────────────┬──────────────────┤
│                          │  ERRORES         │
│   Editor de código       │  Lín 5, Col 3:   │
│   (.mgo)                 │  tipo inválido   │
│                          │                  │
│                          │  OUTPUT          │
│                          │  Hello World     │
├──────────────────────────┴──────────────────┤
│  Lín: 1  Col: 1  │  archivo.mgo            │
└─────────────────────────────────────────────┘
```

### Componentes

| Widget | Función |
|---|---|
| `Text` (izquierdo) | Editor con números de línea sincronizados |
| Panel errores (`Text`) | Click en error salta a línea/col en editor |
| Panel output (`Text`) | Muestra stdout del binario ejecutado |
| Barra de estado | Línea y columna actuales del cursor |

### Flujo Compilar

1. Guarda archivo actual (temp si no tiene nombre)
2. Llama `python main.py <archivo>` via `subprocess.run`
3. Captura stderr → parsea errores con regex `línea:col: mensaje`
4. Muestra errores clickeables en panel de errores
5. Si éxito: muestra "Compilado OK" en barra de estado

### Flujo Ejecutar

1. Requiere compilación previa exitosa
2. Corre el binario generado via `subprocess.run`
3. Muestra stdout en panel output

---

## Orden de implementación

1. `requirements.txt` + instalar llvmlite
2. `LLVMEncoder.py` — variables, expresiones, funciones
3. `LLVMEncoder.py` — control de flujo (if, for, switch)
4. `LLVMEncoder.py` — arrays, slices, structs, builtins
5. Actualizar `main.py` para usar LLVMEncoder + invocar clang
6. `src/gui/editor.py` — editor tkinter completo
7. Commits y pruebas finales
