"""
--13. Triángulo Rectángulo--
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:
Valor de la hipotenusa (redondeado a 2 decimales)
Valor del lado mayor
Valor del lado menor
"""

# Ingreso de datos
print('*'*45)
print('Ingrese los datos del triángulo')
cat1 = int(input('Ingresar el valor del primer cateto: '))
cat2 = int(input('Ingresar el valor del segundo cateto: '))

# determina el lado mayor y menor
cat_mayor = max(cat1,cat2)
cat_menor = min(cat1, cat2)

# determina la hipotenusa
hip = (cat1 + cat2) // 2

# salida por pantalla
print('*'*45)
print('Los valores son:\n Lado menor: ', cat_menor, '\n Lado Mayor: ', cat_mayor)
print('El valor de la hipotenusa es ', hip)

