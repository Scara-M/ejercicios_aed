"""
--Menores y promedio--
Realizar un programa que genere 5000 numeros aleatorios en el rango de [0, 100000] y que permita:
Determinar el menor de los numeros generados en forma aleatoria
Calcular el valor promedio de los números menores a 10.000.
"""
import random

menor = 100000
cont = acum = 0

x = 0
while x < 5000:
    num = random.randint(0, 100000)

    if num < menor:
        menor = num
    
    if num < 10000:
        cont += 1
        acum += num
    x += 1

if cont != 0:
    prom = acum / cont
else:
    prom = 0

prom_redond = round(prom, 2)
# Salida por pantalla
print('El menor de los números generados es ', menor)
print('El promedio de los valores menores a 10000 es ', prom_redond)