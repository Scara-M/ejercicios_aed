"""
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
"""
lista = [10, 7, 3, 7, 2]
suma = 0
x = 0

# ciclo
while x < len(lista):
    suma += lista[x]
    x += 1

# salida por pantalla
print('La suma de los valores de la lista son: ', suma)