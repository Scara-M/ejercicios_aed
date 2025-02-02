"""
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.
"""

def mayor(x1, x2, x3):
    if x1 > x2 and x1 > x3:
        print('El mayor es el primer número')
    else:
        if x2 > x3:
            print('El mayor es el segundo número')
        else:
            print('El mayor es el tercer número')


# programa principal
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))
mayor(num1,num2,num3)