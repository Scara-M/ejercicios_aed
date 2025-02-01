"""
-- Tutarras
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""
# entrada de datos
n = int(input('Ingresar la cantidad a procesar: '))
cant12 = 0

# proceso
for x in range(n):
    print('-'*45)
    base = float(input('Ingrese la base del triángulo: '))
    altura = float(input('Ingrese la altura del triángulo: '))

    # calcular superficie
    sup = base * altura
    print('------ Triángulo', x + 1)
    print('La base del triángulo es ', base)
    print('La altura del triangulo es ', altura)
    print('La superficie del triángulo es ', sup)

    # contar triángulos con una superficie mayor a 12
    if sup > 12:
        cant12 += 1

print('La cantidad de triángulos con una superficie mayor a 12 son ', cant12)
