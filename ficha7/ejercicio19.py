"""
-- Tutarras
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
"""
suma = 0

for x in range(10):
    num = int(input('Ingrese un número: '))

    # sumar los últimos 5 valores ingresados
    if x > 4:
        suma += num

# salida
print('La suma de los últimos 5 valores ingresados es ', suma)