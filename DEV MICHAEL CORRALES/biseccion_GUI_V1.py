#SCRIPT PARA EJECUTAR EL METODO DE BISECCION
#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576
import math
import tkinter as tk
from tkinter import messagebox

#DEFINIMOS LA FUNCION f(X) = EXP(X) - EXP (-X) - 2
def evaluarFuncion(x):
    return math.exp(x) - math.exp(-x) - 2

#DEFINIMOS EL METODO EN ESTE CASO "BISECCION" Y LOS DATOS DE ENTRADA
def biseccion():
    a = 0
    b = 1
    error = 0.001
    errorCalculado = 100
    iteracion = 0
    resultado = ''

    #CICLO PARA EL CALCULO DEL ERROR PASO A PASO EN BISECCION
    while errorCalculado > error:
        m = (a + b) / 2
        f_a = evaluarFuncion(a)
        f_b = evaluarFuncion(b)
        f_m = evaluarFuncion(m)

        if f_a * f_m < 0:
            b = m
        else:
            a = m

        if iteracion > 0:
            errorCalculado = (b - a) / 2

        iteracion += 1
        resultado += '---------------------\n'
        resultado += f'Iteración: {iteracion}\n'
        resultado += f'm: {m}\n'
        resultado += f'f(a) = {f_a}\n'
        resultado += f'f(b) = {f_b}\n'
        resultado += f'f(m) = {f_m}\n'
        resultado += f'Nuevo intervalo = ({a}, {b})\n'
        resultado += f'Error calculado: {errorCalculado}\n'

    resultado += f'La solución es: {m}\n'
    return resultado

# Creamos una ventana y mostramos el resultado
def mostrar_resultado():
    resultado = biseccion()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Resultado", resultado)

mostrar_resultado()
