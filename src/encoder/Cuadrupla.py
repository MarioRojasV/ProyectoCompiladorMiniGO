from dataclasses import dataclass

@dataclass
class Cuadrupla:
    op: str
    arg1: str | None
    arg2: str | None
    result: str | None

    def __str__(self):
        a1 = self.arg1 if self.arg1 is not None else "-"
        a2 = self.arg2 if self.arg2 is not None else "-"
        r  = self.result if self.result is not None else "-"
        return f"({self.op}, {a1}, {a2}, {r})"
