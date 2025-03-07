class Concursante:
    # se inicializan los campos
    def __init__(self, dni, nom, cargo, puntaje):
        self.dni = dni
        self.nombre = nom
        self.cargo = cargo
        self.puntaje = puntaje
    
    # metodo str
    def __str__(self):
        s = 'DNI: ' + str(self.dni)
        s += '| Nombre: ' + str(self.nombre)
        s += '| Cargo: ' + str(self.cargo)
        s += '| Puntaje: ' + str(self.puntaje)
        return s
    