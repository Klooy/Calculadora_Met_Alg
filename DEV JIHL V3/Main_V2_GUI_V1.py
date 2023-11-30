#IMPORTO LOS METODOS ALGORITMICOS
import biseccion
import falsa_posicion
import secante
import newton_raphson
import comparar
import visualizar_grafica

#LIBRERIAS DE INTERFAZ
import matplotlib.pyplot as plt
import numpy as np
import math
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, ttk
import webbrowser

#Ventana principal
def ventana1():
    root = tk.Tk()
    root.title("ALGORITMOS")
    root.geometry("650x400")
    root.resizable(False, False)
    
    miImagen=PhotoImage(file="logo_completo.png")
    miImagen1=PhotoImage(file="logo3.png")

    Label(root, text="BIENVENIDO", fg="Black", bg='white', font=("Times New Roman", 32)).place(x=190, y=110)
    Label(root, image=miImagen, bg='white').place(x=30, y=0)
    Label(root, imag=miImagen1, bg='white').place(x=-1, y=325)

    Label(root, text="CALCULADORA DE METODOS ALGORITMICOS", fg="Black", bg='white', font=("Times New Roman", 14)).place(x=117, y=200)
    Label(root, text="METODOS:", fg="Black", bg='white', font=("Times New Roman", 14)).place(x=280, y=240)
    Label(root, text="BISECCION, FALSA POSICION, SECANTE Y NEWWTON RAPHSON", fg="Black", bg='white', font=("Times New Roman", 14)).place(x=35, y=260)
    
    root.configure(bg='white')  # Fondo para un aspecto más minimalista

    estilo_boton = ttk.Style()
    estilo_boton.configure('Estilo.TButton', font=('Times New Roman', 12, 'bold'), foreground='black', background='black', borderwidth=2,relief='raised', width=8, height=0.5)
    
    boton_iniciar = ttk.Button(root, text="INICIAR", style='Estilo.TButton', command=ventana2)
    boton_iniciar.place(x=280, y=350)


    root.mainloop()



# Ventana Metodos
def ventana2():
    root = Toplevel()
    
    root.title("METODOS")
    root.geometry("650x400")
    root.resizable(False, False)
    miImagen1=PhotoImage(file="logo_completo.png")
    miImagen2=PhotoImage(file="logo3.png")
    
    Label(root, text="METODOS ALGORITMICOS", fg="black", bg='white', font=("Times New Roman", 24)).place(x=120, y=89)


    Label(root, image=miImagen1, bg='white').place(x=30, y=0)
    Label(root, imag=miImagen2, bg='white').place(x=-1, y=325)

    
    root.configure(bg='white')  # Fondo para un aspecto más minimalista

# Botones con estilo ttk
    estilo_boton = ttk.Style()
    estilo_boton.configure('Estilo.TButton', font=('Times New Roman', 12, 'bold'), foreground='black', background='black', borderwidth=2,relief='raised', width=17, height=0.5)
    
    ttk.Button(root, text="Bisección", style='Estilo.TButton', command=biseccion_btn).place(x=105, y=150)
    ttk.Button(root, text="Falsa Posición", style='Estilo.TButton', command=falsa_posicion_btn).place(x=400, y=150)
    ttk.Button(root, text="Secante", style='Estilo.TButton', command=secante_btn).place(x=105, y=200)
    ttk.Button(root, text="Newton-Raphson", style='Estilo.TButton', command=newton_raphson_btn).place(x=400, y=200)
    ttk.Button(root, text="Visualizar Gráfica", style='Estilo.TButton', command=visualizar_grafica_btn).place(x=105, y=250)
    ttk.Button(root, text="Comparar Métodos", style='Estilo.TButton', command=comparar_btn).place(x=400, y=250)
    ttk.Button(root, text="Ayuda", style='Estilo.TButton', command=ayuda_btn).place(x=255, y=350)

    
    root.mainloop()


    
# Acciones para cada botón
def visualizar_grafica_btn():
    print("Visualizando Gráfica:")
    visualizar_grafica.iniciar_ventana()

def biseccion_btn():
    print("Método de Bisección:")
    biseccion.abrir_ventana()

def falsa_posicion_btn():
    print("Método de Falsa Posición:")
    falsa_posicion.abrir_ventana()

def secante_btn():
    print("Método de la Secante:")
    secante.abrir_ventana()

def newton_raphson_btn():
    print("Método de Newton-Raphson:")
    newton_raphson.abrir_ventana()

def comparar_btn():
    print("Comparar Métodos:")
    comparar.abrir_ventana()

def ayuda_btn():
    webbrowser.open('https://github.com/Klooy/Calculadora_Met_Alg/tree/main')



ventana1()



