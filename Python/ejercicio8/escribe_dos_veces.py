# Abrimos el archivo en modo acumulativo 'append'
fichero = open ('datos.txt','a')
# Escribimos algunos datos
fichero.write("Hola\n")
fichero.write("Adios\n")
# Cerramos el archivo
fichero.close()