"""
--Operaciones de orden con 3 nros.--
Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es el resto de la
división de los dos primeros.
"""
# carga de números
num1 = int(input('Ingresar primer número: '))
num2 = int(input('Ingresar segundo número: '))
num3 = int(input('Ingresar tercer número: '))


# Ordenar de mayor a menor
if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2

elif num2 > num3:
    mayor = num2
    if num1 > num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1

else:
    mayor = num3
    if num1 > num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1

print('-' * 5)
# determinar si el tercero es el resto de la division de los dos primeros
if (num1 % num2) == num3:
    print('El tercero número es el resto de los dos primeros')

print('LOS NÚMEROS ORDENADOS DE MAYOR A MENOR SON')
print(mayor)
print(medio)
print(menor)