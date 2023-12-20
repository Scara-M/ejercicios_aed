"""
 -- Área de un triángulo --
Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero
sabiendo que su altura es igual al cuadrado de la base. (Observar que la altura no es un dato... sólo se indica la
forma de calcularla de acuerdo a la base que sí es un dato).
"""

# cargar por teclado
base = int(input('Ingresar la base del triángulo: '))

# operacion
altura = base ** 2
area = (base * altura) / 2

# area del triangulo
print('El área del triángulo es: ', area)