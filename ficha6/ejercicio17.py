"""
-- Tutarras
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
"""
# entrada de datos
n = int(input('Ingresar la cantidad de personas: '))
x = 0
alturas = 0

# proceso
while x < n:
    alt = float(input('Ingresar altura de la persona: '))
    alturas += alt
    x += 1

# determina promedio
prom = alturas/ n

# salida por pantalla
print('La altura promedio de las personas es ', prom)