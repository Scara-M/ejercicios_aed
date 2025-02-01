"""
--Sueldos y aguinaldo--
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre.
"""
menor = None
pos = 0
mayor = None
acum = cont = 0

sueldos = (13000, 12000, 14000, 15000, 110000, 190000)

for x in range(len(sueldos)):
    # ejercicio a
    if mayor is None or sueldos[x] > mayor:
        mayor = sueldos[x]

    # ejercicio b
    if menor is None or sueldos[x] < menor:
        menor = sueldos[x]
        pos = x + 1

    # ejercico c
    acum += sueldos[x]
    cont += 1
        
aguinaldo = mayor / 2


# Salida por pantalla
print('El aguinaldo del vendedor es ', aguinaldo)        
print('Recibió el sueldo más bajo en el ', pos, ' mes')
if cont != 0:
    promedio = acum // cont
else:
    promedio = 0
print('El sueldo promedio del semestre es ', promedio)