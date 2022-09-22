# cargamos el modulo de serilizacion pickle
import pickle

# Creamos la clase Vehiculo
class Vehiculo:
    motor = "diesel"
    ruedas = 4
    color = "rojo"

    def __init__(seft, motor, ruedas, color):
        seft.motor = motor
        seft.ruedas = ruedas
        seft.color = color

    def setColor(seft, color):
        seft.color = color

    def getColor(seft):
        return seft.color


def main():
    coche = Vehiculo("Gasolina", 6, "azul")
    fichero = open('vehiculo.bin','wb')
    pickle.dump(coche, fichero)
    print(f'El vehiculo de {coche.motor.lower()}, de color {coche.color} ha sido guardado.')
    fichero.close()


    # creo un nuevo vehiculo desde el archivo guardado
    fichero = open ('vehiculo.bin','rb')
    camion_rosa = pickle.load(fichero)
    camion_rosa.setColor("rosa")
    print(f'El vehiculo de {camion_rosa.motor.lower()}, de color {camion_rosa.color} ha sido recuperado.')

    fichero.close()

      
if (__name__=="__main__"):
    main()
