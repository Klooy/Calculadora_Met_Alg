from tkinter import *
from tkinter import ttk


def volver_a_menu(menu_ventana, comparar_ventana):
    comparar_ventana.destroy()  # Cierra la ventana de Comparar
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú

def abrir_menu_comparar(menu_ventana):
    # CONFIGURACIÓN BÁSICA DE LA VENTANA
    comparar_ventana = Toplevel(menu_ventana)
    comparar_ventana.title("Menú de Comparación de Métodos")
    comparar_ventana.resizable(False, False)
    comparar_ventana.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    comparar_ventana.configure(bg='lightblue')
    menu_ventana.withdraw()

    # ESTILOS DEL TÍTULO
    estilo_label = {
        'font': ['Arial', 15, 'bold'],
        'foreground': 'white',
        'background': 'black',
        'padx': 250,
        'pady': 5
    }
    text = Label(comparar_ventana, text="COMPARACIÓN DE MÉTODOS", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')

    volver_al_menu = ttk.Button(comparar_ventana, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, comparar_ventana))
    volver_al_menu.place(relx=0.08, rely=0.94, anchor='center')
