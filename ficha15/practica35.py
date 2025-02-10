"""
Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""
empleados = []
sueldos = []
totalsueldos = []

# carga de elementos
for x in range(3):
    nom = input('Ingresar nombre del empleado: ')
    empleados.append(nom)
    su1 = int(input('Ingresar sueldo 1: '))
    su2 = int(input('Ingresar sueldo 2: '))
    su3 = int(input('Ingresar sueldo 3: '))
    sueldos.append([su1,su2,su3])


# acumular los sueldos 
for x in range(3):
    total = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    totalsueldos.append(total)

for x in range(3):
    print(empleados[x], totalsueldos[x])

# obtener el mayor
mayor = totalsueldos[0]
pos = 0
for x in range(1,3):
    if totalsueldos[x] > mayor:
        mayor = totalsueldos[x]
        pos = x
print('El empleados con mayores ingresos es ', empleados[pos])