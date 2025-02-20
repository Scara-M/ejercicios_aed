"""
4 - Repaso de arreglos
Generar un programa que cargue un lote de números enteros y positivos y que a través de un
menú de opciones le permita al usuario
1. Obtener el promedio de los números comprendidos entre dos valores ingresados por el usuario
2. Obtener el menor número impar del lote
3. Imprimir todos los números múltiplos de un valor ingresado por el usuario separados por comas
"""
import modulo
def validar(min, mensaje):
    num = min
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('Error! Vuelva a cargar un valor mayor a ' + str(min))
    return num


def main():
    n = validar(0, 'Ingrese un valor mayor a cero: ')
    enteros = [0] * n
    modulo.cargar_arreglo(enteros)
    print('----- Lista generada ----- : ', enteros)

    op = -1
    while op != 4:
        op = int(input('Ingrese su opcion: '))

        # promedio comprendido
        if op == 1:
            num1 = validar(0, 'Ingrese entero positivo menor: ')
            num2 = validar(0, 'Ingrese entero positivo mayor: ')
            prom = modulo.promedio_comprendido(enteros,num1,num2)
            print('---- El promedio es ', round(prom,2))
        
        # menor numero impar
        elif op == 2:
            menor = modulo.menor_impar(enteros)
            print('---- El menor impar es ', menor)
        

        # imprimir múltiplos de un valor x ingresado por teclado
        elif op == 3:
            x = validar(0, 'Ingresar múltiplo mayor a cero: ')
            print(modulo.listar_multiplo(enteros,x))
        
        # salida del programa
        elif op == 4:
            print('Adiosss')
        else:
            print('Opcion incorrecta. Vuelva a cargar')

if __name__=='__main__':
    main()