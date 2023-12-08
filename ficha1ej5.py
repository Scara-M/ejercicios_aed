"""
--  Conversión de medidas --
Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
yardas
pulgadas
centímetros
metros
Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.
"""

# ingresar medida en pies
medida_pies = float(input('Ingresar medida en pies: '))

# conversion a yardas
medida_yarda = medida_pies / 3

# conversion a pulgadas
medida_plg = medida_pies * 12

# conversion a cm
medida_cm = medida_plg * 2.54

# conversion a metros
medida_m = medida_cm / 100

# salida por resultado
print('La medida ingresada en pies es: ', medida_pies)
print('La conversión a yardas es: ', medida_yarda)
print('La conversión a pulgadas es: ', medida_plg)
print('La conversión a centimetros es: ', medida_cm)
print('La conversión a metros es: ', medida_m)
