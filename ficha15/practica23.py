"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. 
Crear y cargar una lista con todos los sueldos de dichos empleados. 
Imprimir la lista de sueldos ordenamos de menor a mayor.
"""
empleados = []

# carga de elementos
n = int(input('Ingresar la cantidad de empleados: '))
for x in range(n):
    sueldo = float(input('Ingrese el sueldo del empleado: '))
    empleados.append(sueldo)

# ordenar sueldos de menor a mayor
for k in range(n):
    for x in range(n-k):
        if empleados[x] > empleados[x+1]:
            empleados[x],empleados[x+1] = empleados[x+1], empleados[x]

# salida
print(empleados)
