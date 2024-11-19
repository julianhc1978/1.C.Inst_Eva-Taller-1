class ProductoElectronico:
    def __init__(self,nombre,precio_dolares,marca):
        self.nombre = nombre
        self.precio = precio_dolares
        self.marca = marca

    def mostrar(self):
        return f"nombre del producto:{self.nombre}, precio: {self.precio}, marca: {self.marca}"

class TelefonoMovil(ProductoElectronico):
    def __init__(self,nombre,precio_dolares,marca,capacida_bateria_mah):
        super().__init__(nombre, precio_dolares, marca)
        self.capacidad = capacida_bateria_mah

class Laptop(ProductoElectronico):
    def __init__(self,nombre,precio_dolares,marca,tamano_pantalla_pulgadas):
        super().__init__(nombre,precio_dolares,marca)
        self.pantalla = tamano_pantalla_pulgadas

telefono1 = TelefonoMovil("j2",400,"samsung",300)
laptop1 = Laptop("super",3000,"linux",10)

print(telefono1.mostrar())
print(laptop1.mostrar())