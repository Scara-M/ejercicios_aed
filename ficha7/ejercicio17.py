"""
-- Tutarras
Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)
"""
cont = 0
n = int(input('Ingrese la cantidad de enteros a procesar: '))

# proceso
for x in range(n):
    num = int(input('Ingrese un número: '))
    
    # contar valores >= 1000
    if num >= 1000:
        cont += 1

print('La cantidad de valores mayores o iguales a 1000 son: ', cont)