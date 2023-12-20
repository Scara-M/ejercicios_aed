"""
--Terreno--
Se ingresan las medidas de frente y fondo de un terreno.
Determinar si es cuadrado o rectangular y calcular su superficie
"""

# Ingreso de medidas
frente = int(input('Ingresar las medidas del frente del terreno: '))
fondo = int(input('Ingresar la medida del fondo del terreno: '))

# determinar si es cuadrado o rectangular
if frente == fondo:
    print('El terreno es cuadrado')
else:
    print('El terreno es rectángular')

# calculo de superficie
sup = frente * fondo
print('La superficie del terreno es de ', sup, 'metros cuadrados')