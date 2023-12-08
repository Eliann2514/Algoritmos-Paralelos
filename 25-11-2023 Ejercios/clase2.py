class Alumno:
    def NombreCompleto(self,nombre,apellido):
        return nombre +" "+ apellido

alu=Alumno()
nombre = input("Nombre..:")
apellido = input("Apellido..:")

print(alu.NombreCompleto(nombre,apellido))
        