"""
--Suma - División - Potencia--
Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10
dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
"""

# carga de numeros por teclado
num1 = int(input('Ingresar primer número: '))
num2 = int(input('Ingresar segundo número: '))
num3 = int(input('Ingresar tercer número: '))


# Proceso
suma = num1 + num2 + num3
if suma > 10:
    resultado = suma//2
else:
    resultado = suma ** 3


# Salida por pantalla
print('La suma de los números es ', suma)
print('El resultado de la operación es ', resultado)