"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
Mostrar esta tercer lista.
"""
lista1 = []
lista2 = []
sumas = []

# carga de elementos
for x in range(4):
    num1 = int(input('Ingresar numero de la lista 1: '))
    lista1.append(num1)
    num2 = int(input('Ingresar numero de la lista 2: '))
    lista2.append(num2)

# sumar las listas
for x in range(4):
    suma = lista1[x] + lista2[x]
    sumas.append(suma)

print('La suma de las dos lista es ', sumas)