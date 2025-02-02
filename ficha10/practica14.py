"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
"""
def calcular_perimetro(lado):
    perimetro = lado * 4
    return perimetro

# bloque principal
lado = int(input('Ingresar lado del cuadrado: '))
per = calcular_perimetro(lado)
print('El perimetro del cuadrado es ', per)