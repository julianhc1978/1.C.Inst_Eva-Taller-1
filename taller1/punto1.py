class MaterialBiblioteca:
    def __init__(self,titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
        return f"--el material {self.titulo} escrito por {self.autor} ha sido prestado  --disponible: {self.disponible}"
    def devolver(self):
        if self.disponible:
            self.disponible = True
        return f"--el material {self.titulo} escrito por {self.autor} ha sido devuelto  --disponible: {self.disponible} "
    def mostrar(self):
        return f"-material: {self.titulo} -autor: {self.autor} -codigo: {self.codigo}"

class Libro(MaterialBiblioteca):
    def __init__(self,titulo, autor, codigo, numero_paginas, genero):
        super().__init__(titulo, autor, codigo)
        self.numero_paginas = numero_paginas
        self.genero = genero

class Revista(MaterialBiblioteca):
    def __init__(self,titulo, autor, codigo, numero_edicion, feha_publicacion):
        super().__init__(titulo, autor, codigo)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = feha_publicacion

class Periodicos(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, fecha_publicacion, editorial):
        super().__init__(titulo, autor, codigo)
        self.fecha_publicacion = fecha_publicacion
        self.editorial = editorial

libro1 = Libro("cien años de soledad", "gabriel garcia marquez", "001",100, "realismo" )
revista1= Revista("forbes", "john", "002", "202", 2002)
periodico1 = Periodicos("espectador", "juan ", "003", 1999,"planeta")

print(libro1.prestar())
print(libro1.devolver())
print(libro1.mostrar())

print(revista1.prestar())
print(revista1.devolver())
print(revista1.mostrar())

print(periodico1.prestar())
print(periodico1.mostrar())
print(periodico1.devolver())