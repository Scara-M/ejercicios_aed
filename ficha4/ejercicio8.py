"""
--Lanzamiento de dados--
Simular un juego en el que se lanzan dos dados.
Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.
"""
import random

print('LANZAMIENTO DE DADOS')
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

# Proceso
print('Dado 1: ', dado1)
print('Dado 2: ', dado2)
print('La suma de los dados es ', suma)
if dado1 == dado2 or (suma % 2) != 0:
    print('GANÓ EL USUARIO')
else:
    print('PERDIÓ EL USUARIO. Ganó la máquina')