import math
#DEFINIMOS LA FUNCION f(X) = EXP(X) - EXP (-X) - 2
# Función común para evaluar f(x)
def evaluarFuncion(x):
    return math.exp(x) - math.exp(-x) - 2
#DEFINIMOS EL METODO EN ESTE CASO "SECANTE" Y LOS DATOS DE ENTRADA
def secante():
    x0 = 0
    x1 = 1
    error_tol = 0.001
    max_iterations = 100
    iteration = 0
#CICLO PARA EL CALCULO DE LAS ITERACIONES Y EL ERROR 
    while iteration < max_iterations:
        x2 = x1 - evaluarFuncion(x1) * (x1 - x0) / (evaluarFuncion(x1) - evaluarFuncion(x0))
        error = abs(x2 - x1)

        print(f"Iteración {iteration + 1}: x = {x2}, Error ≈ {error}")

        if error < error_tol:
            print(f"Solución aproximada encontrada: x ≈ {x2}")
            return x2

        x0, x1 = x1, x2
        iteration += 1
#IMPRIMO EL RESULTADO DE LAS ITERACIONES, ASI COMO TAMBIEN SU RAIZ APROXIMADA
    print("El método de la secante no convergió después de", max_iterations, "iteraciones.")
    return None

