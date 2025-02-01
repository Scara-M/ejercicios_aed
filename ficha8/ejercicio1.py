"""
1 - Menú de opciones con secuencias
Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes
operaciones:
• Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y
mostrar la suma de los cuadrados
• Ingresar un texto finalizado por un punto y determinar la canƟdad de palabras que finalizan con
vocales
• Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor canƟdad de
valores pares o de impares
• Salir
"""

# menu
menu = ('1 - Mostrar la suma de cuadrados \n'\
        '2 - Mostrar la suma de cuadrados \n'\
        '3 - Mostrar la suma de cuadrados \n'\
        '4 - Mostrar la suma de cuadrados ')

# proceso
opcion = 0
while opcion != 4:
    print(menu)
    opcion = int(input('Ingrese una opción: '))

    # opcion 1
    if opcion == 1:
        n = 0
        suma = 0
        # valida que sea mayor a cero
        while n <= 0:
            n = int(input('Ingrese un número: '))
            if n <= 0:
                print('Error! El numero debe ser mayor a cero')
        for valor in range(1,n+1):
            suma += valor ** 2
        print('La suma de los cuadrados del 1 al', n, 'es', suma)
    
    # opcion 2
    elif opcion == 2:
        frase = input('Ingrese un texto: ').lower

        for car in frase:
            if car != '.' and car != ' ':
                pass
            else:
                pass
    # opcion 3
    elif opcion == 3:
        pass
    else:
        print('ADIOSSSSSSSSSSSSSSSS')