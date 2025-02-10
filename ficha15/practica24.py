"""
Cargar una lista con 5 elementos enteros. 
Ordenarla de menor a mayor y mostrarla por pantalla, 
luego ordenar de mayor a menor e imprimir nuevamente.
"""
lista = []

# cargar elementos
for x in range(5):
    num = int(input('Ingrese un número: '))
    lista.append(num)

# menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x] > lista[x+1]:
            lista[x],lista[x+1] = lista[x+1],lista[x]

# salida por pantalla
print(lista)

# mayor a menor
for k in range(4):
    for x in range(4-k):
        if lista[x] < lista[x+1]:
            lista[x],lista[x+1] = lista[x+1],lista[x]

# salida por pantalla
print(lista)