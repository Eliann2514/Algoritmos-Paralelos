carrera=["ISC","INF"]
nombre=input("Carrera Seleccionada:")
if nombre.upper() in carrera:
  print("Carrera Disponible")
else:
  print("Carrera no disponible en este recinto")