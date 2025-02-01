"""
--Censo--
Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para
sexo.
El programa debe informar:
a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
c) Si hay algún varón que supere los 80 años de edad
"""
# inicializador de variables
cantf = cantm = 0
cant_escolar = 0
varon80 = False

# proceso
sexo = input('Ingrese el sexo (Finalice con otra letra): ').lower()
while sexo == 'm' or sexo == 'f':
    edad = int(input('Ingrese la edad: '))

    # contar sexos
    if sexo == 'm':
        cantm += 1
        if edad > 80:
            varon80 = True
    else:
        cantf += 1
        if edad >= 4 and edad <= 18:
            cant_escolar += 1

    # carga doble lectura
    sexo = input('Ingrese el sexo (Finalice con otra letra): ').lower()

# sexo con mayor cant de hab
if cantf > cantm:
    print('El sexo con mayor cantidad de habitantes es el femenino')
else:
    if cantm > cantf:
        print('El sexo con mayor cantidad de habitantes es el masculino')
    else:
        print('Los sexos tienen la misma cantidad de habitantes')

# mujeres en edad escolar
print('La cantidad de mujeres en edad escolar es de ', cant_escolar)

# varon mayor de 80 años
if varon80 == True:
    print('Hay al menos un varon de más de 80 años')