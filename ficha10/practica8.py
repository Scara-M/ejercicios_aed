"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos.
"""

def contar_vocales(cadena):
    cont = 0
    for x in range(len(cadena)):
        if cadena[x] == 'a' or cadena[x] == 'e' or cadena[x] == 'i' or cadena[x] == 'o' or cadena[x] == 'u':
            cont += 1
    print('La cantidad de vocales son ', cont)

contar_vocales('hola')
contar_vocales('adioss')
contar_vocales('otorrinolaringologo')

