"""
-- Tutarras
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
"""
# entrada de datos
n = int(input('Ingresar la cantidad de piezas a procesar: '))
x = 0
cant = 0

# proceso
while x < n:
    long = float(input('Ingrese la longitud del perfil: '))
    if long >= 1.2 and long <= 1.3:
        cant += 1
    x += 1

# salida por pantalla
print('La cantidad de piezas aptas son ', cant)