"""
--Números: Mayor y Menor--
Cargar por teclado n números enteros positivos, uno a uno. 
Se deberá establecer qué número es el mayor de los números pares y el menor de los números impares.
Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0; el mayor de los pares sería el número 18 y el
menor de los impares el número 9.
"""
mayor_par = None
menor_impar = None

n = int(input('Ingresar el número de enteros a cargar: '))

for i in range(n):
    num = int(input('Ingresar entero: '))

    if num % 2 == 0:
        if mayor_par is None or num > mayor_par:
            mayor_par = num
    else:
        if menor_impar is None or num < menor_impar:
            menor_impar = num


# Salida por pantalla
print('El mayor de los pares es ', mayor_par)
print('El menor de los impares es ', menor_impar)