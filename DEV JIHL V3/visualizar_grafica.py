#SCRIPT PARA VISUALIZAR LA GRAFICA DE CADA METODO


import math
 
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from formateo import formatearFuncion

# Función para visualizar la gráfica
def visualizar_grafica(funcion_str):
    
    # Convertir la cadena de texto en una función
    print(funcion_str)
    print(formatearFuncion(funcion_str))
    print(eval("lambda x: " + formatearFuncion(funcion_str)))

    funcion = eval("lambda x: " + formatearFuncion(funcion_str))

    # Vectorizar la función para que pueda tomar un array numpy
    vf = np.vectorize(funcion)

    # Crear un array de valores x
    x = np.linspace(-5, 5, 400)

    # Calcular los valores y
    y = vf(x)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label='f(x) = ' + funcion_str)

    # Establecer los límites de los ejes
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    # Establecer la cuadrícula
    ax.grid(True)
    ax.set_xticks(np.arange(-5, 6, 0.5))
    ax.set_yticks(np.arange(-5, 6, 0.5))

    # Dibujar el plano cartesiano
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

    # Configurar las etiquetas y el título
    ax.set_xlabel('x', fontsize=14, fontweight='bold')
    ax.set_ylabel('y', fontsize=14, fontweight='bold')
    ax.set_title('Gráfico de la función f(x)', fontsize=16, fontweight='bold')

    ax.legend()

    return fig

def iniciar_ventana():
    # Crear la ventana de tkinter
    window = tk.Tk()
    window.title("Grafica")
    window.geometry("650x600")
    window.resizable(False, False)
    window.configure(bg='#73100f')

    # Crear un widget de entrada de texto
    Tex_label = tk.Label(window, text="Ingresa la funcion:", fg="White", bg='#73100f')
    Tex_label.pack()
    entry = tk.Entry(window)
    entry.pack()

    # Función para manejar el evento del botón
    def on_button_click():
        # Obtener la función ingresada por el usuario
        funcion_str = entry.get()

        # Generar la gráfica
        fig = visualizar_grafica(funcion_str)

        # Crear un canvas para mostrar la gráfica en la ventana de tkinter
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Crear un botón que llame a la función on_button_click cuando se presione
    button = tk.Button(window, text="Generar gráfica", command=on_button_click)
    button.place(x=279, y=55)

    # Iniciar la ventana de tkinter
    window.mainloop()
