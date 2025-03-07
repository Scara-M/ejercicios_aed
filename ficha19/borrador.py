class Empleado:
    def __init__(self,leg,nom):
        self.legajo = leg
        self.nombre = nom
        
    # metodo str
    def __str__(self):
        return 'legajo: ' + str(self.legajo) + ", nombre: " + str(self.nombre)


e1 = Empleado(68296,'Mariano')
print(e1)
