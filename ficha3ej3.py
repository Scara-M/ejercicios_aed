"""
--Duración de un vuelo--
Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), determine
cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha
reservado, ¿a qué hora llegara al mismo?
"""
# carga por teclado
partida = input('Ingresar el horario de partida en formato hh:mm: ')
llegada = input('Ingresar el horario de llegada en formato hh:mm: ')

# partida
hh_partida = int(partida[0] + partida[1])
mm_partida = int(partida[3] + partida[4])

# llegada
hh_llegada = int(llegada[0] + llegada[1])
mm_llegada = int(llegada[3] + llegada[4])

################################################
# convertir las hh a mm
minutos_partida = hh_partida * 60 + mm_partida
minutos_llegada = hh_llegada * 60 + mm_llegada

# Vuelo en minutos
vuelo_mm =  minutos_llegada - minutos_partida

# convertir la hora de llegada al hotel al formato hh:mm
hh_llegada_hotel = (minutos_llegada + 45) // 60
mm_llegada_hotel = (minutos_llegada + 45) % 60

# Salida por pantalla
print('La duración del viaje es de ', vuelo_mm, 'minutos')
print('Llega al hotel a las ' + str(hh_llegada_hotel) + ':' + str(mm_llegada_hotel))