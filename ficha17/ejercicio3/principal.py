"""
3 - Ventas
Se pide cargar las n ventas del día de un comercio en 2 vectores. 
• De cada venta se conoce el articulo adquirido (son 4 tipos de articulos numerados del 0 al 3) 
y la cantidad vendida de dicho articulo en esa venta.
• Se debe calcular y mostrar la cantidad vendida de cada uno de los 4 articulos.
"""
import modulo

def main():
    n = modulo.validar(1, 'Ingrese ventas realizadas (valor mayor a cero): ')
    articulos = [0] * n
    cantidad = [0] * n

    # carga de arreglos
    modulo.cargar_arreglos(articulos,cantidad)
    
    # mostrar articulos
    modulo.mostrar_arreglos(articulos,cantidad)

    # Contar cantidad vendida de cada articulo
    modulo.contar(articulos,cantidad)
    
if __name__ == '__main__':
    main()