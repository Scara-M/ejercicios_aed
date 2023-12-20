"""
-- Costos del Proyecto--
Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene un
presupuesto de x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17%
por el proyecto, determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.
"""

# cargar por teclado el presupuesto
presupuesto = int(input('Ingresar por teclado el presupuesto a gastar: '))

# determinar el porcentaje
gastos = presupuesto * 0.17
gastos_maximos = presupuesto - gastos

# Salida por pantalla
print('El presupuesto del proyecto es: ', presupuesto)
print('El porcentaje a gastar es de ', gastos)
print('El gasto máximo por el proyecto es ', gastos_maximos)