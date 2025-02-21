"""
2 - Empresa de transporte
Una empresa dedicada al transporte de mercadería solicita un programa para manejar estadísticas
de sus envios. Para ello solicita un programa, controlado por menú con opciones para lo siguiente:
Ingresar los datos de los transportes realizados en el mes, de cada uno se conoce:
• Día del mes (1-31)
• Descripción
• Monto del transporte
---- Determinar el monto promedio obtenido en el mes
---- Genere un listado de los envíos realizados, ordenado por importe en forma decreciente
---- Determine que día del mes tuvo mayor cantidad de transportes realizados
"""
import modulo

def validar(min,mensaje):
    num = min
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('Error! El valor debe ser mayor a ' + str(min))
    return num


def main():
    op = -1
    while op != 4:
        n = validar(-1, '---- Ingrese la cantidad de transportes realizados: ')
        dias = [0] * n
        descripciones = [''] * n
        montos = [0.0] * n
        modulo.cargar_datos(dias,descripciones,montos)
        print(dias)
        print(descripciones)
        print(montos)
        print(' ')

        op = int(input('Elija su opción: '))
        # punto 1
        if op == 1:
            prom = modulo.promedio_mensual(montos)
            print('El promedio general es ', prom)
        
        # punto 2
        elif op == 2:
            modulo.ordenar_envios(descripciones,montos)

        # punto 3
        elif op == 3:
            mayor, cantidad = modulo.buscar_mayor(dias)
            print('El dia de mayor cantidad de transportes fue ', mayor)
            print('Con un total de ', cantidad, ' transportes realizados')
        
        # punto 4
        elif op == 4:
            print('Adiossss')
        
        # error
        else:
            print('Opción incorrecta!! Vuelva a ingresar')


if __name__=='__main__':
    main()