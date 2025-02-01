"""
-- programacion Ya
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""
# inicializador de variables
negativos = positivos = mult15 = 0
pares = 0

for x in range(10):
    num = int(input('Ingrese un número: '))

    # cantidad de positivos
    if num > 0:
        positivos += 1
    
    # cantidad de negativos
    if num < 0:
        negativos += 1
    
    # multiplos de 15
    if num % 15 == 0:
        mult15 += 1
    
    # valor acumulado que son pares
    if num % 2 == 0:
        pares += num

# salida por pantalla
print('La cantidad de valores positivos ', positivos)
print('La cantidad de valores negativos es ', negativos)
print('La cantidad de múltiplos de 15 son ', mult15)
print('El valor acumulado de pares es ', pares)