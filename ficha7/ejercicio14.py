"""
--Tutarras
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
"""
suma = 0
for num in range(10):
    num = int(input('Ingrese un número: '))
    suma += num

# determina el promedio
promedio = suma/10

# salida 
print('La suma de los valores ingresados es ', suma)
print('El promedio de los valores ingresados es ', promedio)