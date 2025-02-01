"""
-- Tutarras
Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
"""
mult3 = 0
mult5 = 0

for x in range(10):
    num = int(input('Ingresar número: '))

    # multiplos de 3
    if num % 3 == 0:
        mult3 += 1
    
    # multiplos de 5
    if num % 5 == 0:
        mult5 += 1
    
print('La cantidad de múltiplos de 3 son ', mult3)
print('La cantidad de múltiplos de 5 son ', mult5)