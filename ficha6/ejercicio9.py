"""
-- Mayor numero en orden par--
Ingresar de a uno una serie de números. Encontrar e imprimir el mayor de todos los números pares cuyo número de
orden sea par, el proceso terminará cuando el número leído sea igual a cero
"""

# inicializador de variables
mayor = None

# proceso
num = int(input('Ingrese un número (Finalice con cero): '))
while num != 0:
    
    # determinar par
    if num % 2 == 0:
        ant = num
        # determinar mayor
        if mayor is None or ant > mayor:
            mayor = num
    num = int(input('Ingrese un número (Finalice con cero): '))

# salida por pantalla
print('-'*45)
print('El mayor de todos es ', mayor)
