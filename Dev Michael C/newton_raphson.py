#SCRIPT PARA EJECUTAR EL METODO DE NEWTON RAPHSON
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

# Función para evaluar la derivada de la expresión ingresada por el usuario
def func_prime(expr, x):
    h = 0.000000001  # Valor pequeño para h
    return (evaluarFuncion(expr, x + h) - evaluarFuncion(expr, x)) / h

# Método de Newton-Raphson
def newton_raphson(expr, x0, x1, error_tol, max_iterations, text_widget, ax, canvas):
    iteration = 0
    roots = []

    while iteration < max_iterations:
        x2 = x1 - (evaluarFuncion(expr, x1) / func_prime(expr, x1))
        error = abs(x2 - x1)

        # Imprimir los detalles de cada iteración en la interfaz de usuario
        text_widget.insert(tk.END, '---------------------\n')
        text_widget.insert(tk.END, f'Iteración: {iteration + 1}\n')
        text_widget.insert(tk.END, f'x2: {x2}\n')
        text_widget.insert(tk.END, f'f(x2) = {evaluarFuncion(expr, x2)}\n')
        text_widget.insert(tk.END, f"f'(x2) = {func_prime(expr, x2)}\n")
        text_widget.insert(tk.END, f'Error calculado: {error}\n')

        if error < error_tol:
            text_widget.insert(tk.END, f'Solución aproximada encontrada: x ≈ {x2}\n')
            return x2

        x0, x1 = x1, x2
        roots.append(x1)
        iteration += 1

        # Dibujar la gráfica
        ax.clear()
        x = np.linspace(x0 - 1, x1 + 1, 400)
        y = [evaluarFuncion(expr, i) for i in x]
        y_prime = [func_prime(expr, i) for i in x]
        ax.plot(x, y, label="f(x)")
        ax.plot(x, y_prime, label="f'(x)")
        ax.scatter(roots, [0]*len(roots), color='red')  # Marcar los puntos de corte en el eje X
        for root in roots:
            ax.annotate(f'{root:.2f}', (root, -0.5), textcoords="offset points", xytext=(-10,-10), ha='center')  # Anotar los puntos de corte
        ax.legend()
        ax.grid(True)
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        canvas.draw()

    text_widget.insert(tk.END, f'El método de Newton-Raphson no convergió después de {max_iterations} iteraciones.\n')
    return None

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
    x0 = simpledialog.askfloat("Entrada", "Ingrese el valor inicial x0:")
    x1 = simpledialog.askfloat("Entrada", "Ingrese el valor inicial x1:")
    error_tol = simpledialog.askfloat("Entrada", "Ingrese el error tolerado:")
    max_iterations = simpledialog.askinteger("Entrada", "Ingrese el número máximo de iteraciones:")

    # Calcular la solución y mostrarla
    solucion = newton_raphson(expr, x0, x1, error_tol, max_iterations, text_widget, ax, canvas)
    if solucion is not None:
        messagebox.showinfo("Resultado", f"La solución es: {solucion}")

    root.mainloop()