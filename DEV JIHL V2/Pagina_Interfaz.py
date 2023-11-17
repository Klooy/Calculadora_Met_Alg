from tkinter import *

def ventana1():
    global ventana1
    ventana1 =Tk()
    ventana1.geometry("650x400")
    ventana1.title("Pagina Principal")
    miImagen=PhotoImage(file="logo.png")

    Label(ventana1, text="Bienvenidos", fg="Black", font=("Comic Sans MS", 18)).place(x=255, y=0)
    Label(ventana1, image=miImagen).place(x=530, y=0)

    Label(ventana1, text="Bienvenidos a la calculadora de funciones algoritmicas de los metodos", fg="Black").place(x=50, y=180)
    Label(ventana1, text="Donde se podra resover los Metodos de Bisecccion,Falsa Posicion,Secante y Newton Ryphosn", fg="Black").place(x=50, y=200)

    Button(ventana1, text="Iniciar", command=ventana2).place(x=315, y=300)
    
    ventana1.mainloop()


def ventana2():

    ventana2 = Toplevel(ventana1) #Crear la ventana siguiente
    ventana2.geometry("650x400")
    ventana2.title("Pagina Metodos")
    miImagen=PhotoImage(file="logo.png")

    Label(ventana2, text="Metodos Algoritmicos", fg="Black", font=("Comic Sans MS", 24)).place(x=150, y=0)
    Label(ventana2, image=miImagen).place(x=530, y=0)

    Button(ventana2, text="Volver", command=volver_ventana).place(x=50, y=370)
    Button(ventana2, text="Salir", command=ventana2).place(x=550, y=370)
    Button(ventana2, text="Metodo de Bisecicon", command=ventana3).place(x=50, y=140)
    Button(ventana2, text="Metodo Secante", command=ventana4).place(x=500, y=140)
    Button(ventana2, text="Metodo de Falsa Posicion", command=ventana5).place(x=50, y=250)
    Button(ventana2, text="Metodo de Newton Ryphson", command=ventana6).place(x=460, y=250)
    if(ventana2):
        ventana1.withdraw()


    ventana2.mainloop()

def ventana3():
    ventana3 = Toplevel() #Crear la ventana siguiente
    ventana3.geometry("650x400")
    ventana3.title("Metodo de Biseccion")
    miImagen=PhotoImage(file="logo.png")
    
    Label(ventana3, text="Digitaliza los Datos", fg="Black", font=("Comic Sans MS", 24)).place(x=200, y=0)
    Label(ventana3, image=miImagen).place(x=530, y=0)
    
    Label(ventana3, text="Ingrese la funcion", fg="Black").place(x=0, y=80)
    cuadro_Funcion=Entry(ventana3).place(x=110, y=80)
    
    Label(ventana3, text="Ingrese Valor de A", fg="Black").place(x=0, y=110)
    cuadro=Entry(ventana3).place(x=110, y=110)
    
    Label(ventana3, text="Ingrese Valor de B", fg="Black").place(x=0, y=140)
    cuadro=Entry(ventana3).place(x=110, y=140)

    Label(ventana3, text="Ingrese Valor de Porcentaje de Error", fg="Black").place(x=0, y=170)
    cuadro=Entry(ventana3).place(x=200, y=170)

    Button(ventana3, text="Ingresar", command=ventana3).place(x=50, y=200)
    Button(ventana3, text="Regresar", command=ventana2).place(x=130, y=200)
    Button(ventana3, text="Salir", command=ventana3).place(x=200, y=200)
    
    ventana3.mainloop()

def ventana4():
    ventana4 = Toplevel() #Crear la ventana siguiente
    ventana4.geometry("650x400")
    ventana4.title("Metodo Secante")
    miImagen=PhotoImage(file="logo.png")

    Label(ventana4, text="Digitaliza los Datos", fg="Black", font=("Comic Sans MS", 24)).place(x=200, y=0)
    Label(ventana4, image=miImagen).place(x=530, y=0)
    
    Label(ventana4, text="Ingrese la funcion", fg="Black").place(x=0, y=80)
    cuadro_Funcion=Entry(ventana4).place(x=110, y=80)
    
    Label(ventana4, text="Ingrese Valor de X", fg="Black").place(x=0, y=110)
    cuadro=Entry(ventana4).place(x=110, y=110)
    
    Label(ventana4, text="Ingrese Valor de Porcentaje de Error", fg="Black").place(x=0, y=140)
    cuadro=Entry(ventana4).place(x=200, y=140)

    Button(ventana4, text="Ingresar", command=ventana4).place(x=50, y=200)
    Button(ventana4, text="Regresar", command=ventana2).place(x=130, y=200)
    Button(ventana4, text="Salir", command=ventana4).place(x=200, y=200)


    ventana4.mainloop()

def ventana5():
    ventana5 = Toplevel() #Crear la ventana siguiente
    ventana5.geometry("650x400")
    ventana5.title("Metodo de Falsa Posicion")
    miImagen=PhotoImage(file="logo.png")

    Label(ventana5, text="Digitaliza los Datos", fg="Black", font=("Comic Sans MS", 24)).place(x=200, y=0)
    Label(ventana5, image=miImagen).place(x=530, y=0)
    
    Label(ventana5, text="Ingrese la funcion", fg="Black").place(x=0, y=80)
    cuadro_Funcion=Entry(ventana5).place(x=110, y=80)
    
    Label(ventana5, text="Ingrese Valor de X", fg="Black").place(x=0, y=110)
    cuadro=Entry(ventana5).place(x=110, y=110)
    

    Label(ventana5, text="Ingrese Valor de Porcentaje de Error", fg="Black").place(x=0, y=140)
    cuadro=Entry(ventana5).place(x=200, y=140)

    Button(ventana5, text="Ingresar", command=ventana5).place(x=50, y=200)
    Button(ventana5, text="Regresar", command=ventana2).place(x=130, y=200)
    Button(ventana5, text="Salir", command=ventana5).place(x=200, y=200)

    ventana5.mainloop()

def ventana6():
    ventana6 = Toplevel() #Crear la ventana siguiente
    ventana6.geometry("650x400")
    ventana6.title("Metodo de Newton Ryphson")
    miImagen=PhotoImage(file="logo.png")

    Label(ventana6, text="Digitaliza los Datos", fg="Black", font=("Comic Sans MS", 24)).place(x=200, y=0)
    Label(ventana6, image=miImagen).place(x=530, y=0)
    
    Label(ventana6, text="Ingrese la funcion", fg="Black").place(x=0, y=80)
    cuadro_Funcion=Entry(ventana6).place(x=110, y=80)
    
    Label(ventana6, text="Ingrese Valor de X", fg="Black").place(x=0, y=110)
    cuadro=Entry(ventana6).place(x=110, y=110)
    

    Label(ventana6, text="Ingrese Valor de Porcentaje de Error", fg="Black").place(x=0, y=140)
    cuadro=Entry(ventana6).place(x=200, y=140)

    Button(ventana6, text="Ingresar", command=ventana6).place(x=50, y=200)
    Button(ventana6, text="Regresar", command=ventana2).place(x=130, y=200)
    Button(ventana6, text="Salir", command=ventana6).place(x=200, y=200)


    ventana6.mainloop()

def volver_ventana():
    ventana1.iconify()
    ventana1.deiconify()
   

    
ventana1()







