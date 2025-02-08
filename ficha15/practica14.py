"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
Mostrar el nombre de persona menor en orden alfabético.
"""
nombres = []

# carga de nombres
for x in range(5):
    nom = input('Ingresar el nombre: ')
    nombres.append(nom)

# identicar el menor
menor = nombres[0]
for x in range(1,5):
    if nombres[x] < menor:
        menor = nombres[x]


# salida por pantalla
print('El nombre de la persona en menor orden alfabetico es ', menor)