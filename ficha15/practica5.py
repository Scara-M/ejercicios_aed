"""
Definir una lista por asignación con 5 enteros. 
Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
"""
lista=[8,1,9,2,10]

for x in range(len(lista)):
    if lista[x] > 7:
        print(lista[x])