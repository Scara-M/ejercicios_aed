"""
--Analisis de palabra--
Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular los siguientes
puntos:
Determinar la cantidad de letras que tiene la palabra.
Mostrar un mensaje que informe si la palabra termina en vocal.
"""

# carga de palabra
palabra = input('Ingrese la palabra a analizar: ').lower()


# cantidad de letras de la palabra
cant = len(palabra)

# determinar si termina en vocal
if palabra[-1] == 'a' or palabra[-1] == 'e' or palabra[-1] == 'i' or palabra[-1] == 'o' or palabra[-1] == 'u':
    print('La palabra termina en vocal')
else:
    print('La palabra no termina en vocal')

print('La palabra tiene ', cant, ' letras')