"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
"""
nombres = []
edades = []

# carga de elementos
for x in range(5):
    nom = input('Ingresar el nombre: ')
    nombres.append(nom)
    edad = int(input('Ingresar la edad: '))
    edades.append(edad)

# identificar las mayores de edad
for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])