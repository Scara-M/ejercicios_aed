"""
 -- Análisis de texto
El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero.
La frase finaliza con un punto, y las palabras están separadas por espacios unicamente. Se debe mostrar:
• Ver el porcentaje de vocales respecto del total de letras de la frase
• La longitud promedio de las palabras
• La Palabra mas larga del texto
• Cantudad de palabras que comienzan con “ta”
"""

# Inicio de variables
vocales = 'aeiouáéíóú'
abecedario = 'abcdefghijklmnopqrstuvwxyzáéíóú'
texto = ''
cv = cp = cl = ctl = may = cpTA = 0
hayT = hayTa = False

# Validación de que el texto no este vacío

while len(texto) <= 0:
    texto = input('Ingrese el texto a analizar: ')
    if len(texto) <= 0:
        texto = input('Ingrese el texto a analizar: ')


# comienza con el procesamiento del texto
for car in texto:

    if car in abecedario:
        # recorriendo la palabra
        cl += 1

        # pregunta si la letra es una vocal
        if car in vocales:
            cv += 1

        # si es el primer caracter y tambien si es igual a t
        if cl == 1 and car == 't':
            hayT = True
        else:
            # pregunta si el primer caracter era T y el actual es A
            if hayT and car == 'a':
                hayTa = True
            hayT = False

    # Si es un espacio o punto
    elif car == ' ' or car == '.':
    # si la cantidad de letras es mayor a cero
        if cl > 0:
            cp += 1

            # incrementa el acumulador de letras de la frase en la cantidad de letras de la palabra
            ctl += cl

            # busca la palabra de mayor longitud
            if cl > may:
                # si encuentra un mayor, almacena la longitud de la palabra
                may = cl

        # si encontro la silaba TA
        if hayTa:
            cpTA += 1
            # limpieza de variables
            hayTa = False
        cl = 0

# calculo del porcentaje
if ctl != 0:
    porc = round(cv * 100 / ctl, 2)
else:
    porc = 0

# calculo del promedio
if cp != 0:
    prom = ctl // cp
else:
    prom = 0

# Muestra de resultados
print('El porcentaje de vocales respecto del total de letras es', porc, '%')
print('Hay ', prom, ' letras por palabras')
print('La palabra más larga del texto tiene', may, 'letras')
print('Hay', cpTA, ' palabras que comienzan con \"ta\"')