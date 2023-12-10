class Estudiante:
    def __init__(self, nombre, apellido, edad, sexo, direccion, carrera, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.carrera = carrera
        self.email = email
        self.telefono = telefono
    

nombre = input("Nombre: ")
apellido = input("Apellido: ")
direccion = input("Direccion: ")
edad = input("Edad: ")
sexo = input("Sexo: ")
carrera = input("Carrera: ")
email = input("Email: ")
telefono = input("Telefono: ")

est = Estudiante(nombre=nombre, apellido=apellido, edad=edad, sexo=sexo, direccion=direccion, carrera=carrera, email=email, telefono=telefono )


print("\nDatos ingresados:")
print(f"Nombre: {est.nombre}")
print(f"Apellido: {est.apellido}")
print(f"Edad: {est.edad}")
print(f"Sexo: {est.sexo}")
print(f"Dirección: {est.direccion}")
print(f"Carrera: {est.carrera}")
print(f"Email: {est.email}")
print(f"Telefono: {est.telefono}")
