"""
--Tutarras
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""
# --------------  Lista 1
print('-------- Lista 1 ---------')
x1 = 0
suma1 = 0

# proceso
while x1 < 15:
    num = int(input('Ingrese un número: '))
    suma1 += num
    x1 += 1

# --------------  Lista 2
print('-------- Lista 2 ---------')
x2 = 0
suma2 = 0

# proceso
while x2 < 15:
    num = int(input('Ingrese un número: '))
    suma2 += num
    x2 += 1

# determinar cual tiene un mayor valor acumulado
if suma1 > suma2:
    print('La lista 1 tiene un mayor valor acumulado')
else:
    if suma2 > suma1:
        print('La lista 2 tiene un mayor valor acumulado')
    else:
        print('Las listas son iguales')