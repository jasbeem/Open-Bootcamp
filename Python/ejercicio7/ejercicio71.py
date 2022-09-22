# Importamos el módulo time
import time

hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M')) 

if hora >= 19:
	print ("Ya tenías que estar en casa") 
else:
    horas_restantes= 18-hora
    minutos_restantes= 59-minutos
    print("Quedan "+str(horas_restantes)+" horas y "+str(minutos_restantes)+" minutos.")