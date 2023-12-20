"""
--Votación en el Congreso--
En el Congreso se vota la sanción de una ley muy importante. 
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.
"""

# carga de votos
votos_favor = int(input('Ingresar la cantidad de votos a favor: '))
votos_contra = int(input('Ingresar la cantidad de votos en contra: '))

# proceso
total = votos_favor + votos_contra

porc_favor = (votos_favor/total) * 100
porc_contra = (votos_contra/total) * 100

# Salida
print('El porcentaje de votos a favor es: ', porc_favor)
print('El porcentaje de votos en contra es: ', porc_contra)