"""
--Busqueda de mayor--
Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de [0,
100.000].
"""
import random

mayor = 0
x = 0
while x < 10000:
    num = random.randint(0, 100000)
    if num > mayor:
        mayor = num
    x += 1
    
print('El mayor de los números es ', mayor)