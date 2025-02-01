"""
--Ciclistas--
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es
menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""

# Inicializador de variables
menor = None
supero_record = False
acum_tiempo = 0
cont = 0

n = int(input('Ingresar la cantidad de competidores: '))
tiempo_record = int(input('Ingresar el tiempo récord de la carrera: '))

for x in range(n):
    # datos del competidor
    nom = input('Ingresar el nombre del competidor: ')
    tiempo = int(input('Ingresar el tiempo de carrera del competidor: '))

    # menor tiempo 
    if menor is None or tiempo < menor:
        menor = tiempo
        ganador = nom

    # c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
    acum_tiempo += tiempo
    cont += 1

if cont > 0:
    promedio = acum_tiempo / cont
else:
    promedio = 0


# Salida por pantalla
print(" ")
print('El ganador es ', ganador)
if menor < tiempo_record:
    print('El ganador superó el record')
else:
    print('El ganador no superó el record.')
print('El tiempo promedio de todos los ciclistas es ', promedio)
