#!/usr/bin/python3
peso = input ("Introduce tu peso: ")
altura = input ("Introduce tu altura: ")
# Calculamos indice de masa corporal
imc = round(float(peso)/float(altura)**2,2) 
print("Tu índice de masa corporal es " + str(imc))
