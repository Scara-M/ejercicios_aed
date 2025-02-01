"""
--Secuencia de impares--
Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en
forma ascendente y descendente.
"""
num1 = int(input('Ingresar primer número: '))
num2 = int(input('Ingresar segundo número: '))

if num1 % 2 == 0:
    for x in range(num1 + 1, num2, 2):
        print(x)
    for x in range(num2 - 1, num1, -2):
        print(x)
else:
    for x in range(num1, num2, 2):
        print(x)
    for x in range(num2 + 1, num1, -2):
        print(x)