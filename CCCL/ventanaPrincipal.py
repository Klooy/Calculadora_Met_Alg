from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


import menu

def abrir_menu(ventana):
    menu.abrir_menu(ventana)

def funcion_click(accion, etiqueta, ventana):
    accion.configure(text="INICIAR")
    etiqueta.configure(foreground="white")
    abrir_menu(ventana)

def iniciar_ventana_principal():
    ventana = Tk()
    ventana.title("METODOS NUMERICOS")
    ventana.geometry("700x500")
    ventana.resizable(False, False)
    ventana.configure(bg='lightblue')


    estilo_label = {
    'font': ['Arial', 24, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 20,
    'pady': 10
    }

    estilo_boton = ttk.Style()
    estilo_boton.configure('Estilo.TButton', font=('Arial', 12, 'bold'), foreground='black', background='black', padx=10, pady=5,borderwidth=2,relief='raised' )
    
    text = Label(ventana, text="CALCULADORA DE METODOS NUMERICOS", **estilo_label)
    text.place(relx=0.5, rely=0.15, anchor='center')

    imagen=Image.open('./img/imagenPrincipal.gif')
    imagen = imagen.resize((300, 200)) 
    imagen_tk = ImageTk.PhotoImage(imagen)
    label_imagen = ttk.Label(ventana, image=imagen_tk)
    label_imagen.place(relx=0.5, rely=0.50, anchor='center')
    
    accion = ttk.Button(ventana, text="INICIAR", style='Estilo.TButton',command=lambda: funcion_click(accion, text, ventana))
    accion.place(relx=0.5, rely=0.90, anchor='center')

    ventana.mainloop()

