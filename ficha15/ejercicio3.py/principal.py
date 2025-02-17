"""
3 - Búsqueda de primos
Desarrollar un programa que permita generar un arreglo de n elementos, a partir del arreglo:
• Generar un segundo vector con todos aquellos números primos
• Determinar el promedio del vector generado en el punto 1
"""
import modulo

def validar(min):
    num = min
    while num <= min:
        num = int(input('Ingrese un número mayor a ' + str(min) + ': '))
        if num <= min:
            print('Error!!...Ingrese un número mayor a ' + str(min))
    return num


def main():
    n = validar(0)
    v = [0] * n

    # carga de numeros
    modulo.cargar_arreglo(v)
    
    # vector con numeros primos
    primos = modulo.vector_primo(v)
    
    # promedio 
    prom = modulo.primos_promedio(primos)

    # salida por pantalla
    print('La lista original es ', v)
    print('La lista con los vectores primos es ', primos)
    print('El promedio de los números primos de la lista generada es ', prom)


if __name__== '__main__':
    main()