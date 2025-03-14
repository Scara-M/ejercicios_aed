"""
1. Salón de Fiestas
Un salón dedicado a la organización de fiestas infantiles nos solicita un sistema para gestionar las reservas de un
mes determinado. De cada reserva de festejo se conoce:
• Número de reserva ( es un dato tipo String )
• Nombre del cumpleañero ( es un dato tipo String )
• Edad del cumpleañero (0 a 13 años) (es un dato tipo Integer)
• Tipo de servicio solicitado (0: salón - 1: salón y animación - 2: salón, animación y comida niños - 3: salón,
animación, comida niños y sorpresitas) (es un dato tipo Integer)
• Cantidad Invitados (es un dato tipo Integer)
• Monto (es un dato tipo Float)

Al iniciar el programa todas las reservas se encuentran almacenadas en un archivo de texto llamado reservas.csv
(el cual es provisto). Se debe cargar dicho archivo en un arreglo de registros de tipo Reserva. Una vez cargado,
programe los siguientes punto en un menu de opciones:

1. Mostrar el contenido del vector, incluyendo la descripción del tipo de servicio
2. Agregar una nueva reserva al arreglo de registro, con un número que se ingresa por teclado. Validar que dicho
numero de reserva sea único y solicitar el resto de los datos.
3. Determinar el monto total que el salon ha obtenido por tipo de servicio (vector de acumulacion). Mostrar los
resultados e informar qué servicio presenta el mayor monto.
4. Crear un nuevo vector con todas las reservas donde la edad del cumpleañero sea mayor a un valor x pasado
por parametro y la cantidad de asistentes mayor a un valor y tambien pasado por parametro. Mostrar el
contenido.
5. Salir del programa, pero antes de terminar, grabar nuevamente todas las reservas en el archivo reservas.csv
(sobrescribir el archivo)
"""
import os


def leer_archivo_csv(fd):
    # controlar si existe el archivo
    if not os.path.exists(fd):
        print('El archivo ', fd, ' no existe')
        return
    # leemos el contenido del archivo
    m = open(fd, 'rt')
    for linea in m:
        if linea[-1] == '\n':
            linea = linea[:-1] # es para borrar el \n
        print(linea)


def principal():
    fd = 'reservas.csv' # file descriptor - actua como una variable general
    print('Salon de fiestas')
    leer_archivo_csv(fd)


if __name__ == '__main__':
    principal()