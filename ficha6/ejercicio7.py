"""
--Números pares e impares--
Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se
presenta cuando el usuario ingrese un número negativo.

Los requerimientos funcionales del programa son:
a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
b) Cantidad de valores pares ingresados.
c) Cantidad de valores impares ingresados.
d) Informar si en la carga de números se ingreso al menos un número 0.
e) Informar si la serie contiene solo números pares e impares alternados
"""
# Inicializacion de variables
acum50_100 = 0
cant_pares = cant_impares = 0
num_cero = False
anterior = -1
alternan = True

num = int(input('Ingrese un número (finaliza con valor negativo): '))
while num >= 0:
    # La sumatoria de solo los números que estén comprendidos entre 50 y 100.
    if num >= 50 and num <= 100:
        acum50_100 += num

    # Cantidad de valores pares ingresados.
    paridad = num % 2
    if paridad == 0:
        cant_pares += 1
    
    # Cantidad de valores impares ingresados.
    if paridad != 0:
        cant_impares += 1
    
    # Informar si en la carga de números se ingreso al menos un número 0.
    if num == 0:
        num_cero = True
    
    # Informar si la serie contiene solo números pares e impares alternados
    if anterior == paridad:
        alternan = False
    anterior = paridad

    num = int(input('Ingrese otro número (finaliza con valor negativo): '))

print(" ")
print('La sumatoria de los números entre 50 y 100 es ', acum50_100)
print('La cantidad de pares ingresados es ', cant_pares)
print('La cantidad de impares es ', cant_impares)

if num_cero:
    print('Se ingresó el cero')
else: 
    print('No se ingresó el cero')

if alternan:
    print('Alternan la serie de valores ingresados')
else:
    print('No alternan la serie de valores ingresados')