"""
--Menú de Opciones Básico--
Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:
Si la opción es 1 mostrar la superficie de un triángulo. Para calcular la superficie debe usarse la fórmula de Herón:
superficie = raiz cuadrada (s*(s-a) (s-b) (s-c)
s = (a + b+ c)/2
Si la opción ingresada es 2 mostrar el perímetro del triángulo.
Si la opción ingresada es 3 informar la longitud del lado menor.
Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.
"""

error = False


# Menu
print('1 - Calcular superficie del triángulo')
print('2 - Calcular perímetro del triángulo')
print('3 - Informar longitud menor del triángulo')
opcion = int(input('Ingrese su opción: '))
print(" ")


if opcion > 0 and opcion < 4:
    # Ingresar lados del triángulo
    lado1 = int(input('Ingresar lado 1 del triángulo: '))
    lado2 = int(input('Ingresar lado 2 del triángulo: '))
    lado3 = int(input('Ingresar lado 3 del triángulo: '))
    print(" ")

    # opcion 1
    if opcion == 1:
        s = (lado1 + lado2 + lado3) / 2
        superficie = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
        print('La superficie del triángulo es ', superficie)
    else:
        # Opcion 2
        if opcion == 2:
            perimetro = lado1 + lado2 + lado3
            print('El perímetro del triángulo es ', perimetro)
        else:
            # Opcion 3
            if opcion == 3:
                if lado1 < lado2 and lado1 < lado3:
                    menor = lado1
                else:
                    if lado2 < lado3:
                        menor = lado2
                    else:
                        menor = lado3
                print('El lado menor es ', menor)
            else:
                error = True
        
else:
    print('Error!!. Opcion ingresada incorrecta')