"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""
lista = []

# carga de elementos
for x in range(5):
    num = int(input('Ingresar un número: '))
    lista.append(num)

# identificar el mayor
mayor = lista[0]
for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]

# identificar si se repite el numero
pos = 0
for x in range(1,5):
    if mayor == lista[x]:
        pos = x

# salida por pantalla
print('El mayor de la lista es ', mayor)
print('El mayor se repite en la posicion ', pos)