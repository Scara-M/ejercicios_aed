"""
-- Programación Ya
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""
# inicializaro de variables
cont1c = 0
cont2c = 0
cont3c = 0
cont4c = 0

n = int(input('Ingresar la cantidad de puntos a procesar: '))

for x in range(n):
    print('Punto', x + 1)
    x = int(input('Ingrese la coordenada x: '))
    y = int(input('Ingrese la coordenada y: '))

    # determinar cuadrante
    if x > 0 and y > 0:
        cont1c += 1
    else:
        if x > 0 and y < 0:
            cont2c += 1
        else:
            if x < 0 and y < 0:
                cont3c += 1
            else:
                cont4c += 1

# salida por pantalla
print('La cantidad de puntos en el primer cuadrante son ', cont1c)
print('La cantidad de puntos en el segundo cuadrante son ', cont2c)
print('La cantidad de puntos en el tercer cuadrante son ', cont3c)
print('La cantidad de puntos en el cuarto cuadrante son ', cont4c)

