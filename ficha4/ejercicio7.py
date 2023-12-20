"""
--Tirada de moneda--
Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a
cara o cruz y luego informar si acertó o no con su apuesta.
"""
import random

jugador = input('Elija cara o cruz para jugar: ')
lado = 'cara', 'cruz'

# Definir tirada y ver si acerto el jugador
tirada = random.choice(lado)

print('La tirada fue ', tirada)
if jugador == tirada:
    print('El jugador acertó')
else:
    print('El jugador no acertó')
