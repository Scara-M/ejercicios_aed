"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. 
Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""
productos = []
precios = []
cont = 0

# carga de elementos
for x in range(5):
    prod = input('Ingresar producto: ')
    productos.append(prod)
    precio = float(input('Ingrese precio del artículo: '))
    precios.append(precio)


# identificar cuantos productos tienen un precio mayor al primer producto
primero = precios[0]
for x in range(1,5):
    if precios[x] > primero:
        cont += 1

# salida
print('La cantidad de productos con un precio mayor al primero ingresado son ', cont)