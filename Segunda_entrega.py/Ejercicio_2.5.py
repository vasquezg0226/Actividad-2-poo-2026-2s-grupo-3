from enum import Enum


class Tipo(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta,
                 tipo_cuenta, porcentaje_interes):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0
        # EJERCICIO PROPUESTO: nuevo atributo porcentaje de interés mensual
        self.porcentaje_interes = porcentaje_interes

    def imprimir(self):
        print("Nombres del titular =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.name)
        print("Saldo =", self.saldo)
        # EJERCICIO PROPUESTO: imprimir el nuevo atributo
        print("Interés mensual (%) =", self.porcentaje_interes)

    def consultar_saldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Se ha consignado $" + str(valor) + " en la cuenta. El nuevo saldo es $" + str(self.saldo))
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Se ha retirado $" + str(valor) + " en la cuenta. El nuevo saldo es $" + str(self.saldo))
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

    # EJERCICIO PROPUESTO: calcular y aplicar el interés mensual al saldo
    def aplicar_interes(self):
        self.saldo = self.saldo + self.saldo * self.porcentaje_interes / 100
        return self.saldo


if __name__ == "__main__":
    # EJERCICIO PROPUESTO: la cuenta ahora recibe el porcentaje de interés mensual
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, Tipo.AHORROS, 1.5)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    # EJERCICIO PROPUESTO: probar el cálculo del nuevo saldo con interés
    print("Saldo con interés =", cuenta.aplicar_interes())
    