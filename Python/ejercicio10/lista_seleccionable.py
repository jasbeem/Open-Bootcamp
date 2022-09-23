from tkinter import *

ventana = Tk()
ventana.title("Lista Selecionable")
colores = ('Rojo','Amarillo','Azul','Gris')
var = Variable(value=colores)
etiqueta = Label(ventana, text="", width=50, background="yellow", foreground="blue")
etiqueta.grid(pady=5, row=1, column=0, columnspan=5)
listbox = Listbox(
        ventana,
        listvariable=var,
        height=6,
        selectmode=EXTENDED
    )

def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_colores = ",".join([listbox.get(i) for i in selected_indices])
    texto = f'Selecionaste : {selected_colores}'
    etiqueta.config(text = texto)

def cerrar():
    ventana.destroy()

def main():
    titulo = Label(ventana, text="  Elige tu color favorito  ")
    titulo.grid(pady=5, row=0, column=0)
    
    listbox.grid(pady=5, row=4, column=0)
    listbox.bind('<<ListboxSelect>>', items_selected)    
    boton_cerrar = Button(ventana, text="Cerrar", width=50, command=cerrar)
    boton_cerrar.grid(padx=10, pady=10, row=8, column=0, columnspan=2)
    
    ventana.mainloop()

if (__name__ == "__main__"):
    main()
