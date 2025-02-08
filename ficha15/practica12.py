"""
Crear y cargar una lista con 5 enteros. 
Implementar un algoritmo que identifique el mayor valor de la lista.
"""

lista = []

# carga de elementos
for x in range(5):
    num = int(input('Ingrese un número: '))
    lista.append(num)

# identificar el mayor
mayor = lista[0]
pos_mayor = 0
for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]
        pos_mayor = x

# idenficar el menor
menor = lista[0]
pos_menor = 0
for x in range(1,5):
    if lista[x] < menor:
        menor = lista[x]
        pos_menor = x

# salida por pantalla
print('El mayor de la lista es ', mayor, ' en la posicion ', pos_mayor)
print('El menor de la lista es ', menor, ' en la posicion ', pos_menor)