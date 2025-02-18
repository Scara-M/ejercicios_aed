import random

def carga_aleatoria(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = random.randint(1, 100)


def ordenar_vector(vec):
    n = len(vec)
    for k in range(n-1):
        for x in range(k+1,n):
            if vec[k] > vec[x]:
                vec[k],vec[x] = vec[x],vec[k]


def search_binary(v,x):
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2

        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def busqueda_impares(v, x):
    n = len(v)
    cant = 0
    for i in range(n):
        if not es_par(v[i]) and v[i] > x:
            cant += 1
    return cant