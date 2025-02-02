"""
1 - Secuencia 1,2,3
Desarrollar un programa en Python que permita cargar por teclado una sucesión de números, uno
por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga.
El cero no debe considerarse un dato a procesar.
El programa debe:
• Determinar cuántos de los números ingresados eran divisibles por 4.
• Determinar el mayor de los números impares ingresados.
• Determinar cuántas veces se ingresó el primero de los números (cuente al primero).
• Determinar cuántas veces se ingresó un 1, seguido de un 2, y seguido a su vez de un 3. Por
ejemplo: en la sucesión: 3, 6, 1, 2, 3, 7, 8, 2, 3, 1, 2, 3, 0 ocurrió dos veces.
"""

# programa principal
def principal():
    print('Secuencia 1,2,3')
    print('-'*45)

    cont4 = 0
    cont_prim = 0
    c123 = 0
    s1 = s12 = False
    mayor = None

    num = int(input('Ingrese un número (finaliza con 0): '))
    while num != 0:

        # contar primero
        prim = num

        # divisible por cuatro
        if num % 4 == 0:
            cont4 += 1

        # mayor de los impares
        if num % 2 != 0:
            if mayor is None or num > mayor:
                mayor = num

        # contar cuantas veces se ingresó el primer número
        if num == prim:
            cont_prim += 1

        # determinar la secuencia 1 - 2 -3
        if num == 1:
            s1 = True
            s12 = False
        else:
            if num == 2 and s1:
                s12 = True
            else:
                if num == 3 and s12:
                    c123 += 1

                s12 = False
            s1 = False

        num = int(input('Ingrese un número (finaliza con 0): '))

    print('La cantidad de números divisibles por cuatro son: ', cont4)
    print('El mayor de los impares ingresados es el ', mayor)
    print('El primer número se ingresó ', cont_prim)
    print('La cantidad de veces que se repitió la secuencia 1,2,3 fueron ', c123)
principal()