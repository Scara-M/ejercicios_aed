"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. 
Desplazar el valor mayor de la lista a la última posición.
"""
sueldos = []

# carga de elementos
for x in range(5):
    su = float(input('Ingresar sueldo: '))
    sueldos.append(su)

"""
# desplazar el mayor a la derecha
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print(sueldos)

"""
# con tuplas
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x+1]:
            sueldos[x], sueldos[x+1] = sueldos[x+1], sueldos[x]

print(sueldos)
