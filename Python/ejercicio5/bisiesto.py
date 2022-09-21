#!/usr/bin/python3
def bisiesto (anyo):
    if anyo % 4 != 0: #no divisible entre 4
        return False
    elif anyo % 4 == 0 and anyo % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return False
    elif anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 == 0: #divisible entre 4, 100 y 400
        return True


anyo = int(input("Escribe un año: "))
if bisiesto(anyo):
    print("El año "+str(anyo)+" es bisiesto")
else:
    print("No, El año "+str(anyo)+" no es bisiesto")
