from tkinter import *
from tkinter import ttk
import math
import numpy as np
from tkinter import simpledialog, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#def crearGrafica(funcion):

    #print(funcion)
    #pass

def volver_a_menu(menu_ventana, biseccion_ventana):
    biseccion_ventana.destroy()  # Cierra la ventana de Bisección
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú

def abrir_menu_biseccion(menu_ventana):
    #CONFIGURACION BASICA DE LA VENTANA
    menuBis = Toplevel(menu_ventana)
    menuBis.title("Menú de Biseccion")
    menuBis.resizable(False, False)
    menuBis.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menuBis.configure(bg='lightblue')
    menu_ventana.withdraw()

    #ESTILOS DEL TITULO
    estilo_label = {
    'font': ['Arial', 15, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 250,
    'pady': 5
    }
    text = Label(menuBis, text="METODO DE BISECCION", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')
    
    #ENTRADA DE LA FUNCION
    #funcion=ttk.Entry(menuBis,width=40)
    #funcion.pack()
 
    #BOTON GENERAR GRAFICA 
    #generacionGrafica=ttk.Button(menuBis, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    #generacionGrafica.pack()

     # BOTON VOLVER AL MENU
    volverAlMenu = ttk.Button(menuBis, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuBis))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')


    
