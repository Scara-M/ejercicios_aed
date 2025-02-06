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

def calcular_porcentaje(cant,total):
    if total != 0:
        porc = cant / total * 100
    else:
        porc = 0
    return porc

def es_par(num):
    resto = num % 2
    if resto == 0:
        return True
    else:
        return False


# bloque principal
def main():
    cant_n1_n2 = cont_total = 0
    hay_impar_par = False
    cant_5 = 0
    anterior = 0

    n1 = int(input('Ingrese el valor de n1: '))
    n2 = int(input('Ingrese el valor de n2: '))

    num = int(input('Ingrese un número a procesar (Finalice con cero): '))
    while num != 0:
        cont_total += 1

        # cuantos son mayores a n1 y menores que n2
        if num > n1 and num < n2:
            cant_n1_n2 += 1
        
        # determinar ingreso de un impar
        if cont_total > 1:
            if not es_par(anterior) and es_par(num):
                hay_impar_par = True
        
        # Determinar cuántas veces se ingresó un 5 seguido inmediatamente de otro 5.
            if anterior == 5 and num == 5:
                cant_5 += 1

        anterior = num
        num = int(input('Ingrese un número a procesar (Finalice con cero): '))

    # determina el porcentaje
    porcentaje = calcular_porcentaje(cant_n1_n2,cont_total)
    print('El porcentaje de valores mayores a n1 y menores que n2 es del % ', porcentaje)
    # hay impar_impar
    if hay_impar_par == True:
        print('Hay un par seguido de un impar')
    else:
        print('No hay un par seguido de un impar')
    print('La cantidad de veces que se ingresó un 5 seguido de otro 5 son ', cant_5)
main()