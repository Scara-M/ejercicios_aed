"""
Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
"""
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimir lista completa
print(lista)

# primer componente
print(lista[0])

# primer componente de la primera lista de la principal
print(lista[0][0])

# los elementos de la primera lista
for x in range(len(lista[0])):
    print(lista[0][x])

# cada elemento de las listas
print()
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])