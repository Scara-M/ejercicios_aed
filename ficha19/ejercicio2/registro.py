class AnalisisTermico:
    def __init__(self, reg, mes, maxima, minima):
        self.region = reg
        self.mes = mes
        self.t_maxima = maxima
        self.t_minima = minima

def write(analizador):
    return 'Analizar Termico para: \n' \
    '\t\t La Region ' + analizador.region + '\n' \
    '\t\t Mes: ' + str(analizador.mes) + '\n' \
    '\t\t Maxima: ' + str(analizador.t_maxima) + '\n' \
    '\t\t Minima: ' + str(analizador.t_minima)

