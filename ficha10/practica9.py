"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
"""

def ordenar(x1,x2,x3):
    if x1 < x2 and x1 < x3:
        menor = x1
        if x2 < x3:
            medio = x2
            mayor = x3
        else:
            medio = x3
            mayor = x2
    else:
        if x2 < x3:
            menor = x2
            if x1 < x3:
                medio = x1
                mayor = x3
            else:
                medio = x3
                mayor = x1
        else:
            menor = x3
            if x1 < x2:
                medio = x1
                mayor = x2
            else:
                medio = x2
                mayor = x1
    print('Los números ordenados de menor a mayor son ', menor, medio, mayor)

def carga_numero():
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese un número: '))
    n3 = int(input('Ingrese un número: '))
    ordenar(n1,n2,n3)

# bloque principal
carga_numero()