"""
1 - Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del
país, en base a esos datos armar un menú de opciones que permita:
Determinar el promedio anual de lluvias
Determinar el promedio de lluvias para un determinado trimestre
Determinar el mes más seco del año
"""
import modulo


def main():
    lluvias = [0] * 12
    # carga las lluvias
    modulo.cargar_vector(lluvias)
    prom_anual = modulo.sumar_lluvias(lluvias,12)

    # promedio por trimestre
    prom_tri = modulo.determinar_prom_trimestre(lluvias)

    # mes mas seco del añi
    menor = modulo.busqueda_mas_seco(lluvias)

    # salida por pantalla   
    print(lluvias)
    print('El promedio anual de lluvias es ', prom_anual)
    print('El promedio del trimestre es ', prom_tri )
    print('El mes más seco fue el mes ', menor[1], 'con una precipitacion de ', menor[0])

if __name__=='__main__':
    main()