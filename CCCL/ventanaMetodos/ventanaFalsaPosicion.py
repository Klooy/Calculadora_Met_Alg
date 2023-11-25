from tkinter import *
from tkinter import ttk

#def crearGrafica(funcion):
    #print(funcion)
    #pass

def volver_a_menu(menu_ventana, falsa_ventana):
    falsa_ventana.destroy()  # Cierra la ventana de Falsa Posición
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú
    

def abrir_menu_falsa(menu_ventana):
    menuFalsa = Toplevel(menu_ventana)
    menuFalsa.title("Menú de Falsa Posicion")
    menuFalsa.resizable(False, False)
    menuFalsa.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menuFalsa.configure(bg='lightblue')
    menu_ventana.withdraw()
    
    #ESTILOS DEL TITULO
    estilo_label = {
    'font': ['Arial', 15, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 250,
    'pady': 5
    }
    text = Label(menuFalsa, text="METODO DE LA FALSA POSICION", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')
    
    #ENTRADA DE LA FUNCION
    #funcion=ttk.Entry(menuFalsa,width=40)
    #funcion.pack()

    #BOTON GENERAR GRAFICA 
    #generacionGrafica=ttk.Button(menuFalsa, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    #generacionGrafica.pack()

    # BOTON VOLVER AL MENU
    volverAlMenu = ttk.Button(menuFalsa, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuFalsa))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')
