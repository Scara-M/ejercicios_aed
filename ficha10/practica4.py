"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""

def calcular_menor():
    n1 = int(input('Ingresar primer número: '))
    n2 = int(input('Ingresar segundo número: '))
    n3 = int(input('Ingresar tercer número: '))
    
    if n1 < n2 and n1 < n3:
        menor = n1
    else:
        if n2 < n3:
            menor = n2
        else:
            menor = n3
    # salida
    print('El menor de los valores ingresados es el ', menor)

# programa principal
calcular_menor()
calcular_menor()