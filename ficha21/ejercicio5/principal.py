"""
5 - Cobro de servicios
Desarrollar un programa que permita cargar, para una empresa de cobro de servicios, el detalle de
n cobranzas realizadas (n se carga por teclado) conteniendo la siguiente información: número de caja
(0-9 inclusive), turno (0: mañana, 1: tarde, 2: noche) y monto cobrado.

A medida que se cargan los datos, se pide generar una tabla resumen, dando a elegir al usuario una
carga manual o automática, donde cada fila represente una caja y cada columna un turno, totalizando
los montos cobrados.

Mostrar el contenido de la tabla, y luego informar:
• Recaudación promedio para una caja que se ingresa por teclado
• Total recaudado por cada turno, cuál es el mayor y qué porcentaje representa sobre la recaudación total.
• Qué caja y turno tuvo la menor recaudación acumulada
"""
from general import *
import random

def cargar_matriz(n,carga,m):
    for f in range(n): # ciclo de cargas que realizo el usuario
        if carga == 'm':
            caja = validar_entre(0,9, 'Ingrese número de caja (0 y 9): ')
            turno = validar_entre(0,2,'Ingrese turno entre (0 - 2): ')
            monto = validar(0,'Ingrese monto: ')
        else:
            caja = random.randint(0,9)
            turno = random.randint(0,2)
            monto = random.randint(100,1000)
            print('Cobranza: ', f , 'Caja: ', caja, 'Turno: ', turno, 'Monto: ', monto)
        m[caja][turno] += monto # se guarda cada monto en la fila caja de la columna turno


def mostrar_matriz(m):
    for f in range(len(m)): # itera primero sobre la cantidad de filas
        for c in range(len(m[f])): # itera sobre una fila
            if m[f][c] > 0:
                print('Caja: ', f, 'Turno: ', c,': $' ,m[f][c])


def mostrar_menu():
    print('=' * 80)
    print('Menú de opciones')
    print('1. Recaudacion promedio por caja')
    print('2. Total recaudado por cada turno')
    print('3. Menor recaudacion')
    print('0. Salir')
    opcion = int(input('Ingrese opcion: '))
    return opcion


def promediar_fila(m,caja):
    suma = 0
    for c in range(len(m[caja])): # c= columna Recorre cada columna de la fila. 
        suma += m[caja][c]
    return suma / len(m[caja])


def sumar_columnas(m):
    suma = [0] * len(m[0])
    for f in range(len(m)):
        for c in range(len(m[f])):
            suma[c] += m[f][c]
    return suma


# se retorna el indice porque pregunta por el indice, por eso no se retorna el valor del vector
def buscar_mayor(v):
    may = 0
    for i in range(1,len(v)):
        if v[i] > v[may]:
            may = i
    return may


def sumar_vector(v):
    total = 0
    for i in range(len(v)):
        total += v[i]
    return total


def buscar_menor(m):
    menf, menc = 0, 0 # el menor esta en la posicion cero-cero
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] < m[menf][menc]: # no se guarda el valor, sino la fila y la columna
                menf, menc = f, c # se cambian los indices, no el valor
    return menf, menc


# principal
def principal():
    print('COBRO DE SERVICIOS')
    # carga de datos
    n = validar(0,'Ingrese la cantidad de cobranzas: ')
    carga = input('Elija carga (M)anual o (A)utomática: ').lower()
    m = [[0] * 3 for f in range(10)]
    cargar_matriz(n, carga, m) # n son los registros que se van a cargar
    print('\nResumen de cobranzas')
    mostrar_matriz(m)

    # menu de opciones
    opcion = -1
    
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            caja = validar_entre(0,9,'Ingrese caja (0-9) a promediar: ')
            prom = promediar_fila(m, caja)
            print('Promedio para la caja ', caja, '$ ', prom)
        elif opcion == 2:
            turnos = sumar_columnas(m)
            print('Total recaudado por turnos', turnos)
            #mostrar_vector(turnos)
            may = buscar_mayor(turnos)
            print('La mayor recaudación fue en el turno ', may, ' de $ ', turnos[may])
            total = sumar_vector(turnos)
            porc = turnos[may] * 100 / total
            print('Representa el ', round(porc,2), '% sobre el total de $ ', total)

        elif opcion == 3: # se recorre toda la matriz y la que tuvo menor recaudacion
            caja, turno = buscar_menor(m)
            print('La menor recaudación fue en la caja ', caja, ' en el turno ', turno, ': $', m[caja][turno])

        elif opcion == 0:
            print('Adiossssssssss')


if __name__ == '__main__':
    principal()
