# Encoder — Generador de Código Intermedio (IR) para MiniGO

**Fecha:** 2026-06-01
**Estado:** Aprobado

---

## Contexto

El compilador MiniGO ya cuenta con lexer/parser (ANTLR4) y type checker completo. Esta fase agrega el encoder: un visitor que recorre el AST tipado y produce código intermedio en formato cuádruplas. El spec oficial del proyecto (Definición Compilador miniGo.doc) define el alcance de lo que debe generarse.

---

## Alcance del encoder (según spec oficial)

- Variables de tipos simples (int, float64, string, bool, rune) — globales y locales. Solo las dos formas más simples de declaración tipada: `var x T = expr` y `var x T`.
- Arrays de enteros (`[N]int`) — forma más simple de declaración tipada.
- Métodos (procedimientos y funciones): declaración, llamada, retorno.
- Control de flujo: `if`, `if-else`, `if-else if`, `if` con init, `for` (todas las variantes). Sin `break`, `continue` ni `switch`.
- Builtin `println` para tipos simples. Builtin `len` para arrays de enteros.
- Expresiones: `+`, `-`, `*`, `/`, `%` y operadores de comparación `==`, `!=`, `>`, `<`, `>=`, `<=`. Se incluyen también `&&`, `||`, `!` y negación unaria `-` ya que el TypeChecker los valida y el esfuerzo es mínimo.
- RawString solo dentro de `println`.

---

## Arquitectura

### Estructura de archivos

```
src/encoder/
├── __init__.py        (ya existe)
├── Cuadrupla.py       → dataclass que representa una instrucción IR
└── Encoder.py         → visitor ANTLR que genera la lista de cuádruplas
```

### Flujo de compilación

```
Lexer → Parser → TypeChecker → Encoder → salida (.ir + consola)
```

El encoder solo se invoca si el TypeChecker no reportó errores. Recibe el árbol AST y el objeto `Decoraciones` ya poblado por el TypeChecker.

### Integración en `main.py`

```python
from encoder.Encoder import MiniGOEncoder

encoder = MiniGOEncoder(decoraciones)
encoder.visit(tree)
encoder.printIR()            # imprime en consola
encoder.write(sys.argv[1])   # escribe tests/foo.ir junto al .mgo
```

---

## Representación de cuádruplas

```python
@dataclass
class Cuadrupla:
    op: str
    arg1: str | None
    arg2: str | None
    result: str | None
```

### Instruction set

| op | arg1 | arg2 | result | descripción |
|---|---|---|---|---|
| `ASSIGN` | valor o temp | — | destino | asignación |
| `ADD` | t1 | t2 | t3 | suma |
| `SUB` | t1 | t2 | t3 | resta |
| `MUL` | t1 | t2 | t3 | multiplicación |
| `DIV` | t1 | t2 | t3 | división |
| `MOD` | t1 | t2 | t3 | módulo |
| `UMINUS` | t1 | — | t2 | negación unaria |
| `EQ` | t1 | t2 | t3 | == |
| `NEQ` | t1 | t2 | t3 | != |
| `LT` | t1 | t2 | t3 | < |
| `LEQ` | t1 | t2 | t3 | <= |
| `GT` | t1 | t2 | t3 | > |
| `GEQ` | t1 | t2 | t3 | >= |
| `AND` | t1 | t2 | t3 | && |
| `OR` | t1 | t2 | t3 | \|\| |
| `NOT` | t1 | — | t2 | ! |
| `LABEL` | — | — | Ln | etiqueta de salto |
| `JUMP` | — | — | Ln | salto incondicional |
| `JUMPF` | cond | — | Ln | salta si falso |
| `PARAM` | — | — | t1 | pasa argumento a función |
| `CALL` | nombre | #args | t1 | llamada a función |
| `RETURN` | valor o — | — | — | retorno de función |
| `PRINTLN` | t1 | — | — | print con newline |
| `LEN` | t1 | — | t2 | largo de arreglo |
| `ARRAY_LOAD` | nombre_arr | índice | t | leer arr[i] |
| `ARRAY_STORE` | valor | índice | nombre_arr | escribir arr[i] = valor |

---

## Flujo interno del Encoder

### Estado interno

```python
class MiniGOEncoder(MiniGOVisitor):
    instrucciones: list[Cuadrupla]
    _temp_count: int    # genera t1, t2, t3...
    _label_count: int   # genera L1, L2, L3...
```

### Variables y arreglos

- Variables globales y locales reciben el mismo tratamiento en IR; la distinción de scope ya fue resuelta por el TypeChecker.
- Al declarar con valor: emitir `ASSIGN valor temp`, luego `ASSIGN temp var`.
- Al declarar sin valor: emitir `ASSIGN 0 - var` (enteros), `ASSIGN "" - var` (strings), `ASSIGN false - var` (bool), etc.
- Arrays: se acceden mediante `ARRAY_LOAD` / `ARRAY_STORE` con nombre del arreglo e índice evaluado.
- `UPLUS` (operador `+` unario) es un no-op: retorna el temp del hijo sin emitir instrucción.

### Funciones

Al entrar a `visitFuncDecl`:
1. Emitir `LABEL - - nombre_func`.
2. Visitar el cuerpo normalmente.
3. `RETURN` cierra la función.

Al generar una llamada (`visitCallExpr`):
1. Evaluar cada argumento → temp.
2. Emitir `PARAM - - ti` por cada argumento (en orden).
3. Emitir `CALL nombre #args t_resultado`.

### Control de flujo — If

```
# if cond { body } else { alt }
<evaluar cond → t1>
JUMPF  t1   -   Lelse
<body>
JUMP   -    -   Lend
LABEL  -    -   Lelse
<alt>
LABEL  -    -   Lend
```

Para `if` sin `else`, se omite el `JUMP` y el bloque `alt`.
Para `if` con init (`if stmt; cond { ... }`), se emite el `stmt` antes de evaluar `cond`.

### Control de flujo — For (while-style)

```
LABEL  -  -  Lstart
<evaluar cond → t1>
JUMPF  t1  -  Lend
<body>
JUMP   -   -  Lstart
LABEL  -   -  Lend
```

Para `for` con init y post (`for init; cond; post { body }`):
```
<init>
LABEL  -  -  Lstart
<evaluar cond → t1>
JUMPF  t1  -  Lend
<body>
<post>
JUMP   -   -  Lstart
LABEL  -   -  Lend
```

Para `for` con init y sin condición (`for init;; post { body }`):
```
<init>
LABEL  -  -  Lstart
<body>
<post>
JUMP   -   -  Lstart
```

Para `for` infinito (`for { body }`):
```
LABEL  -  -  Lstart
<body>
JUMP   -   -  Lstart
```

### Expresiones

Cada expresión retorna un nombre de temp (string). Las hojas retornan directamente su nombre o literal sin emitir instrucción.

---

## Manejo de errores

El encoder asume que el AST ya fue validado por el TypeChecker. No reporta errores de tipo. Los nodos fuera del alcance del encoder (structs, slices, switch, break, continue) se ignoran silenciosamente — no interrumpen la generación.

---

## Formato de salida

### Consola

```
=== Código Intermedio ===
(ASSIGN, 5, -, t1)
(ASSIGN, t1, -, x)
(LABEL, -, -, main)
(PARAM, -, -, t1)
(CALL, println, 1, t2)
```

### Archivo `.ir`

Mismo contenido que consola. Se guarda junto al archivo fuente:
- entrada: `tests/test_vars.mgo`
- salida: `tests/test_vars.ir`
