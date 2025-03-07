"""
8 - Concursos administración pública
El gobierno de la provincia de Córdoba desea guardar la información referida a los resultados de los
exámenes de concursos por cargos en la administración pública, en un arreglo de n registros (donde
n es un valor que se carga por teclado). 
Por cada resultado del concurso, se pide guardar el dni del concursante, su nombre, 
el cargo para el que se postuló (un código que va de 0 a 19, o sea, hay 20 cargos) y el puntaje 
obtenido (un valor de 0 a 100 , que puede tener decimales).
--
Se pide desarrollar un programa en Python controlado por un menú de opciones. Ese menú debe
permitir gestionar las siguientes tareas a partir del arreglo pedido en el párrafo anterior:
• Cargar el arreglo pedido con los datos de los n resultados. Validar que el código del cargo se
encuentre entre 0 y 19.
• Mostrar los datos de los concursantes que hayan aprobado el examen (se aprueba con 70 puntos
o más).
• Determinar cuántos concursantes rindieron el examen por cada Ɵpo de cargo (es decir, cuántos
concursantes rindieron por el cargo 0, cuántos por el cargo 1, cuántos por el cargo 2, etc... hasta
el cargo 19).
• Mostrar los datos del arreglo, ordenados de mayor a menor, por el puntaje obtenido en el
examen.
• Cargar por teclado el nombre de un postulante, y mostrar por pantalla todos los datos del mismo
si se encuentra en el vector. Si este postulante además aprobó el concurso, muestre un mensaje
que resalte ese resultado además de sus datos. Informe con otro mensaje si el postulante no se
encuentra en el vector
"""
from registro import *
import random

def validar_rango(min,max,mensaje):
    num = min - 1
    while num < min or num > max:
        num = int(input(mensaje))
        if num < min:
            print('Errro! Ingrese un número entre ' + str(min) + ' y ' + str(max))
    return num


def cargar_manual(v):
    for i in range(len(v)):
        # cada uno de estos campos se los pasa al constructor
        print('Concursante ', i + 1)
        dni = int(input('\tDNI: '))
        nom = input('\tIngrese el nombre: ')
        cargo = validar_rango(0,19,'\tIngrese código del cargo (0-19): ')
        puntaje = validar_rango(0,100,'\tPuntaje: ')
        v[i] = Concursante(dni,nom,cargo,puntaje) # en cada una de las celdas hay un registro. Es el constructor


def cargar_automatica(v):
    for i in range(len(v)):
        # cada uno de estos campos se los pasa al constructor
        dni = random.randint(11111111,99999999)
        nom = 'Concursante' + str(i)
        cargo = random.randint(0,19)
        puntaje = round(random.uniform(0,100),2)
        v[i] = Concursante(dni,nom,cargo,puntaje) # en cada una de las celdas hay un registro. Es el constructor


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


# ordenamiento por selecccion directa
def ordenar(v):
    n = len(v)
    for k in range(n-1):
        for i in range(k+1,n):
            if v[k].puntaje > v[i].puntaje: # se lo ordena con respecto a un campo del registro
                v[k],v[i] = v[i],v[k]


def principal():
    v = []

    op = -1
    while op != 0:

        print('\n SISTEMAS DE CONCURSOS')
        print('1 - Cargar')
        print('4 - Mostrar')
        print('0 - Salir')
        op = int(input('Elija su opcion: '))

        # punto 1
        if op == 1:
            n = validar_rango(0,19, 'Ingrese cantidad de concursantes (entre 0 y 19): ')
            v = [None] * n # se pone none, porque es el valor por defector para inicializar los registros. Ahora hay que convertir cada None en un registro
            carga = input('Carga (M)anual o (A)utomática')
            if carga == 'm' or carga == 'M':
                cargar_manual(v)
            else:
                cargar_automatica(v)
        else:
            if len(v) == 0:
                print('\tDebe cargar el vector (opcion 1) ')
            
            # opcion 4
            elif op == 4:
                ordenar(v)
                mostrar_vector(v)
        
        



if __name__=='__main__':
    principal()