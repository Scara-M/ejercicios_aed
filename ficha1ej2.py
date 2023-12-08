"""
Cuadrado de un binomio
Un binomio al  cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el
segundo más el cuadrado del segundo.
Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b, el valor del
cuadrado del binomio.
"""

# carga por teclado
a = int(input('Ingresar primer valor: '))
b = int(input('Ingresar segundo valor: '))

# proceso
binomio = a ** 2 + 2 * a * b + b ** 2

# resultado
print('El binomio de los dos valores es: ', binomio)