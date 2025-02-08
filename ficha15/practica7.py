"""
Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. 
Imprimir la lista generada.
"""
lista = []

# carga de elementos
for x in range(5):
    num = int(input('Ingrese un número: '))
    lista.append(num)

# salida
print(lista)