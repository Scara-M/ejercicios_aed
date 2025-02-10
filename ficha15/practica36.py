"""
Solicitar por teclado dos enteros. 
El primer valor indica la cantidad de elementos que crearemos en la lista. 
El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.

Por ejemplo si el operador carga un 2 y un 4 significa que debemos crear una lista similar a:
lista=[[1,1,1,1], [1,1,1,1]]
"""
lista = []

# entrada por teclado
elem = int(input('Indicar la cantidad de elementos que contendrá la lista: '))
sub = int(input('Indicar la cantidad de elementos que tendrá cada lista interna: '))

for k in range(elem):
    # se carga una lista vacia
    lista.append([])
    for x in range(sub):
        valor = int(input('Ingrese valor: '))
        lista[k].append(valor)

print(lista)

# suma de elementos
suma = 0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma += lista[k][x]
print('La suma de los elementos es ', suma)