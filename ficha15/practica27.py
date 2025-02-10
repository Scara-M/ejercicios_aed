"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. 
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
"""
paises = []
habitantes = []

# cargar elementos
for x in range(5):
    pa = input('Ingresar nombre del país: ')
    paises.append(pa)
    cant = int(input('Ingresar la cantidad de habitantes: '))
    habitantes.append(cant)

# ordenar alfabeticamente
for k in range(4):
    for x in range(4-k):
        if paises[x] > paises[x+1]:
            paises[x],paises[x+1] = paises[x+1],paises[x]
            habitantes[x], habitantes[x+1] = habitantes[x+1], habitantes[x]
print()
print('Ordenado alfabeticamente')
for x in range(5):
    print(paises[x], 'habitantes: ', habitantes[x])

print()
# orden descendente de habitantes
for k in range(4):
    for x in range(4-k):
        if habitantes[x] < habitantes[x+1]:
            habitantes[x], habitantes[x+1] = habitantes[x+1],habitantes[x]
            paises[x],paises[x+1] = paises[x+1],paises[x]
print()
print('Orden descendente por habitantes')
for x in range(5):
    print(paises[x], 'habitantes: ', habitantes[x])