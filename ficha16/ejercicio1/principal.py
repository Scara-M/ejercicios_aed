"""
1 - Ordenar y buscar
Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive (pueden
existir duplicados). A partir de ese arreglo:
• Ordenarlo de forma ascendente y mostrarlo
• Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si
existe, determinar cuántos valores impares mayores a x se encontraron en el arreglo.
"""
import modulo

def validar(min):
    num = min
    while num <= min:
        num = int(input('Ingrese un número mayor a ' + str(min) + ': '))
        if num <= min:
            print('Error!! ... Ingrese un número mayor a ' + str(min))
    return num


def main():
    n = validar(0)
    v = [0] * n

    # carga aleatoria
    modulo.carga_aleatoria(v)
    print(v)

    # orden ascendente
    modulo.ordenar_vector(v)
    print('---- Orden ascendente --- ', v)


    # busqueda binaria
    x = int(input('Ingrese número a buscar: '))
    busq = modulo.search_binary(v,x)
    if busq != -1:
        print('Se encontró en en arreglo')
    else:
        print('No se encontro en el arreglo')

    # valores impares mayores a x
    cant = modulo.busqueda_impares(v,x)
    print('La cantidad de valores impares mayores a x son ', cant)

    
if __name__=='__main__':
    main()