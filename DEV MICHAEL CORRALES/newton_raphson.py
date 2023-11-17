#SCRIPT PARA EJECUTAR EL METODO DE NEWTON RAPHSON
#DEV MICHAEL FELIPE CORRALES FLOREZ - 1007423576
import math
#DEFINIMOS EL METODO EN ESTE CASO "NEW_RAPHSON" Y LOS DATOS DE ENTRADA
def newton_raphson():
    x0 = 0
    e = 0.001
#DEFINIMOS LA FUNCION f(X) = EXP(X) - EXP (-X) - 2
    def evaluarFuncion(x):
        return math.exp(x) - math.exp(-x) - 2
#DEFINIMOS LA DERIVADA DE LA FUNCION f'(X) = EXP(X) + EXP (-X) 
    def func_prime(x):
        return math.exp(x) + math.exp(-x)

    x1 = x0 - (evaluarFuncion(x0) / func_prime(x0))
    count = 0
#CICLO PARA EL CALCULO DEL ERROR Y LAS ITERACIONES
    while abs(x1 - x0) > e:
        x0 = x1
        x1 = x0 - (evaluarFuncion(x0) / func_prime(x0))
        count += 1
        error = abs((x1 - x0) / x1)
#IMPRIMO LOS RESULTADOS DE LAS ITERACIONES
        print(f"Iteración: {count}, Xi: {x0}, f(Xi): {evaluarFuncion(x0)}, f'(Xi): {func_prime(x0)}, Xi+1: {x1}, Error: {error}")

    print(f"La raíz de la ecuación es aproximadamente: {x1}")
