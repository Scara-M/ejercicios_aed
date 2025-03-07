class Articulo:
    def __init__(self,codigo, nombre, precio, stock_actual, stock_ideal):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock_actual = stock_actual
        self.stock_ideal = stock_ideal

    def __str__(self):
        cad = '{} | {} | {} | {} | {} |'
        return cad.format(self.codigo, self.nombre, self.precio, self.stock_actual,self.stock_ideal)
        
