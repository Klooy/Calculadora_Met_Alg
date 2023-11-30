#SCRIPT PARA COMPARAR LOS METODOS ALGORTIMICOS


import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from formateo import formatearFuncion

def abrir_ventana():
    # Función para evaluar la función
    def evaluarFuncion(funcion_str, x):
         
        funcion = eval("lambda x: " + formatearFuncion(funcion_str))
        return funcion(x)

        # Método de Bisección
    def biseccion(funcion_str, a, b, error):
        iteracion = 0
        while (b - a) / 2 > error:
            m = (a + b) / 2
            f_a = evaluarFuncion(funcion_str, a)
            f_b = evaluarFuncion(funcion_str, b)
            f_m = evaluarFuncion(funcion_str, m)
            if f_a * f_m < 0:
                b = m
            else:
                a = m
            iteracion += 1
        return (a + b) / 2, iteracion

        # Método de Falsa Posición
    def falsa_posicion(funcion_str, a, b, err):
        iteracion = 0
        xiAnterior = 0
        while True:
            f_a = evaluarFuncion(funcion_str, a)
            f_b = evaluarFuncion(funcion_str, b)
            xi = a - ((b - a) / (f_b - f_a)) * f_a
            f_xi = evaluarFuncion(funcion_str, xi)
            if f_a * f_xi < 0:
                b = xi
            else:
                a = xi
            iteracion += 1
            if iteracion > 1 and abs(xi - xiAnterior) < err:
                break
            xiAnterior = xi
        return xi, iteracion

        # Método de Secante
    def secante(funcion_str, a, b, error_tol):
        iteration = 0
        while True:
            c = b - evaluarFuncion(funcion_str, b) * (b - a) / (evaluarFuncion(funcion_str, b) - evaluarFuncion(funcion_str, a))
            if abs(c - b) < error_tol:
                break
            a, b = b, c
            iteration += 1
        return c, iteration

        # Método de Newton-Raphson
    def newton_raphson(funcion_str, a, e):
        count = 0
        while True:
            b = a - (evaluarFuncion(funcion_str, a) / (math.exp(a) + math.exp(-a)))
            count += 1
            if abs(b - a) < e:
                break
            a = b
        return b, count

        # Genera la tabla con los resultados de los métodos
    def generar_tabla():
        funcion_str = funcion_entry.get()
        a = float(a_entry.get())
        b = float(b_entry.get())
        error = float(error_entry.get())

        # Bisección
        biseccion_result, biseccion_iters = biseccion(funcion_str, a, b, error)

        # Falsa Posición
        falsa_posicion_result, falsa_posicion_iters = falsa_posicion(funcion_str, a, b, error)

        # Secante
        secante_result, secante_iters = secante(funcion_str, a, b, error)

        # Newton-Raphson
        newton_result, newton_iters = newton_raphson(funcion_str, a, error)

        # Determina el mejor método
        resultados = {
            "Bisección": (biseccion_result, biseccion_iters),
            "Falsa Posición": (falsa_posicion_result, falsa_posicion_iters),
            "Secante": (secante_result, secante_iters),
            "Newton-Raphson": (newton_result, newton_iters)
        }
        mejor_metodo = min(resultados, key=lambda metodo: resultados[metodo][0])

        # Crear una ventana para la tabla
        tabla_ventana = tk.Toplevel(window)
        tabla_ventana.title("Tabla de Resultados")

        # Crear un widget Treeview para la tabla
        tabla = ttk.Treeview(tabla_ventana, columns=("Método", "Raíz Aproximada", "Iteraciones"), show="headings")
        tabla.heading("Método", text="Método")
        tabla.heading("Raíz Aproximada", text="Raíz Aproximada")
        tabla.heading("Iteraciones", text="Iteraciones")

        # Insertar los datos en la tabla
        for metodo, (raiz, iteraciones) in resultados.items():
            tabla.insert("", "end", values=(metodo, raiz, iteraciones))

        tabla.pack()      

        # Mostrar el mejor método
        mejor_label = tk.Label(tabla_ventana, text=f"El mejor método es: {mejor_metodo} con una raíz aproximada de {resultados[mejor_metodo][0]:.6f} y {resultados[mejor_metodo][1]} iteraciones")
        mejor_label.pack()
    
    # Crear la ventana de tkinter
    window = tk.Tk()
    window.title("Pagina de Comparacion")
    window.geometry("320x200")
    window.resizable(False, False)
    window.configure(bg='#73100f')

    # Crear los widgets de entrada de texto
    funcion_label = tk.Label(window, text="Función:", fg="White", bg='#73100f')
    funcion_label.pack()
    funcion_entry = tk.Entry(window)
    funcion_entry.pack()

    a_label = tk.Label(window, text="Punto de inicio a:", fg="White", bg='#73100f')
    a_label.pack()
    a_entry = tk.Entry(window)
    a_entry.pack()

    b_label = tk.Label(window, text="Punto de inicio b:", fg="White", bg='#73100f')
    b_label.pack()
    b_entry = tk.Entry(window)
    b_entry.pack()

    error_label = tk.Label(window, text="Porcentaje de error:", fg="White", bg='#73100f')
    error_label.pack()
    error_entry = tk.Entry(window)
    error_entry.pack()

    # Crear un botón que llame a la función generar_tabla cuando se presione
    button = tk.Button(window, text="Generar tabla",  command=generar_tabla)
    button.place(x=120, y=174)

    # Iniciar la ventana de tkinter
    window.mainloop()
