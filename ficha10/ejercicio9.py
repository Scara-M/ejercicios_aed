"""
9 - Portal de empleo
Un conocido portal de empleo requiere un programa para validar las búsquedas que se cargan en
su página. Por cada búsqueda se requiere:
CUIT: validar que sea un texto compuesto por 13 números separados por guiones de la siguiente
manera: 00-00000000-0
Descripción de la búsqueda: un texto donde cada palabra se separa con un espacio y termina
con punto. Debe tener un máximo de 60 caracteres y un mínimo de 5 palabras. El porcentaje de
palabras que comienzan con mayúscula no debe ser mayor al 50 %.
Salario ofrecido: controlar que sea un valor mayor a 0
Si todos los datos son válidos, mostrar el aviso completo. En caso contrario, informar que no es
posible mostrarlo.
Para terminar, consultar al usuario si desea cargar otro aviso o salir del programa.
"""
def validar_cuit(cuit):
    valido = False
    digitos = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[11] == '-':
            for car in cuit:
                if car in '0123456789':
                    digitos += 1
            if digitos == 11:
                valido = True
            else:
                print('Todos los caracteres del cuit deben ser digitos')
        else:
            print('Los guiones del cuit deben estar en las posiciones 3 y 12')
    else:
        print('El cuit debe tener 13 caracteres')
    return valido


def validar_descripcion(texto):
    valida = False
    palabras = 0
    hay_mayusc_seguidas = False
    anterior = ''
    if len(texto) <= 60:
        for car in texto:
            if car == ' ' or car == '.':
                palabras += 1
            else:
                if (car >= 'A' and car <= 'Z') and (anterior >= 'A' and anterior <= 'Z'):
                    hay_mayusc_seguidas = True
            anterior = car

        if palabras >= 3:
            if hay_mayusc_seguidas == False:
                valida = True
            else:
                print('La descripción no puede tener dos mayúsculas seguidas')
        else:
            print('La cantidad de palabras debe ser mayor a 3')
    else:
        print('La longitud máxima son 60 caracteres')
    return valida


def validar_salario(salario):
    # valido = False (y se borra el else)
    if salario > 0:
        valido = True
    else:
        print('El salario debe ser un valor mayor que cero')
        valido = False
    return valido


def principal():
    print('Portal de empleo')
    rta = 'S'
    while rta == 'S':
        # Datos
        cuit = input('Ingrese cuit: ')
        descripcion = input('Ingrese descripción: ')
        salario = float(input('Ingrese salario: '))

        # Procesos
        cuit_valido = validar_cuit(cuit)
        desc_valida = validar_descripcion(descripcion)
        salario_valido =  validar_salario(salario)
        # Resultados
        print('-' * 45)
        if cuit_valido and desc_valida and salario_valido:
            print('El empleador ', cuit, 'busca: ')
            print(descripcion)
            print('Salario ofrecido $ ', salario)
        else:
            print('No se puede mostrar el aviso')
        print('-' * 45)
        # consultar al usuario
        rta = input('Desea cargar otro aviso (S/N): ')

principal()