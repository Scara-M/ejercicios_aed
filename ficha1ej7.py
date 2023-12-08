"""
--Precio del boleto
Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo del mismo se debe
considerar el monto base (que se cobra siempre), más un valor extra calculado en base a la cantidad de kilómetros
a recorrer: Por cada kilómetro a recorrer se cobra $0.30 de adicional.
"""

# Carga de datos
monto = float(input('Ingresar el monto base del viaje: '))
distancia = int(input('Ingresar la distancia en km del viaje: '))

# operaciones
adicional = distancia * 0.3
monto_total = monto + adicional

# resultado
print('El precio final del viaje es de: ', monto_total)