"""
--Ecuación de Einstein--
La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:
E = mc^2
Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg. Desarrolle un programa que lea el valor una
masa m en kilogramos y obtenga la cantidad de energía E producida en la conversión.
"""

# datos
c = 299792.458
m = int(input('Ingresar la masa en kg: '))

# ecuacion
e = m * (c ** 2)

# salida
print('La cantidad de energía obtenida es de: ', e)