from tkinter import *

def abrir_menu(ventana):
    menu_ventana = Toplevel(ventana)
    menu_ventana.title("Menú")

    menu_ventana.geometry(ventana.geometry())
    ventana.resizable(False, False)

    

    ventana.withdraw()
    


