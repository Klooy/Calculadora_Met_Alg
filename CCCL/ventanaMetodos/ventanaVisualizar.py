from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import math
import matplotlib.pyplot as plt
import numpy as np


def volver_a_menu(menu_ventana, visualizar_ventana):
    visualizar_ventana.destroy()  # Cierra la ventana de Visualizar
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú

def visualizar_grafica(funcion, canvas):
    try:
        x = np.linspace(-5, 5, 100)
        y = eval(funcion)
    except Exception as e:
        print(f"Error al evaluar la función: {e}")
        return

    # Limpiar el canvas antes de dibujar una nueva gráfica
    canvas.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(x, y)
    ax.set_title("Gráfica de la Función")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Crear un nuevo canvas y mostrar la gráfica
    canvas = FigureCanvasTkAgg(fig, master=menuVisualizar)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor='center')   

def abrir_menu_visualizar(menu_ventana):
    # CONFIGURACIÓN BÁSICA DE LA VENTANA
    menuVisualizar = Toplevel(menu_ventana)
    menuVisualizar.title("Menú de Visualizar")
    menuVisualizar.resizable(False, False)
    menuVisualizar.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menuVisualizar.configure(bg='lightblue')
    menu_ventana.withdraw()

    # ESTILOS DEL TÍTULO
    estilo_label = {
        'font': ['Arial', 15, 'bold'],
        'foreground': 'white',
        'background': 'black',
        'padx': 250,
        'pady': 5
    }
    text = Label(menuVisualizar, text="VISUALIZAR GRÁFICA", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')

    volverAlMenu = ttk.Button(menuVisualizar, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuVisualizar))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')

    entry_funcion = Entry(menuVisualizar, width=30)
    entry_funcion.place(relx=0.5, rely=0.2, anchor='center')

    button_visualizar = ttk.Button(menuVisualizar, text="Visualizar Gráfica", command=lambda: visualizar_grafica(entry_funcion.get(), canvas))
    button_visualizar.place(relx=0.5, rely=0.3, anchor='center')

    volverAlMenu = ttk.Button(menuVisualizar, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuVisualizar))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')

    # Crear un canvas inicial para la gráfica (vacío)
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=menuVisualizar)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor='center')

    menu_ventana.withdraw()

    abrir_menu_button = ttk.Button(menu_ventana, text="Abrir Menú de Visualizar", command=lambda: abrir_menu_visualizar(menu_ventana))
    abrir_menu_button.pack(pady=20)

    
