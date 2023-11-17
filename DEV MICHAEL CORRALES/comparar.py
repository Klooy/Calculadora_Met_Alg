#SCRIPT PARA COMPARAR LOS METODOS ALGORTIMICOS
#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576

import math

# Define la función f(x)
def evaluarFuncion(x):
    return math.exp(x) - math.exp(-x) - 2

# Método de Bisección
def biseccion():
    a = 0
    b = 1
    error = 0.001
    iteracion = 0
    while (b - a) / 2 > error:
        m = (a + b) / 2
        f_a = evaluarFuncion(a)
        f_b = evaluarFuncion(b)
        f_m = evaluarFuncion(m)
        if f_a * f_m < 0:
            b = m
        else:
            a = m
        iteracion += 1
    return m, iteracion

# Método de Falsa Posición
def falsa_posicion():
    a = 0
    b = 1
    err = 0.001
    iteracion = 0
    xiAnterior = 0
    while True:
        f_a = evaluarFuncion(a)
        f_b = evaluarFuncion(b)
        xi = a - ((b - a) / (f_b - f_a)) * f_a
        f_xi = evaluarFuncion(xi)
        if f_a * f_xi < 0:
            b = xi
        else:
            a = xi
        iteracion += 1
        if iteracion > 1 and abs(xi - xiAnterior) < err:
            break
        xiAnterior = xi
    return xi, iteracion

# Método de Secante
def secante():
    x0 = 0
    x1 = 1
    error_tol = 0.001
    iteration = 0
    while True:
        x2 = x1 - evaluarFuncion(x1) * (x1 - x0) / (evaluarFuncion(x1) - evaluarFuncion(x0))
        if abs(x2 - x1) < error_tol:
            break
        x0, x1 = x1, x2
        iteration += 1
    return x2, iteration

# Método de Newton-Raphson
def newton_raphson():
    x0 = 0
    e = 0.001
    count = 0
    while True:
        x1 = x0 - (evaluarFuncion(x0) / (math.exp(x0) + math.exp(-x0)))
        count += 1
        if abs(x1 - x0) < e:
            break
        x0 = x1
    return x1, count

# Genera la tabla con los resultados de los métodos
def generar_tabla():
    print("Método\t\tRaíz Aproximada\tIteraciones")
    print("="*45)

    # Bisección
    biseccion_result, biseccion_iters = biseccion()
    print(f"Bisección\t{biseccion_result:.6f}\t\t{biseccion_iters}")

    # Falsa Posición
    falsa_posicion_result, falsa_posicion_iters = falsa_posicion()
    print(f"Falsa Posición\t{falsa_posicion_result:.6f}\t\t{falsa_posicion_iters}")

    # Secante
    secante_result, secante_iters = secante()
    print(f"Secante\t\t{secante_result:.6f}\t\t{secante_iters}")

    # Newton-Raphson
    newton_result, newton_iters = newton_raphson()
    print(f"Newton-Raphson\t{newton_result:.6f}\t\t{newton_iters}")

    # Determina el mejor método
    resultados = {
        "Bisección": (biseccion_result, biseccion_iters),
        "Falsa Posición": (falsa_posicion_result, falsa_posicion_iters),
        "Secante": (secante_result, secante_iters),
        "Newton-Raphson": (newton_result, newton_iters)
    }
    mejor_metodo = min(resultados, key=lambda metodo: resultados[metodo][0])

    print(f"\nEl mejor método es: {mejor_metodo} con una raíz aproximada de {resultados[mejor_metodo][0]:.6f} y {resultados[mejor_metodo][1]} iteraciones")

