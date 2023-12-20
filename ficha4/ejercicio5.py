"""
--Tarjeta de Bingo--
Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaria la
tarjeta de bingo de una persona. Una vez generados los números aleatorios solicitar al usuario que ingrese 3
números enteros y a partir de alli mostrar los siguientes mensajes:
Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó ninguna
casilla"
Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".
"""
import random

print('BILLETE GENERADO')
billete = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),\
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),\
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

# Carga de los tres enteros
num1 = int(input('Ingresar un número entero: '))
num2 = int(input('Ingresar un número entero: '))
num3 = int(input('Ingresar un número entero: '))

# vericar si coincidio alguno
print(billete)
if num1 in billete or num2 in billete or num3 in billete:
    print('El usuario marcó alguno')
else:
    print('El usuario no marcó ninguno')