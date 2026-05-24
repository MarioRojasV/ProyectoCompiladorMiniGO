class TablaSimbolos:

    class Ident:
        def __init__(self, token, tipo, nivel, decl):
            self.token = token
            self.tipo = tipo
            self.nivel = nivel
            self.decl = decl

    class VarIdent(Ident):
        def __init__(self, token, tipo, nivel, decl):
            super().__init__(token, tipo, nivel, decl)

    class MethodIdent(Ident):
        def __init__(self, token, tipo, params, nivel, decl):
            super().__init__(token, tipo, nivel, decl)
            self.params = params  # lista de tipos de parámetros

    class StructIdent(Ident):
        def __init__(self, token, nivel, campos, decl):
            super().__init__(token, "struct", nivel, decl)
            self.campos = campos  # dict nombre → tipo

    def __init__(self):
        self.tabla = []
        self.nivelActual = -1

    def getNivelActual(self):
        return self.nivelActual

    def insertarVar(self, token, tipo, decl):
        ident = self.VarIdent(token, tipo, self.nivelActual, decl)
        self.tabla.insert(0, ident)

    def insertarMethod(self, token, tipo, params, decl):
        ident = self.MethodIdent(token, tipo, params, self.nivelActual, decl)
        self.tabla.insert(0, ident)

    def insertarStruct(self, token, campos, decl):
        ident = self.StructIdent(token, self.nivelActual, campos, decl)
        self.tabla.insert(0, ident)

    def buscar(self, nombre):
        for ident in self.tabla:
            if ident.token.text == nombre:
                return ident
        return None

    def buscarNivelActual(self, nombre):
        for ident in self.tabla:
            if ident.nivel == self.nivelActual:
                if ident.token.text == nombre:
                    return ident
            else:
                break
        return None

    def openScope(self):
        self.nivelActual += 1

    def closeScope(self):
        self.tabla = [i for i in self.tabla if i.nivel != self.nivelActual]
        self.nivelActual -= 1

    def imprimir(self):
        print("----- INICIO TABLA ------")
        for ident in self.tabla:
            print(f"Nombre: {ident.token.text} - Nivel: {ident.nivel} - Tipo: {ident.tipo}")
        print("----- FIN TABLA ------")
