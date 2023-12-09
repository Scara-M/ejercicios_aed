"""
--Cálculo de sueldo--
Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece.
Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y
un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:
Nombre Empleado: xxxxxxxxx          Nuevo Salario: $ xxx
Área Funcional: xxxxxxxxxxxx
Salario Actual: $ xxxx
"""

# Datos del empleado por teclado
nombre = input('Ingresar el nombre del empleado: ')
salario = float(input('Ingresar el salario del empleado: '))
area = input('Ingresa el área funcional del empleado: ')

# Calculo de porcentajes y nuevo salario
aumento = salario * 0.08
descuento = salario * 0.025
salario_actualizado = salario + aumento - descuento

# Salida por pantalla
print('Nombre Empleado: ', nombre, '\tNuevo Salario: $',salario_actualizado)
print('Área Funcional: ', area)
print('Salario Actual: $', salario)

