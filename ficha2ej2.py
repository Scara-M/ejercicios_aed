"""
-- Descuento en medicinas --
Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar por teclado el
precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%. Mostrar el precio
actual, el monto del descuento y el monto final a pagar.
"""

# carga de datos
precio = float(input('Ingresar precio del medicamento: '))

# calcular con descuento
monto_descuento = precio * 0.35
monto_final = precio - monto_descuento

# salida
print('El precio del medicamento es de: ', precio)
print('El precio del descuento es de: ', monto_descuento)
print('El monto final es de: ', monto_final)