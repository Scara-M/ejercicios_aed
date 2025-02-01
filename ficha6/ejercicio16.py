"""
-- Tutarras
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
# entrada de datos
x = 0
aprobados = 0
desaprobados = 0

# proceso
while x < 10:
    nota = int(input('Ingresar nota del alumno: '))
    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1
    x += 1

# salida por pantalla
print('La cantidad de aprobados son ', aprobados)
print('La cantidad de desaprobados son ', desaprobados)