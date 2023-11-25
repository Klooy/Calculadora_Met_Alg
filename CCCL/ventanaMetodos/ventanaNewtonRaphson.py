from tkinter import *
from tkinter import ttk

#def crearGrafica(funcion):
    #print(funcion)
    #pass

def volver_a_menu(menu_ventana, newton_ventana):
    newton_ventana.destroy()  # Cierra la ventana de Newton-Raphson
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú

def abrir_menu_secante(menu_ventana):
    menuNewton = Toplevel(menu_ventana)
    menuNewton.title("Menú de Newton Raphson")
    menuNewton.resizable(False, False)
    menuNewton.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menuNewton.configure(bg='lightblue')
    menu_ventana.withdraw()
    
    #ESTILOS DEL TITULO
    estilo_label = {
    'font': ['Arial', 15, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 250,
    'pady': 5
    }
    text = Label(menuNewton, text="METODO DE NEWTON RAPHSON", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')
    
    #ENTRADA DE LA FUNCION
    #funcion=ttk.Entry(menuNewton,width=40)
    #funcion.pack()

    #BOTON GENERAR GRAFICA 
    #generacionGrafica=ttk.Button(menuNewton, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    #generacionGrafica.pack()

    # BOTON VOLVER AL MENU
    volverAlMenu = ttk.Button(menuNewton, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuNewton))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')
