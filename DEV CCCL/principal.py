from tkinter import *
from tkinter import ttk
import menu

def abrir_menu(ventana):
    menu.abrir_menu(ventana)

def funcion_click(accion, etiqueta, ventana):
    accion.configure(text="Siguiente")
    etiqueta.configure(foreground="red")
    abrir_menu(ventana)

def iniciar_ventana_principal():
    ventana = Tk()
    ventana.title("METODOS")
    ventana.geometry("500x500")
    ventana.resizable(False, False)

    etiqueta = Label(ventana, text="Etiqueta inicial")
    etiqueta.grid(column=0, row=0)

    accion = ttk.Button(ventana, text="Siguiente", command=lambda: funcion_click(accion, etiqueta, ventana))
    accion.grid(column=0, row=1, pady=400, padx=210)

    ventana.mainloop()

