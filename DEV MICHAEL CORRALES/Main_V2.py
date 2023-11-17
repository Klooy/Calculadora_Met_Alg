#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576
#SCRIPT PRINCIPAL MENU DE OPCIONES

#IMPORTO LOS METODOS ALGORITMICOS
import biseccion
import falsa_posicion
import secante
import newton_raphson
import comparar
import visualizar_grafica
import matplotlib.pyplot as plt
import numpy as np
import math

# NOTA: PARA HACER USO DEL MENU DEBE TENER LAS LIBRERIAS CORRESPONDIENTES
# pip install matplotlib numpy
# pip install math

#CICLO PARA LA EJECUCION DEL "MENU METODOS" 
while True:
    print("\nSelecciona un método:")
    print("1. Visualizar Gráfica")
    print("2. Bisección")
    print("3. Falsa Posición")
    print("4. Secante")
    print("5. Newton-Raphson")
    print("6. Comparar Métodos")
    print("7. Salir")
#SOLICITA EL METODO QUE QUIERO EJECUTAR
    opcion = input("Ingresa el número de método o 7 para salir: ")
#CONDICION PARA EJECUTAR EL METODO
    if opcion == '1':
        print("Visualizando Gráfica:")
        visualizar_grafica.visualizar_grafica()
    elif opcion == '2':
        print("Método de Bisección:")
        biseccion.biseccion()
    elif opcion == '3':
        print("Método de Falsa Posición:")
        falsa_posicion.falsa_posicion()
    elif opcion == '4':
        print("Método de la Secante:")
        secante.secante()
    elif opcion == '5':
        print("Método de Newton-Raphson:")
        newton_raphson.newton_raphson()
    elif opcion == '6':
        print("Comparar Métodos:")
        comparar.generar_tabla()
    elif opcion == '7':
        break
    else:
        print("Opción no válida. Por favor, selecciona un método válido.")