"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""
# Turno mañana
lista1 = []

for x in range(4):
    valor = int(input('Ingrese el sueldo del operario del turno mañana: '))
    lista1.append(valor)

# Turno noche
lista2 = []

for x in range(4):
    valor = int(input('Ingrese el sueldo del operario del turno noche: '))
    lista2.append(valor)

# salida
print('Los sueldos del turno mañana son ', lista1)
print('Los sueldos del turno noche son ', lista2)