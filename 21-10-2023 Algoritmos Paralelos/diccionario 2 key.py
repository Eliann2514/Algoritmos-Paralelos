
d2 = dict([
('Nombre', 'sara'),
('edad', 27),
('documeno', 1003882),

])
print(d2)

mi_d1 = {
'nombre' : 'juan',
'edad' : 25,
'cuidad' : 'madrid'


}
print(mi_d1.items())

mi_d2 = {'a':1, 'b':2, 'c':3}
claves = mi_d2.keys()
print(claves)

mi_d3 = {'a':1, 'b':2, 'c':3}
valores = mi_d3.values() 
print(valores)

mi_d4 = {'a':1, 'b':2, 'c':3}
valores = mi_d4.pop('b') 
print(valores)
print(mi_d4)

mi_d5 = {'a':1, 'b':2, 'c':3}
par_eliminad = mi_d5.popitem()
print(par_eliminad)
print(mi_d5)

