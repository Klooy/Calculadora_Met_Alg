import math
#DEFINIMOS LA FUNCION f(X) = EXP(X) - EXP (-X) - 2
def evaluarFuncion(x):
    return math.exp(x) - math.exp(-x) - 2
#DEFINIMOS EL METODO EN ESTE CASO "FALSA_POSICION" Y LOS DATOS DE ENTRADA
def falsa_posicion():
    a = 0
    b = 1
    err = 0.001
    errorCalculado = 100
    iteracion = 0
    xiAnterior = 0
#CICLO PARA EL CALCULO PASO A PASO DE LAS ITERACIONES
    while errorCalculado > err:
        f_a = evaluarFuncion(a)
        f_b = evaluarFuncion(b)
        xi = a - ((b - a) / (f_b - f_a)) * f_a
        f_xi = evaluarFuncion(xi)

        if f_a * f_xi < 0:
            b = xi
        else:
            a = xi

        if iteracion > 0:
            errorCalculado = xi - xiAnterior

        xiAnterior = xi
        iteracion += 1
#IMPRIMO  LOS DATOS RESULTANTES DE CADA ITERACION, ASI COMO SU RAIZ APROXIMAD
        print('---------------------')
        print(f'Iteración: {iteracion}')
        print(f'f(a) = {f_a}')
        print(f'f(b) = {f_b}')
        print(f'xi: {xi}')
        print(f'f(xi) = {f_xi}')
        print(f'Nuevo intervalo = ({a}, {b})')
        print(f'Error calculado: {errorCalculado}')

    print(f'La solución es: {xi}')
