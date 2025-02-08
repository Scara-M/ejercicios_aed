"""
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. 
Imprimir luego el nombre y el promedio de las dos notas.
"""
lista = ['ana', 7, 9]

prom = (lista[1] + lista[2])//2

print('El nombre del alumno es ', lista[0])
print('El promedio es ', prom)