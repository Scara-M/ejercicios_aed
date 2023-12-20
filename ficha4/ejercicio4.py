"""
--Temperatura diaria--
Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de
un día y determinar:
Cual es el promedio de las temperaturas.
Si existe alguna temperatura que sea mayor al promedio
"""

# carga de temperaturas
t1 = float(input('Ingresar primera temperatura: '))
t2 = float(input('Ingresar segunda temperatura: '))
t3 = float(input('Ingresar tercera temperatura: '))


# determinar el promedio
promedio = (t1 + t2 + t3)/3
redondeado = round(promedio,2)

# temperatura mayor al promedio
print('El promedio de las temperaturas ingresadas es ', redondeado)

if t1 > promedio or t2 > promedio or t3 > promedio:
    print('Existe alguna temperatura ingresada que supera al promedio')
else:
    print('No existe alguna temperatura ingresada que supera al promedio')