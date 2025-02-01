"""
-- Tutarras
Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
# inicializador de variables
aprobados = desaprobrados = 0

for x in range(10):
    nota = int(input('Ingrese la nota: '))

    # contar aprobados y desaprobados
    if nota >= 7:
        aprobados += 1
    else:
        desaprobrados += 1

# salida
print('La cantidad de aprobados es ', aprobados)
print('La cantidad de desaprobados es ', desaprobrados)