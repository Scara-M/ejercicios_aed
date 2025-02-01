"""
-- Ejercicio Estadística de Guardería Náutica--
Un club náutico de la costa del lago San Roque necesita calcular estadísticas acerca de los barcos que tiene en la guardería.
Se pretende un programa que cargue uno por uno los datos de cada barco. 
De ellos se sabe el nombre, el tipo (1 si es velero, 2 si es lancha) y el monto que pagan por mes de guardería.

El programa debe cargar datos de los barcos de acuerdo a una cantidad n que se carga al comienzo y una vez completada la carga informar:
1. El total anual aportado por los veleros y el total anual aportado por las lanchas (2 totales).
2. El nombre del velero que mayor cuota mensual paga de guardería y el valor de su cuota mensual.
3. El valor promedio de cuota pagada por las embarcaciones de la guardería teniendo en cuenta todas las embarcaciones
independientemente del tipo que tengan.
4. El porcentaje que representa el monto mensual recaudado por los veleros sobre el total mensual recaudado y el porcentaje que
representa el monto mensual recaudado por las lanchas sobre el total mensual recaudado (2 porcentajes).
"""
# inicializar variables
acum_anual_v = acum_anual_l = 0

n = int(input('Ingresar la cantidad de barcos a procesar: '))

for i in range(n):
    nom = input('Ingresa el nombre del barco: ')
    tipo = int(input('1.Velero o 2.Lancha: '))
    monto = int(input('Ingresar el monto mensual: '))

    # total aportado por tipo de barco
    
    if tipo == 1:
        acum_anual_v += monto
    else:
        acum_anual_l += monto
    
    # velero con mayor pago mensual
    
    if i == 0:
        nom_mayor = nom
        cuota_mayor = monto
    elif i > 0:
        if monto > cuota_mayor:
            nom_mayor = nom
            cuota_mayor = monto
    
# monto total recaudado
monto_total = acum_anual_l + acum_anual_v

# promedio de las cuotas totales
if n != 0:
    promedio = (monto_total)/n
else:
    promedio = 0

# porcentajes por tipo de barco
porc_velero = acum_anual_v // monto_total * 100
porc_lancha = acum_anual_l // monto_total * 100

# Salida por pantalla
print('El total anual aportado por los veleros es de $', acum_anual_v)
print('El total anual aportado por las lanchas es de $', acum_anual_l)
print('El nombre del mayor con mayor pago mensual es ', nom_mayor, ' con $', cuota_mayor)
print('El valor de la cuota promedio es de $', promedio)
print('El monto recaudado por los veleros es del ', porc_velero, ' %')
print('El monto recaudado por las lanchas es del ', porc_lancha, ' %')