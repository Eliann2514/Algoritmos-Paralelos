class Persona:
    def __init__(self, nombre, apellido, edad, sexo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
    

nombre = input("Nombre: ")
apellido = input("Apellido: ")
direccion = input("Direccion: ")
edad = input("Edad: ")
sexo = input("Sexo: ")


per = Persona(nombre=nombre, apellido=apellido, edad=edad, sexo=sexo, direccion=direccion)


print("\nDatos ingresados:")
print(f"Nombre: {per.nombre}")
print(f"Apellido: {per.apellido}")
print(f"Edad: {per.edad}")
print(f"Sexo: {per.sexo}")
print(f"Dirección: {per.direccion}")

        
