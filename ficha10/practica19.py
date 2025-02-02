"""
Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
"""
def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo = costohora * cantidadhoras
    print(nombre, 'trabajó', cantidadhoras, ' y cobra un sueldo de ', sueldo)

# bloque principal
calcular_sueldo('Juan', 10, 120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre='ana')
calcular_sueldo(cantidadhoras=90,nombre='luis',costohora=7)
calcular_sueldo(costohora=15,nombre='luis',cantidadhoras=8)