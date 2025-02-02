"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.
"""
def calcular_suma(x1,x2,x3=0,x4 = 0, x5 = 0):
    suma = x1 + x2 + x3 + x4 + x5
    return suma

# bloque principal
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))
suma = calcular_suma(num1,num2,num3)
print('La suma de los valores es ', suma)
num4 = int(input('Ingrese un número: '))
suma = calcular_suma(num1,num2,num3,num4)
print('La suma de los valores es ', suma)