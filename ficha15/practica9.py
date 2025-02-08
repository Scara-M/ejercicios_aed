"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""
sueldos = []
suma = 0

for x in range(5):
    num = float(input('Ingrese el sueldo: '))
    sueldos.append(num)
    suma += num

# calcula el promedio
prom = suma / 5 

# salida
print('Los sueldos de los operarios es ', sueldos)
print('El promedio de los sueldos es ', prom)