import random
#random.seed(42)

def validar(min,mensaje):
    num = min
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('Error!!! Vuelva a ingresar un valor mayor a ' + str(min))
    return num


def validar_rango(min,max,mensaje):
    num = min - 1
    while num < min or num > max:
        num = int(input(mensaje))
        if num < min or num > max:
            print('Error!!. Vuelva a ingresar un valor entre ' + str(min) + ' y ' + str(max))
    return num


def cargar_arreglo(temp,reg,dias):
    n = len(temp)
    for i in range(n):
        #print('--- Muestra ---' , i)
        temp[i] = round(random.uniform(10,45), 2)
        #reg[i] = validar_rango(1,20,'Ingrese la regíon (entre 1 y 20): ')
        #dias[i] = validar_rango(1,31, 'Ingrese día del mes: ')
        reg[i] = random.randint(1,20)
        dias[i] = random.randint(1,31)

def calcular_promedio(suma,cant):
    prom = 0
    if cant != 0:
        prom = suma / cant
    return prom


def promedio_general(vec):
    acu = 0
    for elem in vec:
        acu += elem   
    prom = calcular_promedio(acu, len(vec))
    return prom


def ordenar_ascendente(vec1,vec2,vec3):
    n = len(vec1)
    for k in range(n-1):
        for x in range(k+1,n):
            if vec3[k] > vec3[x]:
                vec1[k],vec1[x] = vec1[x], vec1[k]
                vec2[k],vec2[x] = vec2[x], vec2[k]
                vec3[k],vec3[x] = vec3[x], vec3[k]


def mostrar_vector(vec1,vec2,vec3,r):
    n = len(vec1)
    for i in range(n):
        if vec2[i] == r:
            print('Region: ', vec2[i], ' Temperatura: ', vec1[i], ' Dia: ', vec3[i])


def buscar_temperatura(temp,reg,r,x):
    encontro = 0
    for i in range(len(temp)):
        if reg[i] == r and temp[i] > x:
            encontro = 1
    return encontro


def contar(temp,reg):
    cont = [0] * 20
    for i in range(len(temp)):
        cont[reg[i]-1] += 1

    for i in range(len(cont)):
        print('Region: ', i, ' Cantidad: ', cont[i])
    