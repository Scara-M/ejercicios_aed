"""
--Números Enteros--
Escribir un programa que permita leer la cantidad de números enteros ingresados por el usuario y calcular lo
siguiente:
a) El segundo menor
b) El promedio de los números positivos.
c) El mayor de los números negativos.
"""
# declaración de variables
cant_pos = 0
acum_pos = 0
mayor_neg = None

n = int(input('Ingresar la cantidad de números a procesar: '))
print('-'*15)

for i in range(n):
    num = int(input('Ingresar número: '))
    
    # guarda el primer numero como menor
    if i == 0:
        menor = num

    # compara el numero con el menor
    elif i == 1:
        if num < menor:
            menor = num
            menor2 = menor
        else:
            menor2 = num
    else:
        if num < menor:
            menor = num
            menor2 = menor

        elif num < menor2:
            menor2 = num
    
    # El promedio de los números positivos
    if num >= 0:
        cant_pos += 1
        acum_pos += 1

    # el mayor de los negativos
    if num < 0:
        if mayor_neg is None or num < mayor_neg:
            mayor_neg = num

# Salida por pantalla
print('El segundo menor ingresado es: ', menor2)
if cant_pos != 0:
    promedio = acum_pos/cant_pos
else:
    promedio = 0
print('El promedio de los números positivos es: ', promedio)
print('El mayor de los números negativos es ', mayor_neg)
