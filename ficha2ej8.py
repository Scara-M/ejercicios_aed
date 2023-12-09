"""
-- Datos de un rectángulo --
Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro y la
superficie del mismo.
"""

# carga por teclado
ancho = int(input('Ingresar el ancho del rectángulo: '))
alto = int(input('Ingresar el alto del rectángulo: '))

# determinar el perimetro y la superficie
perimetro = ancho * 2 + alto * 2
superficie = ancho * alto

# Salida
print('El perímetro del rectángulo es de: ', perimetro)
print('La superficie del rectángulo es de: ', superficie)