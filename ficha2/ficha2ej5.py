"""
--Cálculo de ángulos--
Se sabe que la suma de dos ángulos desconocidos (alfa + beta) es igual a cierto valor x que se carga por teclado.
Además se sabe que la diferencia entre esos mismos dos ángulos (alfa - beta) es igual a otro valor y que también se
carga por teclado. 
Desarrolle un programa que dados los valores x e y, determine el valor de los dos ángulos alfa y
beta. No es necesario convertir a grados, minutos y segundos el valor de cada ángulo: expréselos como números
reales, tal cual hayan sido obtenidos.
"""

# carga de valores
x = float(input('Ingresar primer valor: '))
y= float(input('Ingresar segundo valor: '))

# operaciones
# x = a + b
# y = a - b

beta = (x - y)/2 
alfa = y + beta

# muestra por pantalla
print('El valor de alfa es: ', alfa)
print('El valor de beta es: ', beta)

 


