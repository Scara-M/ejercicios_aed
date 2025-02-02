"""
Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.
"""
def calcular_superficie(lado):
    sup = lado * lado
    return sup

# programa principal
valor = int(input('Ingrese un valor: '))
sup = calcular_superficie(valor)
print('El valor de la superficie del cuadrado es ', sup)