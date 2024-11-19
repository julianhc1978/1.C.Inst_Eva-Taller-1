class EmpleadoHospital:
    def __init__(self,nombre,id,departamento,salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario = salario_base

    def mostrar_info(self):
        return (f"--empleado:{self.nombre} -id: {self.id} "
                f"-departamento:{self.departamento} -salario: {self.salario}")

class Medico(EmpleadoHospital):
    def __init__(self,nombre,id,departamento,salario_base,especialidad,num_pacientes):
        super().__init__(nombre,id,departamento,salario_base)
        self.especialidad = especialidad
        self.numero = num_pacientes

class Enfermero(EmpleadoHospital):
    def __init__(self,nombre, id,departamento,salario_base,turno,planta):
        super().__init__(nombre,id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

medico1 = Medico("juan", "001", "traumas",100000,"nuerocirujano", 25)
enfermero1 = Enfermero("carla", "002", "anestesia", 3000, "medio", "2")

print(medico1.mostrar_info())
print(enfermero1.mostrar_info())