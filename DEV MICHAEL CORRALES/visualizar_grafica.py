#SCRIPT PARA VISUALIZAR LA GRAFICA DE CADA METODO
#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576

import matplotlib.pyplot as plt
import numpy as np
import math

# Definir la función
def f(x):
    return math.exp(x) - math.exp(-x) - 2

def visualizar_grafica():
    # Crear un array de valores x
    x = np.linspace(-5, 5, 400)

    # Vectorizar la función para que pueda tomar un array numpy
    vf = np.vectorize(f)

    # Calcular los valores y
    y = vf(x)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label='f(x) = exp(x) - exp(-x) - 2')

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

    plt.show()
