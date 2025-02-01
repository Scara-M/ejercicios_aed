"""
--Ventas por sucursal--
Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes
sucursales de un país de una determinada empresa.
Los requerimientos funcionales del programa son:
a) Informar la cantidad de ventas ingresadas.
b) Total de ventas.
c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
d) Cantidad de ventas con 400, 500 y 600 unidades.
e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.
Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.
"""
# Inicializar variables
cant_ventas = 0
acum_ventas = 0
ventas_100_300 = 0
ventas_400_500_600 = 0
ventas_inferior50 = False


ventas = int(input('Ingresar la cantidad de ventas realizadas (finaliza con negativo): '))
while ventas > -1:
    # contar ventas
    cant_ventas += 1

    # total ventas ingresadas
    acum_ventas += ventas

    # ventas entre 100 y 300 unidades
    if ventas > 100 and ventas <= 300:
        ventas_100_300 += 1

    # ventas con 400, 500 y 600 unidades
    if ventas == 400 or ventas == 500 or ventas == 600:
        ventas_400_500_600 += 1

    # ventas inferior a 50
    if ventas < 50:
        ventas_inferior50 = True
    
    ventas = int(input('Ingresar la cantidad de ventas realizadas (finaliza con negativo): '))


# Salida por pantalla
print('La cantidad de ventas ingresadas fueron ', cant_ventas)
print('EL total de ventas realizadas fue de ', acum_ventas)
print('La cantidad de ventas entre 100 y 300 unidades fueron ', ventas_100_300)
print('La cantidad de ventas con 400, 500 y 600 unidades es de ',  ventas_400_500_600)
if ventas_inferior50:
    print('Hubo al menos una venta inferior a 50 unidades')