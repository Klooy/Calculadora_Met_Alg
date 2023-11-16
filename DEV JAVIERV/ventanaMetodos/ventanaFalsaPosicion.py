from tkinter import *
from tkinter import ttk

def crearGrafica(funcion):
    print(funcion)
    pass

def abrir_menu_falsa(menu_ventana):
    menuFalsa = Toplevel(menu_ventana)
    menuFalsa.title("Menú de Falsa Posicion")
    menuFalsa.resizable(False, False)
    menuFalsa.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menu_ventana.withdraw()
    
    #ESTILOS DEL TITULO
    estilo_label = {
    'font': ['Arial', 15, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 20,
    'pady': 10
    }
    text = Label(menuFalsa, text="Escribe la funcion", **estilo_label)
    text.pack()
    #ENTRADA DE LA FUNCION
    funcion=ttk.Entry(menuFalsa,width=40)
    funcion.pack()

    #BOTON GENERAR GRAFICA 
    generacionGrafica=ttk.Button(menuFalsa, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    generacionGrafica.pack()
