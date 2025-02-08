"""
Definir por asignación una lista con 8 elementos enteros. 
Contar cuantos de dichos valores almacenan un valor superior a 100.
"""
lista = [101,5,9,250,600,45,13,160]
cant = 0

for x in range(len(lista)):
    if lista[x] > 100:
        cant += 1

# salida
print('La cantidad de elementos mayores a 100 son ', cant)