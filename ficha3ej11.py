"""
--Palabra enmascarada--
Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la
primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos.

Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
"""
# cargar palabra
palabra = input('Ingresar palabra: ')

# enmascarar palabra
primera = palabra[0]
ultima = palabra[-1]
cant = len(palabra) - 2

# Salida por pantalla
print(primera + cant * '*' + ultima)