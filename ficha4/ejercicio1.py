"""
-- Generador de Dirección de Mail--
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección
de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:
Componer la dirección de correo de la siguiente manera:
<primera letra del nombre><apellido>@<dominio>
Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
<nombre>.<apellido>@<dominio>
"""

# Carga de datos
nombre = input('Ingresar nombre: ').lower()
apellido = input('Ingresar apellido: ').lower()
dominio = input('Ingresar el dominio: ').lower()


if nombre[0] != apellido[0]:
    mail = nombre[0] + apellido + '@' + dominio
else:
    mail = nombre + '.' + apellido + '@' + dominio


# Salida por pantalla
print('El correo generado es: ', mail)