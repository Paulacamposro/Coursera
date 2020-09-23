import math

def main():
    t = Triangulo(1, 1, 1)
    t.perimetro()

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        return (self.a + self.b + self.c)

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a != self.c and self.b != self.c and self.a != self.b:
            return 'escaleno'
        else:
            return 'isósceles'

main()
