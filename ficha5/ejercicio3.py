"""
--Mantenimiento Informático--
El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa que facilite la
gestión de las tareas realizadas en el día.

El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de identificación de la PC,
tiempo de reparación (expresado en minutos) y la causa de mantenimiento (1- Problema de Hardware 2-Problema
de Software)
Los requerimientos funcionales son:
a) ¿Cuál es el tiempo total de las tareas de mantenimiento?
b) ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
c) Tiempo promedio de tareas de mantenimiento.
d) Informar con un mensaje si todas las PC (Número de identificación) que se les ha realizado mantenimiento
tuvieron problemas de Hardware
"""

problemas_hardware = False


# Ingreso de datos de las tres pc
print(" ")
print('--Primer PC--')
num_id1 = int(input('Ingresar el número de identificación de la pc: '))
tiempo1 = int(input('Ingresar en minutos el tiempo de reparación: '))
causa1 = int(input('Ingresar 1- Problema de Hardware o 2- Problema de Software: '))
print(" ")

print('--Segunda PC--')
num_id2 = int(input('Ingresar el número de identificación de la pc: '))
tiempo2 = int(input('Ingresar en minutos el tiempo de reparación: '))
causa2 = int(input('Ingresar 1- Problema de Hardware o 2- Problema de Software: '))
print(" ")

print('Tercer PC')
num_id3 = int(input('Ingresar el número de identificación de la pc: '))
tiempo3 = int(input('Ingresar en minutos el tiempo de reparación: '))
causa3 = int(input('Ingresar 1- Problema de Hardware o 2- Problema de Software: '))
print(" ")

# Tiempo total de las tareas de mantenimiento
tiempo_total = tiempo1 + tiempo2 + tiempo3


# PC con mayor tarea de mantenimiento
if tiempo1 > tiempo2 and tiempo1 > tiempo3:
    mayor_tiempo = num_id1
elif tiempo2 > tiempo3:
    mayor_tiempo = num_id2
else:
    mayor_tiempo = num_id3


# Tiempo promedio de tareas de mantenimiento
tiempo_prom = round(((tiempo1 + tiempo2 + tiempo3)/3),2)


# Informar con un mensaje si todas las PC  que se les ha realizado mantenimiento tuvieron problemas de Hardware
if causa1 == 1 and causa2 == 1 and causa3 == 1:
    problemas_hardware = True


# Salida por pantalla
print('El tiempo total de las tareas de mantenimiento es de ', tiempo_total, ' minutos')
print('La PC con mayor tarea de mantenimiento es la ', mayor_tiempo)
print('El tiempo promedio de las tareas de mantenimiento es de ', tiempo_prom, ' minutos')

if problemas_hardware:
    print('Todas las PC tuvieron problemas de hardware')
else:
    print('No todas las pc tuvieron problemas de hardware')