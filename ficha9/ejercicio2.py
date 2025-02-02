"""
2 - Secuencia 5,5
Desarrollar un programa en Python que permita cargar por teclado una sucesión de números, uno
por uno. Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga.
El cero no debe considerarse un dato a procesar. El programa debe:
• Determinar cuántos de los números ingresados eran mayores que n1 y menores que n2 (cargar
previamente por teclado los números n1 y n2).
• Determinar el porcentaje que el total de números calculado en el punto 1 representa en el total
de números cargados.
• Determinar si en algún momento se ingresó un número impar seguido inmediatamente de un
par. No importa cuántas veces ocurrió: sólo indicar si al menos una vez pasó.

• Determinar cuántas veces se ingresó un 5 seguido inmediatamente de otro 5. Por ejemplo: en
la sucesión: 3, 6, 5, 5, 7, 5, 2, 5, 9, 5, 5, 0 ocurrió dos veces.
"""

def calcular_porcentaje(cant, total):
    if total == 0:
        porc = 0
    else:
        porc = cant * 100 / total
    return porc

def es_par(num):
    paridad = False
    if num % 2 == 0:
        paridad = True
    return paridad

# programa principal
def principal():
    print('** Secuencia 5 **')
    print('-' * 45)

    # inicialización de variables
    cont_num = 0
    contn1_n2 = 0
    sec_imp_par = nimpar = False
    anterior = 0
    cant5_5 = 0
    hay_cinco = False

    # carga de numeros a comparar
    n1 = int(input('Ingresar primer número a comparar: '))
    n2 = int(input('Ingresar segundo número a comparar: '))
    print('-' * 45)

    # procesamiento del programa
    num = int(input('Ingresar número (finalice con cero): '))
    while num != 0:
        # contar total numeros cargados
        cont_num += 1

        # determinar mayores que n1 y n2
        if (num > n1) and (num < n2):
            contn1_n2 += 1

        # si en algún momento se ingresó un número impar seguido de un par
        if not es_par(num):
            nimpar = True
        else:
            if es_par(num) and nimpar:
                sec_imp_par = True
            nimpar = False

        # secuencia 5 - 5
        if anterior == 5 and num == 5:
            cant5_5 += 1
            
        anterior = num
        # carga por doble lectura
        num = int(input('Ingresar número (finalice con cero): '))

    # determinar porcentaje
    porcentaje = calcular_porcentaje(contn1_n2, cont_num)

    # salida por pantalla
    print('El porcentaje de los números cargados >n1 y <n2 es del %', porcentaje)

    if sec_imp_par:
        print('Al menos una vez se ingresó un impar seguido de un par')
    else:
        print('No se ingresó un impar seguido de un par')

    print('La cantidad de veces que se ingresó la secuencia 5-5 es: ', cant5_5)
principal()