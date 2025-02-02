# determina el menor de tres numeros
def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        men = n1
    else:
        if n2 < n3:
            men = n2
        else:
            men = n3
    return men


# determina el cubo de un numero
def calcular_cubo(num):
    cubo = num ** 3
    return cubo


# funcion de cuadrado
def calcular_cuadrado(num):
    cuadrado = num ** 2
    return cuadrado


# funcion reutilizable
def calcular_potencia(base, exp):
    potencia = base ** exp
    return potencia


# programa principal
a = int(input('Ingrese un número: '))
b = int(input('Ingrese un número: '))
c = int(input('Ingrese un número: '))
numero_menor = menor(a, b, c)
cubo = calcular_cubo(numero_menor)

print('El menor es:  ', numero_menor)
print('El cubo del menor es:  ', cubo)
