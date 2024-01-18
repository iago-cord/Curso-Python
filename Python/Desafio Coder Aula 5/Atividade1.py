class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area (self):
        return self.base * self.altura

    def perimetro(self):
        return self.base + self.altura