"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""
alturas = []
suma = 0
altas = bajas = 0

for x in range(5):
    alt = float(input('Ingresar la altura de la persona: '))
    alturas.append(alt)
    suma += alt

# calcula el promedio
prom = suma // 5

for x in range(5):
    if alturas[x] > prom:
        altas += 1
    else:
        bajas += 1

# salida por pantalla
print('El promedio de las alturas es ', prom)
print('La cantidad de personas que son más altas que el promedio son: ', altas)
print('La cantidad de personas que son más bajas que el promedio son: ', bajas)