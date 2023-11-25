from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import numpy as np
import math
import webbrowser
from ventanaMetodos import ventanaBiseccion as biseccion
from ventanaMetodos import ventanaFalsaPosicion as falsa
from ventanaMetodos import ventanaNewtonRaphson as newton
from ventanaMetodos import ventanaSecante as secante
from ventanaMetodos import ventanaVisualizar as visualizar
from ventanaMetodos import ventanaComparar as comparar



def abrirBiseccion(menu_ventana):
    biseccion.abrir_menu_biseccion(menu_ventana)
 
def abrirFalsaPosicion(menu_ventana):
    falsa.abrir_menu_falsa(menu_ventana)

def abrirNewtonRaphson(menu_ventana):
    newton.abrir_menu_secante(menu_ventana)
    
def abrirSecante(menu_ventana):
    secante.abrir_menu_secante(menu_ventana)

def visualizar_grafica_btn(menu_ventana):
    visualizar.abrir_menu_visualizar(menu_ventana)

def comparar_btn(menu_ventana):
    comparar.abrir_menu_comparar(menu_ventana)

def ayuda_btn():
    webbrowser.open('https://github.com/Klooy/Calculadora_Met_Alg/tree/main')

def abrir_menu(ventana):
    menu_ventana = Toplevel(ventana)
    menu_ventana.title("Menú")
    menu_ventana.resizable(False, False)
    menu_ventana.geometry(ventana.geometry())
    ventana.resizable(False, False)
    menu_ventana.configure(bg='lightblue')

    estilo_label = {
        'font': ['Arial', 24, 'bold'],
        'foreground': 'white',
        'background': 'black',
        'padx': 200,
        'pady': 3
    }

    text = Label(menu_ventana, text="METODOS NUMERICOS", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')

    metodoBiseccion = ttk.Button(menu_ventana, text="Metodo de Biseccion", command=lambda: abrirBiseccion(menu_ventana))
    metodoBiseccion.place(relx=0.25, rely=0.30, anchor='center')

    metodoFalsaPosicion = ttk.Button(menu_ventana, text="Metodo de la Falsa posicion", command=lambda: abrirFalsaPosicion(menu_ventana))
    metodoFalsaPosicion.place(relx=0.70, rely=0.30, anchor='center')

    metodoSecante = ttk.Button(menu_ventana, text="Metodo de la Secante", command=lambda: abrirSecante(menu_ventana))
    metodoSecante.place(relx=0.25, rely=0.50, anchor='center')

    metodoNewton = ttk.Button(menu_ventana, text="Metodo de Newton Raphson", command=lambda: abrirNewtonRaphson(menu_ventana))
    metodoNewton.place(relx=0.70, rely=0.50, anchor='center')

    visualizar_grafica_btn_local = ttk.Button(menu_ventana, text="Visualizar Gráfica", command=lambda: visualizar_grafica_btn(menu_ventana))
    visualizar_grafica_btn_local.place(relx=0.35, rely=0.70, anchor='center')

    comparar_btn_local = ttk.Button(menu_ventana, text="Comparar Métodos", command=lambda: comparar_btn(menu_ventana))
    comparar_btn_local.place(relx=0.60, rely=0.70, anchor='center')

    boton_ayuda = ttk.Button(menu_ventana, text="Ayuda", command=ayuda_btn)
    boton_ayuda.place(relx=0.9, rely=0.94, anchor='center')

    ventana.withdraw()

