"""
--Cuadrados y cubos--
Leer dos números y calcular:
La suma de sus cuadrados.
El promedio de sus cubos.
"""

# datos de entrada
a = int(input('Ingresar primer número: '))
b = int(input('Ingresar segundo número: '))

# suma de sus cuadrados
suma =  a ** 2 + b ** 2

# promedio de cubos
promedio = (a ** 3 + b ** 3 )/2

# Salida
print('La suma de sus cuadrados es: ', suma)
print('El promedio de sus cubos es: ', promedio)
