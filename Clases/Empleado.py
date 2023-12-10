class Empleado:
    def __init__(self, nombre="", apellidos="", edad=0, sexo="", direccion="", email="", sueldo=0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, sueldo):
        self.sueldo = sueldo

    def calcular_afp(self):
       
        return 0.1 * self.sueldo  
    def calcular_ars(self):
        return 0.05 * self.sueldo  
    def calcular_irs(self):
        return 0.15 * self.sueldo 
    def imprimir_informacion(self):
        print("Información de la Persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.calcular_afp()}")
        print(f"ARS: {self.calcular_ars()}")
        print(f"IRS: {self.calcular_irs()}")


empleado1 = Empleado(nombre="Elian", apellidos="Hernandez", edad=23, sexo="M", direccion="C/ Duarte",
                          email="eliahernandez@gmail.com", sueldo=2000000)

empleado1.asignar_sueldo(350000)

empleado1.imprimir_informacion()