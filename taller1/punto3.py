import math

class Figura_3D:
    def volumen_cub(self,lado):
        volumen = lado**3
        return f"el volumen del cubo es {volumen} "

    def volumen_esfera(self,radio):
        volumen = (4 / 3) * math.pi * radio ** 3
        return f"el volumen de la esfera es {volumen}"

class Cubo(Figura_3D):
    def __init__(self,lado):
        self.lado = lado

class Esfera(Figura_3D):
    def __init__(self, radio):
        self.radio = radio

esfera = Esfera(35)
cubo = Cubo(12)

print(cubo.volumen_cub(cubo.lado))
print(esfera.volumen_esfera(esfera.radio))