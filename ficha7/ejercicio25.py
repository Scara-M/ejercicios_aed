"""
--programacion YA
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.

Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

# TURNO MAÑANA
acum_manana = 0

print('-- Turno Mañana -- ')
for x in range(5):
    edad = int(input('Ingrese la edad del estudiane: '))

    acum_manana += edad

prom_manana = acum_manana // 5

# TURNO TARDE
acum_tarde = 0

print(' ')
print('-- Turno Tarde -- ')
for x in range(6):
    edad = int(input('Ingrese la edad del estudiane: '))

    acum_tarde += edad

prom_tarde = acum_tarde // 6

# TURNO NOCHE
acum_noche = 0

print(' ')
print('-- Turno Noche -- ')
for x in range(11):
    edad = int(input('Ingrese la edad del estudiane: '))

    acum_noche += edad

prom_noche = acum_noche // 11

print(' ')
print('-' * 45)

# determinar el mayor promedio
if prom_manana > prom_tarde and prom_manana > prom_noche:
    mayor = 'Turno Mañana'
else:
    if prom_tarde > prom_noche:
        mayor = 'Turno Tarde'
    else:
        mayor = 'Turno Noche'

# salida por pantalla
print('El promedio del turno mañana es ', prom_manana)
print('El promedio del turno tarde es ', prom_tarde)
print('El promedio del turno noche es ', prom_noche)
print('El turno que tiene un promedio mayor es ', mayor)