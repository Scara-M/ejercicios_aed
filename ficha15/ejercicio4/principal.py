"""
4 - Mayores con el mismo índice
Cargar por teclado dos vectores de tamaño n y, a partir de ellos, generar un tercer vector que
contenga, para cada componente, el mayor valor entre las componentes homólogas (mismo índice) de los otros dos vectores.
Por ejemplo, si se cargan los siguientes vectores a y b:
a = [3, 4, 6]
b = [8, 5, 1]
El resultado sería:
c = [8, 5, 6]
"""
import modulo
def validar(min):
    num = min
    while num <= min:
        num = int(input('Ingrese un número mayor a ' + str(min) + ': ' ))
        if num <= min:
            print('Error!...Ingrese un número mayor a ' + str(min))
    return num

def main():
    n = validar(0)
    vec1 = n * [0]
    vec2 = n * [0]
    modulo.carga_vector(vec1)
    modulo.carga_vector(vec2)
    vec3 = modulo.determinar_mayor(vec1,vec2)
    print(vec1)
    print(vec2)
    print(vec3)

if __name__ == '__main__':
    main()