#IMPORTO LOS METODOS ALGORITMICOS
import biseccion
import falsa_posicion
import secante
import newton_raphson
#CICLO PARA LA EJECUCION DEL "MENU METODOS" 
while True:
    print("\nSelecciona un método:")
    print("1. Bisección")
    print("2. Falsa Posición")
    print("3. Secante")
    print("4. Newton-Raphson")
    print("5. Salir")
#SOLICITA EL METODO QUE QUIERO EJECUTAR
    opcion = input("Ingresa el número de método o 5 para salir: ")
#CONDICION PARA EJECUTAR EL METODO
    if opcion == '1':
        print("Método de Bisección:")
        biseccion.biseccion()
    elif opcion == '2':
        print("Método de Falsa Posición:")
        falsa_posicion.falsa_posicion()
    elif opcion == '3':
        print("Método de la Secante:")
        secante.secante()
    elif opcion == '4':
        print("Método de Newton-Raphson:")
        newton_raphson.newton_raphson()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, selecciona un método válido.")
