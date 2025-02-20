def cargar_arreglo(vec):
    for i in range(len(vec)):
        vec[i] = int(input('Ingrese un número a cargar: '))


def calcular_promedio(suma,cant):
    prom = 0
    if cant != 0:
        prom = suma/cant
    return prom


def promedio_comprendido(v,x,y):
    acu = 0
    cant = 0
    for i in range(len(v)):
        if v[i] >= x and v[i] <= y:
            acu += v[i]
            cant += 1

    promedio = calcular_promedio(acu, cant)
    return promedio


def es_par(num):
    paridad = False
    if num % 2 == 0:
        paridad = True
    return paridad


def menor_impar(v):
    menor = v[0]
    for i in range(len(v)):
        if v[i] < menor and not es_par(v[i]):
            menor = v[i]
            
    if es_par(v[0]):
        menor = 0
    return menor


def listar_multiplo(v,x):
    res = ' '
    for pos in range(len(v)):
        if v[pos] % x == 0:
            res += str(v[pos]) + ','
    return res