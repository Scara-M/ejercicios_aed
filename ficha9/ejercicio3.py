"""
3 - Inicio con sílaba ’pa’
Desarrollar un programa en Python que permita cargar por teclado un texto. Siempre se supone
que usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está
separada de las demás por un espacio en blanco. El programa debe determinar:
• La cantidad de palabras que comienzan con la expresión “pa” y termina con la letra “n”.
• La cantidad de palabras que presentan más de dos vocales a partir de la tercera letra de la
palabra.

• El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad
de total de palabras del texto.
• Cantidad de palabras de más de 5 letras.
"""


def es_vocal(car):
    vocales = 'aeiouáéíóú'
    return car in vocales


def calcular_porcentaje(cant, total):
    porc = 0
    if total > 0:
        porc = round(cant * 100 / total, 2)
    return porc


# programa principal
def principal():
    # inicialización de variables
    hay_pa = False
    cont_letras = 0
    anterior = None
    cant_pa_n = 0
    cant_vocal = 0
    cant_pal_2voc = 0
    cant5 = 0
    cont_pal = 0
    tiene5 = False

    # carga de texto
    texto = input('Ingrese su texto: ').lower()
    for car in texto:
        if car == ' ' or car == '.':
            if cont_letras > 0:
                # contador de palabras
                cont_pal += 1
                # cantidad de palabras comienzan con pa y terminan con n
                if hay_pa and anterior == 'n':
                    cant_pa_n += 1

                # cantidad de palabras que tienen más de 2 vocales a partir de la tercera letra
                if cant_vocal > 2:
                    cant_pal_2voc += 1

                # cantidad de palabras con más de cinco letras
                if tiene5:
                    cant5 += 1

            tiene5 = False
            hay_pa = False
            cont_letras = 0
            cant_vocal = 0
        else:
            cont_letras += 1

            # determinación expresion pa
            if anterior == 'p' and car == 'a':
                hay_pa = True

            # cantidad de vocales después de la tercera letra
            if cont_letras > 2:
                if es_vocal(car):
                    cant_vocal += 1

            # palabras con más de 5 letras
            if cont_letras > 5:
                tiene5 = True
        anterior = car

    # calcular porcentaje
    porcentaje = calcular_porcentaje(cant_pal_2voc, cont_pal)
    # Salida por pantalla
    print('La cantidad de palabras que comienzan con "pa" y terminan con "n" son: ', cant_pa_n)
    print('La cantidad de palabras que tienen más de 2 vocales a partir de la tercera letra son: ', cant_pal_2voc)
    print('El porcentaje de palabras que tienen más de 2 vocales a partir de la tercer letras es del % ', porcentaje)
    print('La cantidad de palabras con más de cinco letras son: ', cant5)

principal()
