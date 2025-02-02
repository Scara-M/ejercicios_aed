"""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
"""
def contar_letras(cadena):
    cont = len(cadena)
    return cont

def contar_mayor(x1,x2):
    if x1 > x2:
        mayor = x1
    else:
        mayor = x2
    return mayor

# bloque principal
text1 = input('Ingrese una palabra: ')
cant1 = contar_letras(text1)
text2 = input('Ingrese una palabra: ')
cant2 = contar_letras(text2)
may = contar_mayor(cant1,cant2)
print('El que tiene más caracteres es ', may)
