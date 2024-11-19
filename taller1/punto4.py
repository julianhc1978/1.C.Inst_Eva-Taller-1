class VehiculoCarreras:
    def __init__(self,marca,modelo,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad_maxima

    def mostrar_info(self):
        return f"-el vehiculo:{self.marca} modelo: {self.modelo} velocidad:{self.velocidad}km/h"

class Cochef1(VehiculoCarreras):
    def __init__(self,marca,modelo,velocidad_maxima,tipo_neumaticos):
        super().__init__(marca,modelo,velocidad_maxima)
        self.tipo_neumatica = tipo_neumaticos

class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

class CocheNascar(VehiculoCarreras):
    def __init__(self,marca, modelo, velocidad_maxima, revoluciones):
        super().__init__(marca, modelo, velocidad_maxima)
        self.revoluciones = revoluciones

formula1 = Cochef1("monster", 2024, 350,"lisos")
moto1 = MotoGP("redbull", 2023,300,4500)
nascar = CocheNascar("chevrolet", 2020, 290,3500)

print(formula1.mostrar_info())
print(moto1.mostrar_info())
print(nascar.mostrar_info())