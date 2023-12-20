"""
--Edad mínima--
Ingresar por teclado las edades de 3 participantes de un concurso.
Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.
"""
# Ingreso de edades
edad1 = int(input('Ingresar la edad del primer participante: '))
edad2 = int(input('Ingresar la edad del segundo participante: '))
edad3 = int(input('Ingresar la edad del tercer participante: '))
minima = int(input('Ingresar la edad mínima para participar: '))

# Verificar las edades
if edad1 >= minima and edad2 >= minima and edad3 >= minima:
    print('Todos los participantes cumplen con la edad mínima')
else:
    print('No todos los participantes cumplen con la edad mínima') 