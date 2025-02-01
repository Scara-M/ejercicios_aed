"""
--Menú y números aleatorios--
Realice un programa que le ofrezca al usuario un menú de opciones que le permita ejecutar las siguientes acciones:
Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].
Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].
Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor
promedio de los números menores a 10.000.
Cualquier otro número: Salir del programa.
"""
import random
# Inicializar variables

# Menu
print('1 - Calcular promedio de 1000 numeros aleatorios')
print('2 - Buscar el mayor de 10.000 números aleatorios')
print('3 - Buscar el menor de 5000 números aleatorios')
print('Elija otro número para salir del programa')
opcion = int(input('Ingrese su opción: '))
print(" ")

while opcion > 0 and opcion < 4:
    if opcion == 1:
        x = 0
        acum = 0
        while x < 1000:
            num = random.randint(0, 100000)
            acum += num
            x += 1
        promedio = acum / 1000
        print('El promedio de los 1000 números aleatorios es de ', promedio)
    
    # Buscar el mayor
    if opcion == 2:
        x = 0
        mayor = 0
        while x < 10000:
            num = random.randint(0, 100000)
            if num > mayor:
                mayor = num
            x += 1
        print('El mayor de los 10000 números aleatorios es ', mayor)
    
    # Buscar el menor y calcular el valor promedio de los números menores a 10.000.
    if opcion == 3:
        x = 0
        menor = 100000
        acum = 0
        cont = 0

        while x < 5000:
            num = random.randint(0, 100000)
            if num < menor:
                menor = num
            
            if num < 10000:
                acum += num
                cont += 1
            x += 1

        if cont != 0:
            prom = acum / cont
        else:
            prom = 0
        print('El menor de los 5000 números generados es ', menor) 
        print('El promedio de los valores menores a 10000 es ', prom)
        
    print(" ")
    print('1 - Calcular promedio de 1000 numeros aleatorios')
    print('2 - Buscar el mayor de 10.000 números aleatorios')
    print('3 - Buscar el menor de 5000 números aleatorios')
    print('Elija otro número para salir del programa')
    opcion = int(input('Ingrese su opción: '))
    print(" ")

print('ADIOOOSSSSSSSSSS')