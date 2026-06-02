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

def test_int_literal_en_asignacion():
    # Requiere Task 3 para generar ASSIGN, por ahora solo verifica que no crashea
    enc = get_encoder("package p;")
    assert enc.instrucciones == []

def test_literales_no_crashea():
    # Programa mínimo válido con literales — no debe crashear
    enc = get_encoder("package p; var x int = 5;")
    # No hay ASSIGN todavía (Task 3 lo implementa), pero no debe lanzar excepción
    assert isinstance(enc.instrucciones, list)

def test_true_false_identificadores():
    # Verificar que visitIdentifierOperand retorna "true"/"false" correctamente
    # Esto se verificará mejor en Task 7 con return; por ahora solo no crashea
    enc = get_encoder("package p;")
    assert enc.instrucciones == []

def test_var_decl_con_tipo_y_valor():
    enc = get_encoder("package p; var x int = 5;")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.result == "x" and i.arg1 == "5" for i in assigns)

def test_var_decl_sin_valor_int():
    enc = get_encoder("package p; var x int;")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.arg1 == "0" and i.result == "x" for i in assigns)

def test_var_decl_sin_valor_bool():
    enc = get_encoder("package p; var b bool;")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.arg1 == "false" and i.result == "b" for i in assigns)

def test_var_decl_sin_valor_string():
    enc = get_encoder("package p; var s string;")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.arg1 == '""' and i.result == "s" for i in assigns)

def test_suma():
    enc = get_encoder("package p; func f() { var x int = 3 + 2; };")
    add = find(enc, "ADD")
    assert add is not None
    assert add.arg1 == "3"
    assert add.arg2 == "2"
    assert add.result is not None

def test_resta():
    enc = get_encoder("package p; func f() { var x int = 10 - 4; };")
    assert find(enc, "SUB") is not None

def test_mult():
    enc = get_encoder("package p; func f() { var x int = 3 * 4; };")
    assert find(enc, "MUL") is not None

def test_div():
    enc = get_encoder("package p; func f() { var x int = 10 / 2; };")
    assert find(enc, "DIV") is not None

def test_mod():
    enc = get_encoder("package p; func f() { var x int = 10 % 3; };")
    assert find(enc, "MOD") is not None

def test_negacion_unaria():
    enc = get_encoder("package p; func f() int { return -5; };")
    assert find(enc, "UMINUS") is not None

def test_suma_variables():
    enc = get_encoder("""
package p;
func f() {
    var a int = 3;
    var b int = 2;
    var c int = a + b;
};
""")
    add = find(enc, "ADD")
    assert add is not None
    assert add.arg1 == "a"
    assert add.arg2 == "b"

def test_comparacion_eq():
    enc = get_encoder("package p; func f() bool { return 3 == 3; };")
    assert find(enc, "EQ") is not None

def test_comparacion_lt():
    enc = get_encoder("package p; func f() bool { return 3 < 5; };")
    cmp = find(enc, "LT")
    assert cmp is not None
    assert cmp.arg1 == "3"
    assert cmp.arg2 == "5"

def test_logico_and():
    enc = get_encoder("package p; func f() bool { return true && false; };")
    assert find(enc, "AND") is not None

def test_logico_not():
    enc = get_encoder("package p; func f() bool { return !true; };")
    not_instr = find(enc, "NOT")
    assert not_instr is not None
    assert not_instr.arg1 == "true"

def test_asignacion_simple():
    enc = get_encoder("""
package p;
func f() {
    var x int = 0;
    x = 5;
};
""")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.result == "x" and i.arg1 == "5" for i in assigns)

def test_short_var_decl():
    enc = get_encoder("""
package p;
func f() {
    x := 42;
};
""")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.result == "x" and i.arg1 == "42" for i in assigns)

def test_compound_assign_plus():
    enc = get_encoder("""
package p;
func f() {
    var x int = 0;
    x += 5;
};
""")
    add = find(enc, "ADD")
    assert add is not None
    assert add.arg1 == "x"
    assert add.arg2 == "5"
    assigns = find_all(enc, "ASSIGN")
    assert any(i.result == "x" for i in assigns)

def test_inc_dec():
    enc = get_encoder("""
package p;
func f() {
    var x int = 0;
    x++;
    x--;
};
""")
    assert find(enc, "ADD") is not None
    assert find(enc, "SUB") is not None

def test_func_decl_emite_label():
    enc = get_encoder("package p; func suma(a int, b int) int { return a + b; };")
    labels = find_all(enc, "LABEL")
    assert any(i.result == "suma" for i in labels)

def test_func_call_emite_param_y_call():
    enc = get_encoder("""
package p;
func suma(a int, b int) int { return a + b; };
func f() {
    var r int = suma(1, 2);
};
""")
    params = find_all(enc, "PARAM")
    assert len(params) == 2
    assert params[0].result == "1"
    assert params[1].result == "2"
    call = find(enc, "CALL")
    assert call is not None
    assert call.arg1 == "suma"
    assert call.arg2 == "2"  # número de argumentos

def test_return_con_valor():
    enc = get_encoder("package p; func f() int { return 42; };")
    ret = find(enc, "RETURN")
    assert ret is not None
    assert ret.arg1 == "42"

def test_return_sin_valor():
    enc = get_encoder("package p; func f() { return; };")
    ret = find(enc, "RETURN")
    assert ret is not None
    assert ret.arg1 is None

def test_simple_if():
    enc = get_encoder("""
package p;
func f() {
    var x int = 5;
    if x > 0 {
        x = 1;
    };
};
""")
    # Debe haber GT, JUMPF, ASSIGN, LABEL
    assert find(enc, "GT") is not None
    assert find(enc, "JUMPF") is not None
    labels = find_all(enc, "LABEL")
    assert len(labels) >= 1  # al menos Lend

def test_if_else():
    enc = get_encoder("""
package p;
func f() {
    var x int = 5;
    if x > 0 {
        x = 1;
    } else {
        x = 2;
    };
};
""")
    jumpf = find(enc, "JUMPF")
    jump  = find(enc, "JUMP")
    labels = find_all(enc, "LABEL")
    assert jumpf is not None
    assert jump  is not None
    assert len(labels) >= 2  # Lelse y Lend

def test_if_with_init():
    enc = get_encoder("""
package p;
func f() {
    if x := 5; x > 0 {
        x = 1;
    };
};
""")
    # La declaración del init (x := 5) debe generar ASSIGN antes del JUMPF
    assigns = find_all(enc, "ASSIGN")
    jumpf   = find(enc, "JUMPF")
    assert any(i.result == "x" for i in assigns)
    assert jumpf is not None

def test_while_loop():
    enc = get_encoder("""
package p;
func f() {
    var x int = 5;
    for x > 0 {
        x--;
    };
};
""")
    labels = find_all(enc, "LABEL")
    assert len(labels) >= 2  # Lstart y Lend
    assert find(enc, "JUMPF") is not None
    assert find(enc, "JUMP")  is not None

def test_for_loop_con_init_y_post():
    enc = get_encoder("""
package p;
func f() {
    for i := 0; i < 10; i++ {
        var x int = i;
    };
};
""")
    assigns = find_all(enc, "ASSIGN")
    assert any(i.result == "i" for i in assigns)  # init i := 0
    assert find(enc, "LT")    is not None          # condición
    assert find(enc, "JUMPF") is not None
    assert find(enc, "ADD")   is not None          # i++

def test_infinite_loop():
    enc = get_encoder("""
package p;
func f() {
    for {
        var x int = 1;
    };
};
""")
    labels = find_all(enc, "LABEL")
    jumps  = find_all(enc, "JUMP")
    assert len(labels) >= 1
    assert len(jumps)  >= 1
    label_names = {l.result for l in labels}
    assert any(j.result in label_names for j in jumps)

def test_for_sin_condicion():
    enc = get_encoder("""
package p;
func f() {
    for i := 0;; i++ {
        var x int = i;
    };
};
""")
    labels = find_all(enc, "LABEL")
    jumps  = find_all(enc, "JUMP")
    assert len(labels) >= 1
    assert len(jumps)  >= 1
    assert find(enc, "JUMPF") is None
