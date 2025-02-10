"""
Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
"""
padres = []
hijos = []

# se carga los elementos
for k in range(3):
    ma = input('Ingresar el nombre de la madre: ')
    pa = input('Ingresar el nombre del padre: ')
    padres.append([ma,pa])
    cant = int(input('Ingresar la cantidad de hijos de los padres: '))
    hijos.append([])
    # lista de hijos
    for x in range(cant):
        nom = input('Ingresar el nombre del hijo: ')
        hijos.append(nom)

print('Listado del padre, madre y sus hijos')
for k in range(3):
    print('Padre: ', padres[k][0])
    print('Madre: ', padres[k][1])
    for k in range(len(hijos[k])):
        print('Hijo: ', hijos[k][x])

print('Listado del padre y cantidad de hijos que tiene')
for x in range(3):
    print('Padre: ', padres[x][0])
    print('Cantidad de hijos: ', len(hijos[x]))