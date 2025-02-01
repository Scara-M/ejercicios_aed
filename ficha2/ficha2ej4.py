"""
 --Polinomio de segundo grado --
 Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado, y
calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado). Además, para el mismo
polinomio, calcule y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.
"""
# carga de coeficientes
a = int(input('Ingresar primer coeficiente: '))
b = int(input('Ingresar segundo coeficiente: '))
c = int(input('Ingresar tercer coeficiente: '))
x = int(input('Ingresar el valor de la variable: '))

# valor del polinomio en el punto x 
polinomio = a * (x ** 2) + b * x + c

# discriminante
discriminante = b ** 2 - 4 * a * c

# salida por pantalla
print('El valor del polinomio es: ', polinomio)
print('El valor del discriminante es: ', discriminante)

