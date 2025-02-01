"""
--Complejo de cines--
Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:
cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0
(cero).

El programa deberá:
a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con
descuento y $75 en los días sin descuento.
b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de
funciones.
"""
# Inicializar variables
recaudacion = 0
func_desc = 0
funciones = 0

# Entrada del ciclo
espectadores = int(input('Ingresar cantidad de espectadores (Ingrese cero para finalizar): '))


while espectadores != 0:
    descuento = input('Ingresar "S" si se aplico descuento o "N" si no se aplico: ').lower()

    if descuento == 's':
        entrada = 50
        func_desc += 1
    else:
        entrada = 75

    recaudacion += (entrada * entrada)
    funciones += 1
    
    # Nuevo inicio
    espectadores = int(input('Ingresar cantidad de espectadores (Ingrese cero para finalizar): '))

porcentaje = func_desc / funciones * 100

# Salida por pantalla
print(" ")
print('La recaudación total del complejo es de $ ', recaudacion)
print('La cantidad de funciones con descuento son ', func_desc)
print('El porcentaje de funciones con descuento que se efectuaron es del ', porcentaje, ' %')