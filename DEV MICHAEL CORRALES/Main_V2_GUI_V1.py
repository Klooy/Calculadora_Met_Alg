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
from tkinter import messagebox

# Ventana principal
root = tk.Tk()
root.title("Menú de Métodos")

# Acciones para cada botón
def visualizar_grafica_btn():
    print("Visualizando Gráfica:")
    visualizar_grafica.visualizar_grafica()

def biseccion_btn():
    print("Método de Bisección:")
    biseccion.biseccion()

def falsa_posicion_btn():
    print("Método de Falsa Posición:")
    falsa_posicion.falsa_posicion()

def secante_btn():
    print("Método de la Secante:")
    secante.secante()

def newton_raphson_btn():
    print("Método de Newton-Raphson:")
    newton_raphson.newton_raphson()

def comparar_btn():
    print("Comparar Métodos:")
    comparar.generar_tabla()

# Botones para cada opción
visualizar_grafica_btn = tk.Button(root, text="Visualizar Gráfica", command=visualizar_grafica_btn)
biseccion_btn = tk.Button(root, text="Bisección", command=biseccion_btn)
falsa_posicion_btn = tk.Button(root, text="Falsa Posición", command=falsa_posicion_btn)
secante_btn = tk.Button(root, text="Secante", command=secante_btn)
newton_raphson_btn = tk.Button(root, text="Newton-Raphson", command=newton_raphson_btn)
comparar_btn = tk.Button(root, text="Comparar Métodos", command=comparar_btn)

# Ventana con botones
visualizar_grafica_btn.pack()
biseccion_btn.pack()
falsa_posicion_btn.pack()
secante_btn.pack()
newton_raphson_btn.pack()
comparar_btn.pack()

#Bucle principal de la ventana (Nota personal; esto evita que se me cierre la ventana de los botones al ejecutar una accion)
root.mainloop()
