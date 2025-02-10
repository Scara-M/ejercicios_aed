"""
Crear una lista y almacenar los nombres de 5 países. 
Ordenar alfabéticamente la lista e imprimirla.
"""
paises = []

# carga de elementos
for x in range(5):
    nom = input('Ingresar el nombre del país: ')
    paises.append(nom)

# ordenar alfabeticamente
for k in range(4):
    for x in range(4-k):
        if paises[x] > paises[x+1]:
            paises[x],paises[x+1] = paises[x+1],paises[x]

# salida
print(paises)