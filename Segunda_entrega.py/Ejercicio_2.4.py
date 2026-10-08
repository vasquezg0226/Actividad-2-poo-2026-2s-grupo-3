import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.pow(self.base * self.base + self.altura * self.altura, 0.5)

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.base == hipotenusa and self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


# EJERCICIO PROPUESTO: nueva clase Rombo
class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return self.diagonal_mayor * self.diagonal_menor / 2

    def calcular_perimetro(self):
        lado = math.sqrt((self.diagonal_mayor / 2) ** 2 + (self.diagonal_menor / 2) ** 2)
        return 4 * lado


# EJERCICIO PROPUESTO: nueva clase Trapecio
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2


if __name__ == "__main__":
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    print("El área del círculo es =", figura1.calcular_area())
    print("El perímetro del círculo es =", figura1.calcular_perimetro())
    print()
    print("El área del rectángulo es =", figura2.calcular_area())
    print("El perímetro del rectángulo es =", figura2.calcular_perimetro())
    print()
    print("El área del cuadrado es =", figura3.calcular_area())
    print("El perímetro del cuadrado es =", figura3.calcular_perimetro())
    print()
    print("El área del triángulo es =", figura4.calcular_area())
    print("El perímetro del triángulo es =", figura4.calcular_perimetro())
    figura4.determinar_tipo_triangulo()
    print()
    # EJERCICIO PROPUESTO: probar el rombo y el trapecio
    figura5 = Rombo(8, 6)
    print("El área del rombo es =", figura5.calcular_area())
    print("El perímetro del rombo es =", figura5.calcular_perimetro())
    print()
    figura6 = Trapecio(10, 6, 4, 5, 5)
    print("El área del trapecio es =", figura6.calcular_area())
    print("El perímetro del trapecio es =", figura6.calcular_perimetro())
    