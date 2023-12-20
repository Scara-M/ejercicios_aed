"""
--Jornal de un Operario--
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el
jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese
día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.

La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50
pesos la hora.
"""

# Carga por teclado
codigo = int(input('Ingrese el código de turno del operario (1-Diurno 2- Nocturno): '))
horas = int(input('Ingresar la cantidad de horas trabajadas por el operario: '))


if codigo == 1:
    jornal = horas * 35.5
else:
    jornal = horas * 40.6

# Salida por pantalla
print('El jornal del operario es: $', jornal)