"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""
nombres = []
notas = []
condiciones = []
cant = 0

# carga de elementos
for x in range(4):
    nom = input('Ingresar nombre del alumno: ')
    nombres.append(nom)
    nota = int(input('Ingresar nota del alumno: '))
    notas.append(nota)

# identificar condicion del alumno
for x in range(4):
    if notas[x] >= 8:
        condiciones.append('Muy bueno')
        cant += 1
    elif notas[x] >= 4 and notas[x] <= 7:
        condiciones.append('Bueno')
    else:
        condiciones.append('Insuficiente')

#  salida por pantalla
for x in range(4):
    print(nombres[x], notas[x], condiciones[x])
    
print('La cantidad de alumnos con la condición muy bueno son ', cant)