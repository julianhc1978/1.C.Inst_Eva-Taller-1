class TransportePublico:
    def __init__(self,tipo,capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar(self):
        return f"--tipo de transporte: {self.tipo}, capacidad: {self.capacidad}"

class Autobus(TransportePublico):
    def __init__(self,tipo,capacidad,nombre_ruta):
        super().__init__(tipo, capacidad)
        self.nombre_ruta = nombre_ruta

class Tren(TransportePublico):
    def __init__(self,tipo,capacidad,numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

autobus1 = Autobus("autobus",30,"envigago-poblado")
tren1 = Tren("tren",200,6)

print(autobus1.mostrar())
print(tren1.mostrar())