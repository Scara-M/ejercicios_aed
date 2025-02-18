
def validar_rango(inf,max):
    num = inf - 1
    while num < inf or num > max:
        num = int(input('Ingresar un número entre (0 y 3): '))
        if num < inf or num > max:
            print('Error!! .. Valor incorrecto')
    return num


def validar(min,mensaje):
    num = min - 1
    while num < min:
        num = int(input(mensaje))
        if num < min:
            print('Error!!')
    return num


def cargar_arreglos(vec1,vec2):
    for i in range(len(vec1)):
        print('----- Venta  ----- ', i)
        vec1[i] = validar_rango(0,3)
        vec2[i] = validar(-1, 'Ingrese la cantidad de ventas: ')


def mostrar_arreglos(vec1,vec2):
    for i in range(len(vec1)):
        print('---- Venta ---- ', i)
        print('Articulo ', vec1[i], 'Cantidad ', vec2[i])


def contar(art, cant):
    acu = [0] * 4
    for i in range(len(art)):
        acu[art[i]] += cant[i]

    print('--- Cantidades vendidas por artículos ---')
    for i in range(len(acu)):
        print('Cantidad vendida del articulo ', i, ': ', acu[i])