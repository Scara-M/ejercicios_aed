import arreglos

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Valor mayor a ' + str(inf) + ': '))
        if n <= inf:
            print('Error: se pidió > a ', inf)
    return n

def test():
    n = validate(0)
    v = n * [0]
    arreglos.read(v)
    k = int(input('Ingrese el valor de k: '))
    arreglos.product(v,k)
    print('El vector quedó así: ', v)

if __name__ == '__main__':
    test()