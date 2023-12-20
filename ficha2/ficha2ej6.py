"""
-- Precio de venta --
Conociendo el precio de lista de un artículo, determinar:
• Precio de venta al contado (10% de descuento)
• Precio de venta con tarjeta (5% de recargo)
"""

# carga por teclado
precio = float(input('Ingresar precio del artículo: '))

# precio al contado
descuento = precio * 0.1
precio_contado = precio - descuento

# precio con tarjeta
recargo = precio * 0.05
precio_recargo = precio + recargo

# Salida por pantalla
print('El precio de venta al contado es de: ', precio_contado)
print('El precio de venta con tarjeta: ', precio_recargo)