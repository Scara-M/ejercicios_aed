"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. 
Ordenar de menor a mayor la lista.
"""
sueldos = []

# carga de elementos
for x in range(5):
    sueldo = float(input('Ingresar el sueldo: '))
    sueldos.append(sueldo)


# ordenar de menor a mayor
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x+1]:
            sueldos[x], sueldos[x+1] = sueldos[x+1], sueldos[x]

# salida por pantalla
print(sueldos)