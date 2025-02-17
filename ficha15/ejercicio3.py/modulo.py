import math


def cargar_arreglo(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = int(input('Ingrese un número: '))


def es_primo(num):
    primo = True
    if num % 2 == 0:
        primo = False
    else:
        tope = math.ceil(math.sqrt(num))
        for i in range(3,tope):
            if num % i == 0:
                primo = False
                break
    return primo


def vector_primo(vec):
    v = []
    for item in vec:
        if es_primo(item):
            v.append(item)
    return v


def calcular_promedio(suma,cant):
    prom = 0
    if cant != 0:
        prom = suma / cant
    return prom


def primos_promedio(vec):
    n = len(vec)
    suma = 0
    for i in range(n):
        suma += vec[i]

    prom = calcular_promedio(suma,n)
    return prom
    