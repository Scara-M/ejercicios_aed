"""
--programacionYa
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""
n = int(input('Ingresar la cantidad de triángulos a analizar: '))
cant_equi = cant_isos = cant_esc = 0

for x in range(n):
    print('-' * 25)
    print('Triángulo ', x + 1)
    lado1 = int(input('Ingrese primer lado del triángulo: '))
    lado2 = int(input('Ingrese segundo lado del triángulo: '))
    lado3 = int(input('Ingrese tercer lado del triángulo: '))

    print('-' * 25)
    # determinar tipo de triángulo
    if lado1 == lado2 and lado1 == lado3:
        print('El triángulo es equilátero')
        cant_equi +=1
    else:
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print('El triángulo es escaleno')
            cant_esc += 1
        else:
            print('El triángulo es isosceles')
            cant_isos += 1

# salida por pantalla
print('La cantidad de triángulos equilateros es ', cant_equi) 
print('La cantidad de triángulos isoceles es ', cant_isos) 
print('La cantidad de triángulos escalenos es ', cant_esc) 