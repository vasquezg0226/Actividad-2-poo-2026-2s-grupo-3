from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0, tipo=None, es_observable=False,
                 periodo_orbital=0.0, periodo_rotacion=0.0):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
        # EJERCICIO PROPUESTO: nuevos atributos en el constructor
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def imprimir(self):
        print("Nombre del planeta =", self.nombre)
        print("Cantidad de satélites =", self.cantidad_satelites)
        print("Masa del planeta =", self.masa)
        print("Volumen del planeta =", self.volumen)
        print("Diámetro del planeta =", self.diametro)
        print("Distancia al sol =", self.distancia_sol)
        print("Tipo de planeta =", self.tipo.value)
        print("Es observable =", self.es_observable)
        # EJERCICIO PROPUESTO: imprimir los nuevos atributos
        print("Periodo orbital (años) =", self.periodo_orbital)
        print("Periodo de rotación (días) =", self.periodo_rotacion)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite = 149597870 * 3.4
        return self.distancia_sol > limite


if __name__ == "__main__":
    # EJERCICIO PROPUESTO: los planetas ahora reciben periodo orbital y de rotación
    p1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000,
                 TipoPlaneta.TERRESTRE, True, 1.0, 1.0)
    p1.imprimir()
    print("Densidad del planeta =", p1.calcular_densidad())
    print("Es planeta exterior =", p1.es_planeta_exterior())
    print()
    p2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000,
                 TipoPlaneta.GASEOSO, True, 11.86, 0.41)
    p2.imprimir()
    print("Densidad del planeta =", p2.calcular_densidad())
    print("Es planeta exterior =", p2.es_planeta_exterior())