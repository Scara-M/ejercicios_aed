"""
5 - Farmacia
Generar un archivo llamado stock.dat conteniendo un registro por cada arơculo de la farmacia,
con los siguientes campos: código, descripción, precio unitario, stock actual, stock ideal.

Crear un programa que cargue el contenido del archivo en un vector (ordenado alfabéticamente
por descripción de articulo) y luego ofrezca un menú con las siguientes opciones:

• Listado: mostrar el contenido del vector.
• Compras: ingresar un código de arơculo. Si existe, ingresar la canƟdad comprada y sumarla al
stock actual. Si no existe, informarlo.
• Ventas: ingresar un nombre de arơculo. Si existe, ingresar la canƟdad que se desea vender; controlar que exista suficiente stock, restar la canƟdad vendida e informar el monto de la venta
(canƟdad por precio unitario). Si el arơculo no existe o no hay suficiente stock, informarlo.
• Actualización: reemplazar el contenido del archivo stock.dat con los datos del vector.
• Pedido: crear un archivo de texto llamado pedido.txt, conteniendo todos los arơculos que necesitan reposición (stock actual <stock ideal). Por cada línea indicar: arơculo, canƟdad a pedir,
costo esƟmado.
"""
from registro import *
import os.path
import pickle


def add_in_order(v,art):
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2
        
        if art.nombre == v[c].nombre:
            pos = c
            break
        if art.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [art]


def generar_vector(fd):
    v = []
    if not os.path.exists(fd):
        print('El Archivo no existe')
    else:
        tam = os.path.getsize(fd)
        m = open(fd,'rb')
        while m.tell() < tam:
            art = pickle.load(m)
            #v.append(art)
            add_in_order(v, art)
        m.close()
    return v


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def mostrar_menu():
    print('\nSISTEMA DE FARMACIA')
    print('1. Listado')
    print('2. Compras')
    print('3. Ventas')
    print('4. Actualizacion')
    print('5. Pedido')
    print('0. Salir')
    opcion = int(input('Elija su opcion: '))
    print('-'* 80)
    return opcion


def buscar_por_codigo(v,cod):
    for i in range(len(v)):
        if v[i].codigo == cod:
            return i
    return -1


def buscar_por_nombre(v,nom):
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2
        
        if nom == v[c].nombre:
            return c
        if nom < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    return -1


def actualizar_archivo(v,fd):
    m = open(fd,'wb')
    for i in range(len(v)):
        pickle.dump(v[i],m)
    m.close()
    print('Archivo ', fd, 'grabado')


def generar_pedido(v):
    fd = 'pedido.txt'   
    m = open(fd,'wt')
    for i in range(len(v)):
        if v[i].stock_actual < v[i].stock_ideal:
            cant = v[i].stock_ideal - v[i].stock_actual
            linea = '{} {} {}\n'.format(v[i].nombre, cant, cant*v[i].precio)
            # en la linea van tres campos. con el format el campo que debe ir
            m.write(linea)
    m.close()
    print('Archivo ', fd, 'grabado')

# principal
def principal():
    fd = 'stock.dat'
    v = generar_vector(fd)  # file descriptor

    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()

        if opcion == 1:
            mostrar_vector(v)

        elif opcion == 2:
            cod = int(input('Ingrese código a buscar: '))
            pos = buscar_por_codigo(v,cod)
            if pos == -1:
                print('El artículo no existe')
            else:
                print(v[pos])
                cant = int(input('Ingrese cantidad comprada: '))
                v[pos].stock_actual += cant
                print('Stock Actualizado')
                print(v[pos])
        
        elif opcion == 3:
            nom = input('Ingrese nombre del artículo: ')
            pos = buscar_por_nombre(v,nom)
            if pos == -1:
                print('El articulo no existe')
            else:
                print(v[pos])
                cant = input('Ingrese nombre del artículo: ')
                if cant > v[pos].stock_actual:
                    print('No hay suficiente stock para realizar la venta')
                else:
                    v[pos].stock_actual -= cant
                    print('Mondo de la venta $ ', cant * v[pos].precio)
                    print(v[pos])
        
        elif opcion == 4:
            actualizar_archivo(v,fd)
        
        elif opcion == 5:
            generar_pedido(v)


if __name__=='__main__':
    principal()
