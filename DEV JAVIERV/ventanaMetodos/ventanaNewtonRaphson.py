from tkinter import *
from tkinter import ttk

def crearGrafica(funcion):
    print(funcion)
    pass

def abrir_menu_secante(menu_ventana):
    menuNewton = Toplevel(menu_ventana)
    menuNewton.title("Menú de Newton Raphson")
    menuNewton.resizable(False, False)
    menuNewton.geometry(menu_ventana.geometry())
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
    text = Label(menuNewton, text="Escribe la funcion", **estilo_label)
    text.pack()
    #ENTRADA DE LA FUNCION
    funcion=ttk.Entry(menuNewton,width=40)
    funcion.pack()

    #BOTON GENERAR GRAFICA 
    generacionGrafica=ttk.Button(menuNewton, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    generacionGrafica.pack()
