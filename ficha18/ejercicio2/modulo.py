import random

def cargar_datos(di,de,mon):
    descripciones = ['carne', 'vinos', 'gaseosas', 'aceites', 'galletitas']
    n = len(di)
    for i in range(n):
        di[i] = random.randint(1,31)
        de[i] = random.choice(descripciones)
        mon[i] = round(random.uniform(100,10000),2)


def calcular_promedio(suma,cant):
    prom = 0
    if cant != 0:
        prom = round(suma / cant,2)
    return prom


def promedio_mensual(vec):
    acu = 0
    cant = len(vec)
    for i in range(len(vec)):
        acu += vec[i]
        
    prom = calcular_promedio(acu,cant)
    return prom


def ordenar_envios(env,imp):
    n = len(env)

    for k in range(n-1):
        for x in range(k+1,n):
            if imp[k] < imp[x]:
                imp[k], imp[x] = imp[x], imp[k]
                env[k], env[x] = env[x], env[k]

    for i in range(n):
        print('Envio realizado: ', env[i], 'Monto: ', imp[i])


def contar(dias):
    cant = [0] * 31
    for x in dias:
        cant[x-1] += 1
    return cant


def buscar_mayor(dias):
    x_dia = contar(dias)
    mayor = mayor_dia = 0
    for i in range(len(x_dia)):
        if x_dia[i] > mayor:
            mayor = x_dia[i]
            mayor_dia = i
    return mayor_dia + 1, mayor