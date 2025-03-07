def validar(min,mensaje):
    num = min
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('Error!!.. El valor ingresado debe ser mayor a ' + str(min))
    return num


def validar_entre(min,max, mensaje):
    num = min - 1
    while num < min or num > max:
        num = int(input(mensaje))
        if num < min or num > max:
            print('Error!!.. El valor ingresado debe estar entre ' + str(min) +  ' y' + str(max))
    return num

