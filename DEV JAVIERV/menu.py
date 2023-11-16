
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ventanaMetodos import ventanaBiseccion as biseccion
from ventanaMetodos import ventanaFalsaPosicion as falsa
from ventanaMetodos import ventanaNewtonRaphson as newton
from ventanaMetodos import ventanaSecante as secante


def abrirBiseccion(menu_ventana):
    biseccion.abrir_menu_biseccion(menu_ventana)
 
def abrirFalsaPosicion(menu_ventana):
    falsa.abrir_menu_falsa(menu_ventana)

def abrirNewtonRaphson(menu_ventana):
    newton.abrir_menu_secante(menu_ventana)
    
def abrirSecante(menu_ventana):
    secante.abrir_menu_secante(menu_ventana)
    





def abrir_menu(ventana):
    menu_ventana = Toplevel(ventana)
    menu_ventana.title("Menú")
    menu_ventana.resizable(False, False)
    menu_ventana.geometry(ventana.geometry())
    ventana.resizable(False, False)
    
    metodoBiseccion=ttk.Button(menu_ventana, text="Metodo de Biseccion", command=lambda:abrirBiseccion(menu_ventana))
    metodoBiseccion.pack()
    metodoFalsaPosicion=ttk.Button(menu_ventana, text="Metodo de la Falsa posicion", command=lambda:abrirFalsaPosicion(menu_ventana))
    metodoFalsaPosicion.pack()
    metodoNewton=ttk.Button(menu_ventana, text="Metodo de Newton Raphson", command=lambda:abrirNewtonRaphson(menu_ventana))
    metodoNewton.pack()
    metodoSecante=ttk.Button(menu_ventana, text="Metodo de la Secante", command=lambda:abrirSecante(menu_ventana))
    metodoSecante.pack()
    

    ventana.withdraw()
     


