#archivo principal
import Biseccion as ab
import Falsaposicion as ac
import Secante as ad
import NewtonRyphson as af

#Menu de opciones
sigue = 1
while(sigue == 1):
    print("Operaciones De Metodos")
    print("1.Metodo de Biseccion")
    print("2.Metodo de falsa posicion")
    print("3.Metodo de Secante")
    print("4.Metodo de Newton Raphson")
    print("5.Salir")

    opcion = input("\nIngrese opcion: ")

    if(opcion == '1'):
        print("Operacion Metodo de Biseccion")
        a = float(input('Ingrese el valor de a: '))
        b = float(input('Ingrese el valor de b: '))
        err=float(input('digite el error: '))
        res = ab.Biseccion(a,b)
        print(f"El resultado  es {res}")
    elif(opcion == '2'):
        print("Operacion Metodo de Falsa Posicion")
        a = float(input('Ingrese el valor de a: '))
        b = float(input('Ingrese el valor de b: '))
        err=float(input('digite el error: '))
        res = ac.Falsaposicion(a,b)
        print(f"El resultado  es {res}")
    elif(opcion == '3'):
        print("Operacion Metodo de Secante")
        p0 = float(input('Ingrese el valor de a: '))
        p1 = float(input('Ingrese el valor de b: '))
        err=float(input('digite el error: '))
        res = ad.Falsaposicion(p0,p1)
        print(f"El resultado  es {res}")
    elif(opcion == '4'):
        print("Operacion Metodo de Newton Raphson")
        x = float(input('Ingrese el valor de a: '))
        err=float(input('digite el error: '))
        res = af.Falsaposicion(x)
        print(f"El resultado  es {res}")
    else:
        print("Salida de la aplicacion")


print("\n Gracias por utilizar nuestra App")

