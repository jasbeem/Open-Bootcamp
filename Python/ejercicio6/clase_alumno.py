#!/usr/bin/python3
class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 6

class Coche(Vehiculo):
    velocidad = 120
    cilidrada = 2000

coche = Coche()
print ("Velocidad es: ", coche.velocidad)
print ("Color es: ", coche.color)
