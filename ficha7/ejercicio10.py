"""
10 - Caracteres: promedio de letras
Cargar por teclado una frase (de a un caracter por vez). La carga solo debe terminar cuando se
ingrese un punto (el cual no forma parte de la frase a procesar).
Se debe informar la cantidad de palabras de la frase y cantidad promedio de letras por palabra.
Por ejemplo, la frase “Este es un ejercicio muy sencillo.” tiene 6 palabras y la cantidad promedio
de letras por palabra es de 4,66 ( (4+2+2+9+3+8)/ 6).
"""

# inicialización de variables
abecedario = 'abcdefghijklmnopqrstuvwxyzáéíóú'
frase = ''
cletras = 0
cpalabras = 0
ctotalletras = 0

# validación de que se carga una palabra
while len(frase) <= 0:
    frase = input('Ingresar frase a procesar: ').lower()
    if len(frase) <= 0:
        frase = input('Ingresar frase a procesar: ').lower()

# procesamiento de la palabra
for car in frase:
    if car in abecedario:
        # analiza letras
        cletras += 1

    elif car == '' or car == '.':
        # analiza palabras
        if cletras > 0:
            cpalabras += 1
            ctotalletras += cletras
        cletras = 0

# Muestra de resultados
print('La cantidad de palabras de la frase son ', ctotalletras)
print(cpalabras)