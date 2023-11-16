from tkinter import *
from tkinter import ttk

def crearGrafica(funcion):
    print(funcion)
    pass

def abrir_menu_biseccion(menu_ventana):
    #CONFIGURACION BASICA DE LA VENTANA
    menuBis = Toplevel(menu_ventana)
    menuBis.title("Menú de Biseccion")
    menuBis.resizable(False, False)
    menuBis.geometry(menu_ventana.geometry())
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
    text = Label(menuBis, text="Escribe la funcion", **estilo_label)
    text.pack()
    #ENTRADA DE LA FUNCION
    funcion=ttk.Entry(menuBis,width=40)
    funcion.pack()
 
    #BOTON GENERAR GRAFICA 
    generacionGrafica=ttk.Button(menuBis, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    generacionGrafica.pack()


    