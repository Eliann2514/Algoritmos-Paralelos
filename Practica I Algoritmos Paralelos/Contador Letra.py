palabras = ("manzana", "cascada", "camisa", "analisis", "prueba")
contador_a = 0
for palabra in palabras:
    contador_a += palabra.count('a')
    print("Numero de veces que aparece 'a':", contador_a)
