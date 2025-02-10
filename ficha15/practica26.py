"""
Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. 
Luego ordenar las notas de mayor a menor. 
Imprimir las notas y los nombres de los alumnos.
"""
alumnos = []
notas = []

# carga de elementos
for x in range(5):
    nom = input('Ingresar nombre: ')
    alumnos.append(nom)
    no = int(input('Ingresar nota: '))
    notas.append(no)

# ordenar por notas de menor a mayor
for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x+1]:
            notas[x],notas[x+1] = notas[x+1],notas[x]
            alumnos[x],alumnos[x+1] = alumnos[x+1],alumnos[x]

# salida por pantalla
for x in range(5):
    print('La nota del estudiante ', alumnos[x], ' es ', notas[x])