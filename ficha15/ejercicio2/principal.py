"""
2 - ÚlƟmo y primero
Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:
Informe cuántas veces se repite en el vector el último número ingresado
Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.
"""
import modulo

def validar(min):
    num = min
    while num <= min:
        num = int(input('Ingrese un número mayor a ' + str(min) + ': '))
        if num <= min:
            print('Erro!!..Ingrese un número mayor a ' + str(min))
    return num


def main():
    n = validar(0)
    vec = [0] * n
    # carga vector
    modulo.carga_vector(vec)

    # cant ultimo elemento
    cant = modulo.contar_ultimo_elemento(vec)
    
    # menores al primer elemento
    v = modulo.menores_primero(vec)

    # salida por pantalla
    print('La lista es ', vec)
    print('La cantidad de veces que se repite el último número es ', cant)
    print('El vector con los elementos menores al primer elemento de la original es ', v)

if __name__ == '__main__':
    main()