# carga por teclado de un vector de n casillas
def read(v):
    n = len(v)
    print('Cargue los elementos de un vector: ')
    for i in range(n):
        v[i] = int(input('Casilla[' + str(i) + ']: '))

# multiplica por k al arreglo
def product(v,k):
    n = len(v)
    for i in range(n):
        v[i] *= k