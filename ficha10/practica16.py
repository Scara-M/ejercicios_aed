"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
"""
def contar_letras(cadena):
    cant = 0
    for x in range(len(cadena)):
        if cadena[x] == 'a' or cadena[x] == 'A':
            cant += 1
    return cant

# bloque principal
palabra = input('Ingrese una palabra: ')
print('La cantidad de letras "a" que tiene la palabra es ', contar_letras(palabra))