"""
4 - Secuencia en rango
Desarrollar un programa de Python que permita cargar por teclado un secuencia de números, uno
por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga.
El cero no debe considerarse un dato a procesar. El programa debe:
• Determinar cuantos números se encuentran en el rango definido por 2 números p y q previamente ingresados (validar que los números que definen el rango son mayores a cero)
• Determinar la canƟdad de veces que se ingresaron 2 números conƟguos pares.
• Determinar la canƟdad de números que son múlƟplos del primer numero de la secuencia
• Determinar el porcentaje que representa la canƟdad del primer punto sobre el total de números
de la secuencia
"""

def validar_mayor(num, mensaje='Ingrese un número: '):
    numero = 0
    while numero <= num:
        numero = int(input(mensaje))
        if numero <= num:
            print('Error! El numero debe ser mayor a ', num)
    return numero

def validar_rango():
    cota_inferior = validar_mayor(0,'Ingrese la cota inferior: ')
    cota_superior = validar_mayor(0,'Ingrese la cota superior: ')
    while cota_superior < cota_inferior:
        cota_superior = validar_mayor('Ingrese cota superior (debe ser mayor a la inferior): ')
    return cota_inferior, cota_superior


# bloque principal
cota_inferior , cota_superior = validar_rango()


num = int(input('Ingrese un número (Finalice con cero): '))
if num < cota_inferior:
    print('Hola')
else:
    print('Adios')

#while num != 0:
#    num = int(input('Ingrese un número (Finalice con cero): '))