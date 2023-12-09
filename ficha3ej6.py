"""
--Cálculo presupuestario--
En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital
se reparte de la siguiente manera:
Área Presupuesto
Urgencias 37%
Pediatría 42%
Traumatología 21%
Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.
"""

# carga del presupuesto total
presupuesto = int(input('Ingresar el presupuesto total del hospital: '))

# Presupuesto por area
pres_urgencias = presupuesto * 0.37
pres_pediatria = presupuesto * 0.42
pres_traumatologia = presupuesto * 0.21

# Salida por pantalla
print('El presupuesto total es de $', presupuesto)
print('El presupuesto para Urgencias es $', pres_urgencias)
print('El presupuesto para Pediatría es $', pres_pediatria)
print('El presupuesto para Traumatología es $', pres_traumatologia)
