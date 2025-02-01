"""
-- Promedio de números aleatorios--
Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0,
100000]
"""
import random

acum = 0
x = 0
while x < 1000:
    num = random.randint(0, 100000)
    acum += num
    x += 1

prom = acum / x
print('El promedio de los números generados es ', prom)