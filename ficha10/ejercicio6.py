"""
6 - Secuencia promedio de pares
Se pide desarrollar un programa en Python controlado por un menú de opciones. Ese menú debe permitir gestionar las siguientes tareas, siempre usando funciones que acepten parámetros y/o retornen valores en cada situación en que se considere apropiado:
-------
• Cargar una sucesión de números enteros y positivos (validar que efectivamente cada número
que se cargue sea mayor a cero). La carga finaliza cuando se ingresa un cero. Mostrar la canƟdad
de números de la sucesión cargada que son múlƟplos del primer numero de la secuencia.
------
Ingresar por teclado dos números p y q que definen los límites de un intervalo [𝑝, 𝑞] (validar
que 0 < 𝑝 < 𝑞) y una sucesión de n números (también cargando n por teclado y validando
que 𝑛 > 0). Determine cuántos de los números de la sucesión cargada están fuera del intervalo
y cuántos están dentro del intervalo, e indicar también cuántos de los números cargados eran
pares y estaban dentro del intervalo dado.
-------
Cargar una secuencia de números enteros posiƟvos (validar que efecƟvamente cada número
que se cargue sea mayor a cero). La carga debe terminar cuando se ingrese un número mayor a
100. Determine si en la secuencia se ingresaron dos números conƟguos que sean pares. Si es así
muestre el promedio de todos los números pares que se hayan ingresado. Si no, informe que no
se ingresaron números conƟguos pares. Ejemplo: en la secuencia 1, 2, 3, 6, 4, 7, 8 hay al menos
un dos números conƟguos que son pares (el 6 y el 4) y en este caso, el promedio de todos los
pares de la secuencia es (2 + 6 + 4 + 8) / 4 = 20/4 = 5. Pero en esta secuencia: 1, 2, 5, 7, 8, 9, 3,
6, 1 no hay números conƟguos pares.
"""
def validar_mayor(valor,mensaje='Ingrese un número: '):
    numero = int(input(mensaje))
    while numero <= valor:
        print('El número debe ser mayor a ', valor)
        numero = int(input(mensaje))
    return numero


def es_multiplo(numero,divisor):
    paridad = numero % divisor
    if paridad == 0:
        return True
    else:
        return False


def validar_rango():
    n1 = validar_mayor(0, 'Ingrese el valor mínimo p: ')
    n2 = validar_mayor(0, 'Ingrese el valor máximo q: ')
    while n2 <= n1:
        print('Error! El valor de q debe ser mayor al de p')
        n2 = validar_mayor(0, 'Ingrese el valor máximo q: ')
    return n1, n2


# bloque principal
menu = ('-------------------------\n\
1 - Cargar una sucesión de números enteros y positivos\n\
2 - Numeros en el intervalo \n\
3 - Numeros contiguos \n\
4 - Salir del programa \n\
-------------------------')

op = -1
while op != 4:
    print(menu)
    op = int(input('Ingrese una opción (Finalice con 4): '))

    # opcion 1
    if op == 1:
        cant = 0
        
        num = validar_mayor(-1,'Ingrese un número(Finaliza con cero): ')
        primero = num
        while num != 0:
            if es_multiplo(num,primero):
                cant += 1
            num = validar_mayor(-1,'Ingrese un número(Finaliza con cero): ')
        print('La cantidad de números que son múltiplos del primer número ingresado son: ', cant)

    # opcion 2
    elif op == 2:
        cant_fuera = cant_adentro = 0
        pares = impares = 0

        p, q = validar_rango()
        
        n = validar_mayor(0, 'Ingrese la cantidad de números a procesar: ')
        for x in range(n):
            num = int(input('Ingrese un número: '))

            # dentro o fuera del rango
            if num < p or num > q:
                cant_fuera += 1
            else:
                cant_adentro += 1

            #  determinar cantidad pares e impares
            if es_multiplo(num,2):
                pares += 1
            else: 
                impares += 1
        # salida
        print('La cantidad de números fuera del intervalo son: ', cant_fuera)
        print('La cantidad de números dentro del intervalo son: ', cant_adentro)
        print('La cantidad de pares son ', pares)
        print('La cantidad de impares son ', impares)
        
    # opcion 3
    elif op == 3:
        
        num = validar_mayor(0, 'Ingrese un entero positivo (Finaliza con mayor a 100): ')
        while num < 100:
             num = validar_mayor(0, 'Ingrese un entero positivo (Finaliza con mayor a 100): ')
    else:
        print('-'*15)
        print('Opción Incorrecta. Vuelva a ingresar')
else:
    print('-'*45)
    print('ADIOSSSS')

"""
Cargar una secuencia de números enteros posiƟvos (validar que efecƟvamente cada número
que se cargue sea mayor a cero). La carga debe terminar cuando se ingrese un número mayor a
100. Determine si en la secuencia se ingresaron dos números conƟguos que sean pares. Si es así
muestre el promedio de todos los números pares que se hayan ingresado. Si no, informe que no
se ingresaron números conƟguos pares. 
Ejemplo: en la secuencia 1, 2, 3, 6, 4, 7, 8 hay al menos
un dos números conƟguos que son pares (el 6 y el 4) y en este caso, el promedio de todos los
pares de la secuencia es (2 + 6 + 4 + 8) / 4 = 20/4 = 5. Pero en esta secuencia: 1, 2, 5, 7, 8, 9, 3,
6, 1 no hay números conƟguos pares.
"""