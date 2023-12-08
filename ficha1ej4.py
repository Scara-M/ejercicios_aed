"""
Últimos dígitos
¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría
los dos últimos dígitos? 
Desarrolle un programa que cargue un número entero por teclado, y muestre el último
dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado) [Ayuda: ¿cuáles son los posibles restos que
se obtienen de dividir un número cualquiera por 10?]
"""

# carga por teclado
num = int(input('Ingrese un número de más de 2 cifras: '))

# obtencion de los ultimos digitos
ultimo_dig = num % 10
ultimo_2dig = num % 100

# salida por pantalla
print('El último dígito del valor ingresado es: ', ultimo_dig)
print('Los dos últimos dígitos del valor ingresado es: ', ultimo_2dig)