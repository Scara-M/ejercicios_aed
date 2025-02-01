"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""
# entrada de datos
n = int(input('Ingresar la cantidad de empleados: '))
x = 1
cant_100_300 = 0
cant_300 = 0
importe = 0

# proceso
print('-'*45)
while x <= n:
    sueldo = float(input('Ingresar sueldo del empleado: '))
    if sueldo >= 100 and sueldo <= 300:
        cant_100_300 += 1
    else:
        if sueldo > 300:
            cant_300 += 1
    importe += sueldo
    x += 1

# salida por pantalla
print('La cantidad de empleados que cobran entre $100 y $300 es: ', cant_100_300)
print('La cantidad de empleados que cobran más de $300 es ', cant_300)
print('El importe que gasta la empresa en sueldos es de $ ', importe)