"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
"""
# carga por teclado
n = int(input('Ingrese la cantidad de enteros a procesar: '))
pares = impares = 0
x = 0

# determinar pares e impares
while x < n:
    num = int(input('Ingrese número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    x += 1

# salida por pantalla
print('La cantidad de valores pares son: ', pares)
print('La cantidad de valores impares son: ', impares)