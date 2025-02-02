"""
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
"""
def tabla(num, termino = 10):
    for x in range(termino):
        va = x * num
        print(va, ',',sep='',end='')
    print()

# bloque principal
print('Tabla del 3')
tabla(3)
print('Tabla del 8')
tabla(8)