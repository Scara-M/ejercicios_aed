"""
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
"""
def presentacion():
    print('Suma de dos valores')

def linea():
    print('-'*45)


def suma():
    x1 = int(input('Ingrese primer número: '))
    x2 = int(input('Ingrese segundo número: '))
    suma = x1 + x2
    print('La suma de los dos valores es ', suma)

# programa principal
presentacion()
linea()
for x in range(5):
    suma()
    linea()
