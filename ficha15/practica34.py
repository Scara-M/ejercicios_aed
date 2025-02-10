"""
Crear y cargar una lista con los nombres de tres alumnos. 
Cada alumno tiene dos notas, almacenar las notas en una lista paralela. 
Cada componente de la lista paralela debe ser también una lista con las dos notas. 
Imprimir luego cada nombre y sus dos notas.
"""
alumnos = []
notas = []

# carga de elementos
for x in range(3):
    nom = input('Ingresar nombre del alumno: ')
    alumnos.append(nom)
    no1 = int(input('Ingresar primer nota del alumno: '))
    no2 = int(input('Ingresar segunda nota del alumno: '))
    notas.append([no1, no2])


# muestra por pantalla
for x in range(3):
    print('Alumno: ', alumnos[x], 'Nota1: ', notas[x][0], 'Nota2: ', notas[x][1])