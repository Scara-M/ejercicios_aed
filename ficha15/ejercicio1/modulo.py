def cargar_vector(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = float(input('Ingrese precipitación del mes ' + str(i+1) + ': '))


def calcular_promedio(suma,cant):
    prom = 0
    if cant != 0:
        prom = suma / cant
    return prom


def sumar_lluvias(vec,cant):
    #cant = len(vec)
    suma = 0
    for i in range(cant):
        suma += vec[i]

    c = calcular_promedio(suma, cant)
    return c


def determinar_prom_trimestre(vec):
    trimestre = int(input('Ingrese trimestre a calcular: '))
    if trimestre == 1:
        n = range(3)
    elif trimestre == 2:
        n = range(3,6)
    elif trimestre == 3:
        n = range(6,9)
    else:
        n = range(9,12)
    
    suma = 0
    for i in n:
        suma += vec[i]

    c = calcular_promedio(suma,len(n))
    return c 


def busqueda_mas_seco(vec):
    menor = vec[0]
    pos = 0
    for i in range(len(vec)):
        if vec[i] < menor:
            menor = vec[i]
            pos = i
    return menor, pos