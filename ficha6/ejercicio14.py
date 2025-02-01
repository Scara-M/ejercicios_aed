"""
--Tutarras
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
"""
suma = 0
x = 0
while x < 10:
    num = int(input('Ingrese un número: '))
    suma += num
    x += 1

prom = suma // 10

# salida por pantalla
print('La suma de los valores ingresados es ', suma)
print('El promedio entre los valores ingresados es: ', prom)