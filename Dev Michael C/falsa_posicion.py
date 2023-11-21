#SCRIPT PARA EJECUTAR EL METODO DE FALSA POSCION
#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576
import math
import tkinter as tk
from tkinter import simpledialog, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Función para evaluar la expresión ingresada por el usuario
def evaluarFuncion(expr, x):
    return eval(expr)

# Método de la falsa posición
def falsa_posicion(expr, a, b, error, text_widget, ax, canvas):
    errorCalculado = 100
    iteracion = 0
    xiAnterior = 0

    # Dibujar los puntos 'a' y 'b' iniciales
    ax.plot(a, evaluarFuncion(expr, a), 'go')  # Marcar el punto 'a' en verde
    ax.plot(b, evaluarFuncion(expr, b), 'bo')  # Marcar el punto 'b' en azul
    ax.annotate(f'a={a:.2f}', (a, evaluarFuncion(expr, a)), textcoords="offset points", xytext=(-10,-10), ha='center')  # Anotar el punto 'a'
    ax.annotate(f'b={b:.2f}', (b, evaluarFuncion(expr, b)), textcoords="offset points", xytext=(-10,-10), ha='center')  # Anotar el punto 'b'
    canvas.draw()

    while errorCalculado > error:
        f_a = evaluarFuncion(expr, a)
        f_b = evaluarFuncion(expr, b)
        xi = a - ((b - a) / (f_b - f_a)) * f_a
        f_xi = evaluarFuncion(expr, xi)

        if f_a * f_xi < 0:
            b = xi
        else:
            a = xi

        if iteracion > 0:
            errorCalculado = abs(xi - xiAnterior)
        xiAnterior = xi
        iteracion += 1

        # Imprimir los detalles de cada iteración en la interfaz de usuario
        text_widget.insert(tk.END, '---------------------\n')
        text_widget.insert(tk.END, f'Iteración: {iteracion}\n')
        text_widget.insert(tk.END, f'f(a) = {f_a}\n')
        text_widget.insert(tk.END, f'f(b) = {f_b}\n')
        text_widget.insert(tk.END, f'xi: {xi}\n')
        text_widget.insert(tk.END, f'f(xi) = {f_xi}\n')
        text_widget.insert(tk.END, f'Nuevo intervalo = ({a}, {b})\n')
        text_widget.insert(tk.END, f'Error calculado: {errorCalculado}\n')

        # Dibujar la gráfica
        ax.clear()
        x = np.linspace(a - 1, b + 1, 400)
        y = [evaluarFuncion(expr, i) for i in x]
        ax.plot(x, y)
        ax.axvline(x=xi, color='r')  # Dibujar una línea vertical en x=xi
        ax.axhline(0, color='black')  # Dibujar el eje y
        ax.axvline(0, color='black')  # Dibujar el eje x
        ax.plot(a, evaluarFuncion(expr, a), 'go')  # Marcar el punto 'a' en verde
        ax.plot(b, evaluarFuncion(expr, b), 'bo')  # Marcar el punto 'b' en azul
        ax.annotate(f'a={a:.2f}', (a, evaluarFuncion(expr, a)), textcoords="offset points", xytext=(-10,-10), ha='center')  # Anotar el punto 'a'
        ax.annotate(f'b={b:.2f}', (b, evaluarFuncion(expr, b)), textcoords="offset points", xytext=(-10,-10), ha='center')  # Anotar el punto 'b'
        canvas.draw()

    return xi

# Función para limpiar la información
def limpiar(text_widget, ax, canvas):
    text_widget.delete('1.0', tk.END)
    ax.clear()
    canvas.draw()

# Función para abrir la ventana
def abrir_ventana():
    # Crear la ventana de tkinter
    root = tk.Tk()

    # Crear un widget de texto para mostrar los detalles de cada iteración
    text_widget = tk.Text(root)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear una figura y un eje para la gráfica
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Crear un lienzo para dibujar la gráfica en la interfaz de usuario
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Crear un botón para limpiar la información
    button = tk.Button(root, text="Limpiar", command=lambda: limpiar(text_widget, ax, canvas))
    button.pack()

    # Solicitar la función, los intervalos y el error al usuario
    expr = simpledialog.askstring("Entrada", "Ingrese la función f(x):")
    a = simpledialog.askfloat("Entrada", "Ingrese el límite inferior del intervalo (a):")
    b = simpledialog.askfloat("Entrada", "Ingrese el límite superior del intervalo (b):")
    error = simpledialog.askfloat("Entrada", "Ingrese el error deseado:")

    # Calcular la solución y mostrarla
    solucion = falsa_posicion(expr, a, b, error, text_widget, ax, canvas)
    messagebox.showinfo("Resultado", f"La solución es: {solucion}")

    root.mainloop()
