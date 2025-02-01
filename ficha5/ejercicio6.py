"""
--Institución Educativa--
Una institución educativa necesita un programa que facilite la gestión de cupos de los cursos de primer grado.
Ingresar tres grados. De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B, ...) y la cantidad de
niños y de niñas y cupo máximo (que es el mismo para los tres cursos).
Los requerimientos funcionales son:
a) Código de identificación del curso que tenga menos alumnos inscriptos.
b) Porcentaje de niñas de cada curso.
c) Porcentaje de niños de cada curso.
d) Promedio general de alumnos.
e) Si algunos de los tres grados supera el cupo máximo informar un mensaje la necesidad de apertura de una
nueva división.
"""
# Ingreso de datos

cupo = int(input('Ingresar el cupo máximo del curso: '))
# grado1
print('---------- Curso 1 ----------')
cod_id1 = input('Ingresar código de identificación del curso: ')
cant_v1 = int(input('Ingresar la cantidad de niños del curso: '))
cant_m1 = int(input('Ingresar la cantidad de niñas del curso: '))
curso1 = cant_m1 + cant_v1

# grado2
print('---------- Curso 2 ----------')
cod_id2 = input('Ingresar código de identificación del curso: ')
cant_v2 = int(input('Ingresar la cantidad de niños del curso: '))
cant_m2 = int(input('Ingresar la cantidad de niñas del curso: '))
curso2 = cant_m2 + cant_v2

# grado3
print('---------- Curso 3 ----------')
cod_id3 = input('Ingresar código de identificación del curso: ')
cant_v3 = int(input('Ingresar la cantidad de niños del curso: '))
cant_m3 = int(input('Ingresar la cantidad de niñas del curso: '))
curso3 = cant_m3 + cant_v3

# proceso
# - cod id del curso con menos inscriptos
if curso1 < curso2 and curso1 < curso3:
    menos_insc = cod_id1
else:
    if curso2 < curso3:
        menos_insc = cod_id2
    else:
        menos_insc = cod_id3

# -- total inscriptos
total_m = cant_m1 + cant_m2 + cant_m3
total_v = cant_v1 + cant_v2 + cant_v3
total_inc = curso1 + curso2 + curso3

# -- porcentajes por curso
# mujeres
porc_m1 = cant_m1 / total_m * 100 
porc_m2 = cant_m2 / total_m * 100 
porc_m3 = cant_m3 / total_m * 100 
# varones
porc_v1 = cant_v1 / total_v * 100 
porc_v2 = cant_v2 / total_v * 100 
porc_v3 = cant_v3 / total_v * 100 

# -- promedio general
prom = (curso1 + curso2 + curso3)//3

# si alguno de los cursos supera el cupo maximo
supera = False
if curso1 > cupo or curso2 > cupo or curso3 > cupo:
    supera = True

# Salida por pantalla
# - 1 cod id del curso con menos inscriptos
print('El código de identificación del curso con menos inscriptos es: ', menos_insc)

# - 2 porc niñas de cada curso
print('El porcentaje de niñas del curso 1 es % ', porc_m1)
print('El porcentaje de niñas del curso 2 es % ', porc_m2)
print('El porcentaje de niñas del curso 3 es % ', porc_m3)
# - 3 porc niños de cada curso
print('El porcentaje de niños del curso 1 es % ', porc_v1)
print('El porcentaje de niños del curso 2 es % ', porc_v2)
print('El porcentaje de niños del curso 3 es % ', porc_v3)
# - 4 promedio general de alumnos
print('El promedio general de alumnos es de ', prom)
# - 5 si alguno de los cursos supera el cupo maximo
if supera == True:
    print('Algunos de los cursos supera el cupo')