from registro import *
import pickle
import random

def generar_archivo(fd):
    articulos = ['Alcohol','Gasa','Algodon','Jeringa','Aspirina',
                'Vitaminas','Dentifrico','Bicarbonato',
                'Amoxidal','Novalgina','Agua oxigenada','Pañales','Mamadera',
                'Chupete','Crema','Champú','Acondicionador']
    m = open('stock.dat','wb')
    for i in range(len(articulos)):
        precio = random.randrange(10,200)
        actual = random.randrange(20)
        ideal = random.randrange(20)
        pickle.dump(Articulo(i,articulos[i],precio,actual,ideal),m)
    m.close()


if __name__=='__main__':
    fd = 'stock.dat'
    generar_archivo(fd)
    print('Archivo ', fd, 'generado')