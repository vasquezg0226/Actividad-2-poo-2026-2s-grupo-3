class Persona:
    def __init__(self, nombre, apellidos, numero_documento_identidad,
                 anio_nacimiento, pais_nacimiento, genero):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anio_nacimiento = anio_nacimiento
        # EJERCICIO PROPUESTO: nuevos atributos en el constructor
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.numero_documento_identidad)
        print("Año de nacimiento =", self.anio_nacimiento)
        # EJERCICIO PROPUESTO: imprimir los nuevos atributos
        print("País de nacimiento =", self.pais_nacimiento)
        print("Género =", self.genero)
        print()


if __name__ == "__main__":
    # EJERCICIO PROPUESTO: los objetos ahora reciben país y género
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998, "Colombia", "H")
    p2 = Persona("Luis", "León", "1053223344", 2001, "Colombia", "H")
    p1.imprimir()
    p2.imprimir()