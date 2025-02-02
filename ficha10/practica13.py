"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
"""
def calcular_promedio(x1,x2,x3):
    prom = (x1 + x2 + x3)//3
    return prom

# bloque principal
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))
promedio = calcular_promedio(num1,num2,num3)
print('El promedio de los números es ', promedio)