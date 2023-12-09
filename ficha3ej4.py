"""
--Control electoral--
Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato:
apellido, nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
cantidad de votos entre paréntesis, y debajo una línea con tantas "x" como votos obtenidos (por ejemplo, el
candidato obtuvo 4 votos, deberá aparecer una línea como esta: "xxxx" con cuatro letras "x") (Asumimos que en
el centro vecinal no hay demasiados electores, de forma que podamos estar seguros que no habrá miles o millones
de votos... sólo unos pocos para darle sentido al enunciado).
"""

# carga por teclado
apellido = input('Ingresar el apellido del candidato: ')
nombre = input('Ingresar el nombre del candidato: ')
votos = int(input('Ingresar la cantidad de votos obtenidos: '))

# Salida por pantalla
print(nombre[0] + apellido[0])
print('Cantidad de votos: ', votos)
print('x' * votos)