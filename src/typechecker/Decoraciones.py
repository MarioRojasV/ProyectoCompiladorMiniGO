class Decoraciones:
    def __init__(self):
        self.tipos = {}       # id(ctx) → tipo de la expresión
        self.referencias = {} # id(ctx) → Ident de la tabla de símbolos

    def setTipo(self, ctx, tipo):
        self.tipos[id(ctx)] = tipo

    def getTipo(self, ctx):
        return self.tipos.get(id(ctx), None)

    def setRef(self, ctx, ident):
        self.referencias[id(ctx)] = ident

    def getRef(self, ctx):
        return self.referencias.get(id(ctx), None)
