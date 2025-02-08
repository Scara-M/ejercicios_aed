"""
Definir una lista que almacene por asignación los nombres de 5 personas. 
Contar cuantos de esos nombres tienen 5 o más caracteres.
"""
nombres=["juan", "ana", "marcos", "carlos", "luis"]
cont = 0

for x in range(len(nombres)):
    if len(nombres[x]) >= 5:
        cont += 1

# salida
print(cont)