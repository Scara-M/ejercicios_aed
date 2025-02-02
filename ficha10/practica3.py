"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.
"""

def cuadrado():
    print('Cuadrado de un número')
    num = int(input('Ingrese un número: '))
    cuadrado = num ** 2
    print('El cuadrado de',num, 'es',cuadrado)


def producto():
    print('Producto de dos números')
    num1 = int(input('Ingrese primer número: '))
    num2 = int(input('Ingrese segundo número: '))
    prod = num1 * num2
    print('El producto de los valores ingresados es ', prod)


# programa principal
cuadrado()
producto()