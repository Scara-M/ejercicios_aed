"""
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.
"""
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print(lista)

# cambiar por cero los mayores a 50
for k in range(len(lista)):
    for x in range(len(lista[k])):
        if lista[k][x] > 50:
            lista[k][x] = 0
print(" ")
print(lista)