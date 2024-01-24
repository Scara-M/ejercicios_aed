"""
--Observatorio meteorológico--
Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día. Se solicita el
desarrollo de un programa que facilite información estadísticas de ellas.

El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).
Los requerimientos funcionales son:
a) Promedio de temperatura diaria.
b) Temperatura máxima.
c) Temperatura mínima.
d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio
"""

t_mayor_prom = False
print(" ")


# Ingreso de temperaturas
t1 = int(input('Ingresar la primer temperatura registrada: '))
t2 = int(input('Ingresar la segunda temperatura registrada: '))
t3 = int(input('Ingresar la tercer temperatura registrada: '))
t4 = int(input('Ingresar la cuarta temperatura registrada: '))
print(" ")


# Temperatura promedio
t_prom = (t1 + t2 + t3 + t4)//4


# temperatura maxima
if t1 > t2 and t1 > t3 and t1 > t4:
    t_max = t1
elif t2 > t3 and t2 > t4:
    t_max = t2
elif t3 > t4:
    t_max = t3
else:
    t_max = t4


# temperatura minima
if t1 < t2 and t1 < t3 and t1 < t4:
    t_min = t1
elif t2 < t3 and t2 < t4:
    t_min = t2
elif t3 < t4:
    t_min = t3
else:
    t_min = t4


# algunas de las temperaturas supera a la temperatura promedio
if t1 > t_prom or t2 > t_prom or t3 > t_prom or t4 > t_prom:
    t_mayor_prom = True


# Salida por pantalla 
print('El promedio de las temperaturas diarias es ', t_prom)
print('La temperatura máxima es de ', t_max)
print('La temperatura mínima es de ', t_min)

if t_mayor_prom:
    print('Alguna de las temperaturas supera al promedio')
else:
    print('Ninguna de las temperaturas supera al promedio')