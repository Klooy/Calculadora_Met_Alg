from tkinter import *
from tkinter import ttk

#def crearGrafica(funcion):
    #print(funcion)
    #pass

def volver_a_menu(menu_ventana, secante_ventana):
    secante_ventana.destroy()  # Cierra la ventana de Secante
    menu_ventana.deiconify()  # Muestra nuevamente la ventana del menú

def abrir_menu_secante(menu_ventana):
    menuSecante = Toplevel(menu_ventana)
    menuSecante.title("Menú de Secante")
    menuSecante.resizable(False, False)
    menuSecante.geometry(menu_ventana.geometry())
    menu_ventana.resizable(False, False)
    menuSecante.configure(bg='lightblue')
    menu_ventana.withdraw()
    
    #ESTILOS DEL TITULO
    estilo_label = {
    'font': ['Arial', 15, 'bold'],
    'foreground': 'white',
    'background': 'black',
    'padx': 300,
    'pady': 5
    }
    text = Label(menuSecante, text="METODO DE LA SECANTE", **estilo_label)
    text.place(relx=0.5, rely=0.08, anchor='center')
    
    #ENTRADA DE LA FUNCION
    #funcion=ttk.Entry(menuSecante,width=40)
    #funcion.pack()

    #BOTON GENERAR GRAFICA 
    #generacionGrafica=ttk.Button(menuSecante, text="Generar grafica", command=lambda:crearGrafica(funcion.get()))
    #generacionGrafica.pack()

    # BOTON VOLVER AL MENU
    volverAlMenu = ttk.Button(menuSecante, text="Volver al Menú", command=lambda: volver_a_menu(menu_ventana, menuSecante))
    volverAlMenu.place(relx=0.08, rely=0.94, anchor='center')
