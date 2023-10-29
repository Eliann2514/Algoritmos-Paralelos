numero =1
sueldo =0
total =0

while numero <=12:
    sueldo =int(input("Entre sueldo:"))
    total = total + sueldo / 12
    numero = numero +1
print("Total de sueldos:", total)