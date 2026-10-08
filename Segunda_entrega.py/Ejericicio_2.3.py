from enum import Enum


class TipoCom(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoA(Enum):
    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class TipoColor(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color,
                 es_automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0
        # EJERCICIO PROPUESTO: nuevo atributo es_automatico y control de multas
        self.es_automatico = es_automatico
        self.cantidad_multas = 0
        self.valor_multas = 0

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # EJERCICIO PROPUESTO: get del nuevo atributo
    def get_es_automatico(self):
        return self.es_automatico

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    # EJERCICIO PROPUESTO: set del nuevo atributo
    def set_es_automatico(self, es_automatico):
        self.es_automatico = es_automatico

    def acelerar(self, incremento_velocidad):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_actual + incremento_velocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")
            # EJERCICIO PROPUESTO: al superar la velocidad máxima se genera una multa que crece con cada intento
            self.cantidad_multas += 1
            self.valor_multas += 50000 * self.cantidad_multas

    def desacelerar(self, decremento_velocidad):
        if self.velocidad_actual - decremento_velocidad > 0:
            self.velocidad_actual = self.velocidad_actual - decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        return distancia / self.velocidad_actual

    # EJERCICIO PROPUESTO: determinar si tiene multas y el valor total de multas
    def tiene_multas(self):
        return self.cantidad_multas > 0

    # EJERCICIO PROPUESTO: valor total de las multas
    def calcular_total_multas(self):
        return self.valor_multas

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.tipo_combustible.name)
        print("Tipo de automóvil =", self.tipo_automovil.name)
        print("Número de puertas =", self.numero_puertas)
        print("Cantidad de asientos =", self.cantidad_asientos)
        print("Velocidad máxima =", self.velocidad_maxima)
        print("Color =", self.color.name)
        # EJERCICIO PROPUESTO: imprimir el nuevo atributo
        print("Es automático =", self.es_automatico)


if __name__ == "__main__":
    # EJERCICIO PROPUESTO: el automóvil ahora recibe es_automatico
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250,
                      TipoColor.NEGRO, True)
    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    print("Velocidad actual =", auto1.get_velocidad_actual())
    auto1.acelerar(20)
    print("Velocidad actual =", auto1.get_velocidad_actual())
    auto1.desacelerar(50)
    print("Velocidad actual =", auto1.get_velocidad_actual())
    auto1.frenar()
    print("Velocidad actual =", auto1.get_velocidad_actual())
    auto1.desacelerar(20)
    # EJERCICIO PROPUESTO: probar las multas intentando superar la velocidad máxima
    auto1.acelerar(300)
    auto1.acelerar(300)
    print("Tiene multas =", auto1.tiene_multas())
    print("Total de multas =", auto1.calcular_total_multas())