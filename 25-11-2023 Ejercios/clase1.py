class Alumno:
    #contenido de la clase.
    nombre =""
    apellido =""
    def NombreCompleto(self):
        return self.nombre + " "+ self.apellido
    
alu = Alumno()
alu.nombre = input("Nombre..:")
alu.apellido = input("Apellido..:")

print(alu.NombreCompleto())