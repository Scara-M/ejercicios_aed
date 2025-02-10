"""
Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.
"""
lista=[[1,1,1,1,1], [2,2,2,2,2]]
suma1 = suma2 = 0

# recorre lista 1
for x in range(len(lista[0])):
    suma1 += lista[0][x]
print(suma1)

# # recorre lista 2
for x in range(len(lista[1])):
    suma2 += lista[1][x]
print(suma2)