def carga_vector(vec):
    n = len(vec)
    for i in range(n):
        vec[i] = int(input('Ingrese valor de la casilla ' + str(i)+ ': '))


def determinar_mayor(v1,v2):
    n = len(v1)
    v = [0] * n

    for i in range(n):
        if v1[i] > v2[i]:
            v[i] = v1[i]
        else:
            v[i] = v2[i]
    return v
