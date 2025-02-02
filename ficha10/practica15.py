"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados.
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.
"""
def calcular_superficie(lado1,lado2):
    superficie = lado1 * lado2
    return superficie

# bloque principal
print('Superficie 1')
la1 = int(input('Ingrese lado 1: '))
la2 = int(input('Ingrese lado 2: '))
sup1 = calcular_superficie(la1,la2)
print('Superficie 2')
la3 = int(input('Ingrese lado 1: '))
la4 = int(input('Ingrese lado 2: '))
sup2 = calcular_superficie(la3,la4)

# determinar mayor
if sup1 > sup2:
    print('El primer triángulo tiene una superficie mayor')
else:
    print('El segunddo triángulo tiene un superficie mayor')