def carga_vector(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = int(input('Ingrese un número: '))


def contar_ultimo_elemento(vec):
    cant = 0
    n = len(vec)
    ultimo = vec[-1]
    for i in range(n-1):
        if vec[i] == ultimo:
            cant += 1
    return cant


def menores_primero(vec):
    v = []
    primero = vec[0]
    for i in range(1,len(vec)):
        if vec[i] < primero:
            v.append(vec[i])
    return v