"""
--Puntos en un plano--
Desarrollar un programa que permita ingresar las coordenadas de n puntos en el plano, e informe:
a) En qué cuadrante se encuentra cada uno.
b) Determinar cuántos puntos se encuentran en el primer o tercer cuadrante.
c) Determinar cuál de todos los puntos cargados se encuentra a mayor distancia del origen de coordenadas.
"""
# inicializacion de variables
cant_primer = cant_tercer = 0

# entrada de datos
n = int(input('Ingresar la cantidad de puntos a procesar: '))

for i in range(n):
    print('-'* 4)
    print('Punto ', i + 1)
    x = int(input('Ingresar coordenada x: '))
    y = int(input('Ingresar coordenada y: '))
    
    # determinar cuadrante
    if x > 0 and y > 0:
        print('Primer cuadrante')
        cant_primer += 1
        dist_primer = (x, y)
    elif x < 0 and y > 0:
        print('Segundo cuadrante')
        dist_segundo = (x, y)
    elif x < 0 and y < 0:
        print('Tercer cuadrante')
        cant_tercer += 1
        dist_tercer = (x, y)
    elif x > 0 and y < 0:
        print('Cuarto cuadrante')
        dist_cuarto = (x, y)
    else:
        print('Origen')
        

    # verificar distancia
    origen = (0,0)
    
    #if dist_primer > origen:
        

# puntos entre el primer y el tercer cuadrante
total_prim_ter = cant_primer + cant_tercer



    
