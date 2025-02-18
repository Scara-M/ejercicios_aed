"""
2 - Alumnos
Ingresar (o generar de manera aleatoria) los legajos de los n alumnos de un curso, siendo n un
valor que se carga por teclado, y almacenarlos en un arreglo unidimensional. Se pide para ello:
• Ordenar el arreglo de menor a mayor. Mostrar por pantalla como quedó.
• Buscar en el arreglo el alumno con el legajo x, x se ingresa por teclado. Si existe mostrarlo, si no
mostrar un mensaje de error.
"""
import modulo

def validar(min):
    num = min
    while num <= min:
        num = int(input('Ingresar un valor mayor a ' + str(min) + ': '))
        if num <= min:
            print('Error!! ... Ingresar un valor mayor a ' + str(min))
    return num


def main():
    n = validar(0)
    legajos = [0] * n

    # cargar legajos
    modulo.cargar_arreglo(legajos)
    print('Legajos cargados', legajos)

    # ordenar ascendente
    modulo.ordenar_arreglo(legajos)
    print('Legajos orden ascendente ', legajos)

    # busqueda binara
    x = int(input('Ingresar legajo del alumno: '))
    busq = modulo.binary_seach(legajos, x)
    if busq != -1:
        print('El legajo se encontró')
    else:
        print('Error! El legajo no se encontró')


if __name__=='__main__':
    main()