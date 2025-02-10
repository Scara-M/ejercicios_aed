"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
"""
empleados=[]
faltas=[]

for k in range(3):
    nom=input("Ingrese el nombre de empleado:")
    empleados.append(nom)
    cant=int(input("Cuantos dias falto:"))
    faltas.append([])
    for x in range(cant):
        dia=int(input("Ingrese el numero de dia que falto:"))
        faltas[k].append(dia)

print("Nombres de empleados y dias que falto")
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print(faltas[k][x])

print("Nombres de empleados y cantidad de inasistencias")
for x in range(3):
    print(empleados[x],len(faltas[x]))

men=len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<men:
        men=len(faltas[x])

print("Empleado o empleados que faltaron menos")
for x in range(3):
    if len(faltas[x])==men:
           print(empleados[x])