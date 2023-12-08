"""
División con resto
Plantear un script (directamente en el shell de Python) que permita informar, para dos valores a y b el resultado de
la división a/b y el resto de esa divisón.
"""
# carga de valores
a = int(input('Ingresar el primer valor: '))
b = int(input('Ingresar el segundo valor: '))

# Determinacion del resto y division
cociente = a // b
resto = a % b

# resultado
print('El cociente de la operación es: ', cociente)
print('El resto de la división es: ', resto)