class Mascota:
    def __init__(self,nombre,edad,especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar(self):
        return f"--nombre: {self.nombre}, edad: {self.edad}, especie: {self.especie}"

class Perro(Mascota):
    def __init__(self,nombre,edad,especie,raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def ladrar(self):
        return f"¡GUAU, GUAU!"

class Gato(Mascota):
    def __init__(self,nombre,edad,especie,color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def maullar(self):
        return f"¡MIAU!"

perro1 = Perro("pecas",7,"perro","pitbull")
print(perro1.mostrar())
print(perro1.ladrar())

gato1 = Gato("luna",3,"gato","negro")
print(gato1.mostrar())
print(gato1.maullar())