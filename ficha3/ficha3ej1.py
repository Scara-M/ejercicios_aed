"""
-- Fecha como cadena --
Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en
formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es
'16/03/2016' el programa debe mostrar: 'Día: 16 - Mes: 03 - Año: 2016'.
"""

# cargar fecha por teclado
fecha = input('Cargar fecha con el formato dd/mm/aaaa: ')


# separar por dia - mes - año
dd, mm, aaaa = fecha[0] + fecha[1], fecha[3] + fecha[4], fecha[6] + fecha[7] + fecha[8] + fecha[9]


# Salida por pantalla
print('Día:', dd, '- Mes:', mm, '- Año:', aaaa)