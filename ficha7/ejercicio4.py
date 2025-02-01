"""
--Decimal a Hexadecimal--
Generar n numeros aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y generar el numero
hexadecimal
"""
import random

n = int(input('Ingresar la cantidad de números a procesar: '))

for x in range(n):
    num = random.randint(5000, 450000)
    hexadecimal = num // 16
    print(num)
    print(hexadecimal)
    print('-' * 45)