#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576
#SCRIPT MAIN CON INTERFAZ GUI V.1 MENU DE OPCIONES

#IMPORTO LOS METODOS ALGORITMICOS
import biseccion
import falsa_posicion
import secante
import newton_raphson
import comparar
import visualizar_grafica
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

# Ventana principal
root = tk.Tk()
root.title("Menú de Métodos")
root.configure(bg='white')  # Fondo blanco para un aspecto más minimalista

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

# Botones para cada opción
visualizar_grafica_btn = ttk.Button(root, text="Visualizar Gráfica", command=visualizar_grafica_btn)
biseccion_btn = ttk.Button(root, text="Bisección", command=biseccion_btn)
falsa_posicion_btn = ttk.Button(root, text="Falsa Posición", command=falsa_posicion_btn)
secante_btn = ttk.Button(root, text="Secante", command=secante_btn)
newton_raphson_btn = ttk.Button(root, text="Newton-Raphson", command=newton_raphson_btn)
comparar_btn = ttk.Button(root, text="Comparar Métodos", command=comparar_btn)
ayuda_btn = ttk.Button(root, text="Ayuda", command=ayuda_btn)

# Ventana con botones
visualizar_grafica_btn.pack(pady=10)  # Agregar un poco de espacio vertical entre los botones
biseccion_btn.pack(pady=10)
falsa_posicion_btn.pack(pady=10)
secante_btn.pack(pady=10)
newton_raphson_btn.pack(pady=10)
comparar_btn.pack(pady=10)
ayuda_btn.pack(pady=10)

#Bucle principal de la ventana (Nota personal; esto evita que se me cierre la ventana de los botones al ejecutar una accion)
root.mainloop()