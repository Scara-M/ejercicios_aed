import random

def cargar_arreglo(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = random.randint(100,10000)


def ordenar_arreglo(vec):
    n = len(vec)
    for k in range(n-1):
        for x in range(k+1, n):
            if vec[k] > vec[x]:
                vec[k], vec[x] = vec[x], vec[k]


def binary_seach(v,x):
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