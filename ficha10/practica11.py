"""
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
"""
def retornar_mayor(x1,x2):
    if x1 > x2:
        mayor = x1
    else:
        mayor = x2
    return mayor

# programa principal
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
may = retornar_mayor(num1,num2)
print('El mayor de los dos números es ', may)