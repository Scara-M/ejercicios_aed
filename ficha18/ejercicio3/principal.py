"""
3 - Multas de tránsito
Se necesita desarrollar un script que permita procesar las n multas de tránsito labradas el último
fin de semana en las rutas de la provincia. 
Para ello se pide cargar un arreglo con los n códigos de infracción, valores comprendidos en [1:20], 
junto con los importes en pesos de los cinco tipos de infracciones, tal como se indica en la siguiente tabla:
    Código         Tipo de infracción
1, 6, 11, 16            1
2, 7, 12, 17            2
3, 8, 13, 18            3
4, 9, 14, 19            4
5, 10, 15, 20           0
Con los datos cargados en los arreglos se pide:
• Generar un tercer vector con los importes totales facturados por tipo de infracción
• Determinar el código de infracción que más apareció en las multas y la cantidad de multas labradas para dicho código.
• Informar el importe total facturado durante el fin de semana.
"""
def validar(min,mensaje):
    num = min
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('-- Error!...El valor debe ser mayor a ' + str(min))
    return num


def main():
    op = -1
    while op != 5:
        op = int(input('-- Elija su opción: '))

        # punto 1
        if op == 1:
            print('Carga de datos')
            n = validar(0, '----- Ingrese la cantidad de multas a procesar: ')
            codigos = [0] * n
            importes = [0] * 5
            
        # punto 2
        elif op == 2:
            print('Punto 2')
        
        # punto 3
        elif op == 3:
            print('Punto 3')
        
        # punto 4
        elif op == 4:
            print('Punto 4')
        
        # punto 5
        elif op == 5:
            print('Adiossssss')

        else:
            print('Opción incorrecta. Vuelva a cargar!')

if __name__=='__main__':
    main()