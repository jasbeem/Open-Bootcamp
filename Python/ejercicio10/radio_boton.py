from tkinter import *

ventana = Tk()
opcion = StringVar()
opcion.set(None)
etiqueta = Label(ventana, text="", width=50, background="yellow", foreground="blue")
etiqueta.grid(pady=5, row=1, column=0, columnspan=5)

def pulsado():
    texto = opcion.get().capitalize()
    etiqueta.config(text = texto)
    


def reiniciar():
    etiqueta.config(text = "")
    opcion.set(None)

def main():
    titulo = Label(ventana, text="  Elige tu color favorito  ")
    titulo.grid(pady=5, row=0, column=0)
    boton_rojo = Radiobutton(ventana, text="Rojo", variable=opcion, value='rojo', command=pulsado)
    boton_rojo.grid(pady=5, row=2, column=0)
    boton_amarillo = Radiobutton(ventana, text="Amarillo", variable=opcion, value='amarillo', command=pulsado)
    boton_amarillo.grid(pady=5, row=3, column=0)
    boton_azul = Radiobutton(ventana, text="Azul", variable=opcion, value='azul', command=pulsado)
    boton_azul.grid(pady=5, row=4, column=0)
    boton_gris = Radiobutton(ventana, text="Gris", variable=opcion, value='gris', command=pulsado)
    boton_gris.grid(pady=5, row=5, column=0)

    boton_reiniciar = Button(ventana, text="Reiniciar", width=50, command=reiniciar)
    boton_reiniciar.grid(padx=10, pady=10, row=8, column=0, columnspan=2)
    
    ventana.mainloop()

if (__name__ == "__main__"):
    main()
