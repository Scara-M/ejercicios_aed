"""
--Importe como cadena--
Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma
flotante y muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer precedida por el signo
'$' y en el otro debe aparecer precedida por la palabra "pesos". 
"""

# carga por teclado
importe = float(input('Ingresar cantidad de dinero: '))

# proceso
r1 = '$ ' + str(importe)
r2 = str(importe) + ' pesos'

# Salida por pantalla
print(r1)
print(r2)