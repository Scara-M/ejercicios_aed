"""
-- Galería de arte--
Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:
1. Verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901
y terminó en el año 2000).
2. Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
3. Informar la diferencia en años entre la obra más nueva y la más antigua.
"""
# inicializar varibales
ant_xx = False
obra_ingresada = False

# ingreso de años de los cuadros
cuadro1 = int(input('Ingresar el año del primer cuadro: '))
cuadro2 = int(input('Ingresar el año del segundo cuadro: '))
cuadro3 = int(input('Ingresar el año del tercer cuadro: '))
ingresado = int(input('Ingrese año: '))

# verificar si los cuadros son anteriores a 1901
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    ant_xx = True

# si alguna de las obras ingresadas es la que se crea por teclado
if cuadro1 == ingresado or cuadro2 == ingresado or cuadro3 == ingresado:
    obra_ingresada = True

# determinar la obra nueva y la vieja
if cuadro1 < cuadro2 and cuadro1 < cuadro3:
    menor = cuadro1
    if cuadro2 < cuadro3:
        mayor = cuadro3
    else:
        mayor = cuadro2
else:
    if cuadro2 < cuadro3:
        menor = cuadro2
        if cuadro1 > cuadro3:
            mayor = cuadro1
        else:
            mayor = cuadro3
    else:
        menor = cuadro3
        if cuadro1 > cuadro3:
            mayor = cuadro1
        else:
            mayor = cuadro3

# diferencia entre la obra nueva y antigua
diferencia = mayor - menor

# salida por pantalla
print('-'*45)
# verifica si los cuadros ingresados son anteriores al siglo xx
if ant_xx == True:
    print('Todos los cuadros ingresados son anteriores al siglo XX')
else:
    print('No todos los cuadros son anteriores al siglo XX')

# si alguna de las obras ingresadas es la que se crea por teclado
if obra_ingresada == True:
    print('Hay al menos una obra del catalogo que es la que se ingresó por catálogo')
else:
    print('No hay ninguna obra con el año ingresado')

# -- 3 diferencia entre la obra más nueva y mas antigua
print('El mayor es: ', mayor)
print('El menor es: ', menor)
print('La diferencia entre el mayor y el menor es de: ', diferencia)