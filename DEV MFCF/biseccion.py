import math
#DEFINIMOS LA FUNCION f(X) = EXP(X) - EXP (-X) - 2
def evaluarFuncion(x):
    return math.exp(x) - math.exp(-x) - 2
#DEFINIMOS EL METODO EN ESTE CASO "BISECCION" Y LOS DATOS DE ENTRADA
def biseccion():
    a = 0
    b = 1
    error = 0.001
    errorCalculado = 100
    iteracion = 0
#CICLO PARA EL CALCULO DEL ERROR PASO A PASO EN BISECCION
    while errorCalculado > error:
        m = (a + b) / 2
        f_a = evaluarFuncion(a)
        f_b = evaluarFuncion(b)
        f_m = evaluarFuncion(m)

        if f_a * f_m < 0:
            b = m
        else:
            a = m

        if iteracion > 0:
            errorCalculado = (b - a) / 2

        iteracion += 1
#IMPRIMO EL PASO A PASO DE CADA ITERACION Y EL ERROR APROXIMADO
        print('---------------------')
        print(f'Iteración: {iteracion}')
        print(f'm: {m}')
        print(f'f(a) = {f_a}')
        print(f'f(b) = {f_b}')
        print(f'f(m) = {f_m}')
        print(f'Nuevo intervalo = ({a}, {b})')
        print(f'Error calculado: {errorCalculado}')

    print(f'La solución es: {m}')
