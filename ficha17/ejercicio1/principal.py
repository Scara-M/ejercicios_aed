"""
1 - Estudio climatológico
Como parte de un estudio climatológico, se desea un programa que permita obtener una serie de
estadísticas a partir de un conjunto de muestras de temperatura.
Se pide un programa que:
• Ingrese n muestras de temperatura, donde cada muestra contiene la temperatura registrada, la
región donde se registró la misma (1-20), y el día del mes en el que se registró la temperatura.
• Determinar el promedio general de temperatura
• Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor
• Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado
por teclado.
• Determinar la cantidad de muestras por region (20 contadores)
"""
import modulo

def main():
    n = modulo.validar(0, 'Ingrese cantidad de muestras a procesar: ')
    temperaturas = [0] * n
    regiones = [0] * n
    dias = [0] * n
    
    # carga de arreglos
    modulo.cargar_arreglo(temperaturas,regiones,dias)
    print(temperaturas)
    print(regiones)
    print(dias)

    # determinar_promedio
    prom = modulo.promedio_general(temperaturas)
    print('El promedio es ', round(prom,2))
    
    # orden
    r = modulo.validar_rango(1,20,'Ingrese región a analizar (1 y 20): ')
    modulo.ordenar_ascendente(temperaturas,regiones, dias)
    modulo.mostrar_vector(temperaturas,regiones,dias,r)
    
    # temperatura muestra supero a x
    x = float(input('Ingrese un valor de la temperatura'))
    reg = modulo.validar_rango(0,3, 'Ingrese una región a analizar: ')
    r = modulo.buscar_temperatura(temperaturas,regiones,reg,x)
    if r == 1:
        print('Se encontró una temperatura que supera al valor ingresado')
    else:
        print('No se encontró una temperatura al valor ingresado')
    
    # determinar muestras por región
    modulo.contar(temperaturas, regiones)
    

if __name__ == '__main__':
    main()
