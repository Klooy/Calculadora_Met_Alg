import math

#FUNCION FALSA POSICION
def Funcion(x):
    respuesta = math.exp(3 * x) - 4
    return respuesta

# CALCULAR XI 
def Xi(a, b, f_a, f_b):
    xi = (a * f_b - b * f_a) / (f_b - f_a)
    return xi

# DATOS
a = float(input('digite a: '))
b = float(input('digite b: '))
err = float(input('digite el error: '))
errorCalculado = 100
iteracion = 0
xiAnterior = 0

# ITERACIONES
while errorCalculado > err:
    f_a = Funcion(a)
    f_b = Funcion(b)
    xi = Xi(a, b, f_a, f_b)
    f_xi = Funcion(xi)
    if f_a * f_xi < 0:
        b = xi
    else:
        a = xi
    if iteracion > 0:
        errorCalculado = xi - xiAnterior
    xiAnterior = xi
    iteracion += 1
    

    print('---------------------')
    print(f'Iteracion: {iteracion}')
    print(f'f(a)= {f_a}')
    print(f'f(b)= {f_b}')
    print(f'xi: {xi}')
    print(f'f(xi)= {f_xi}')
    print(f'errorCalculado: {errorCalculado}')

print('---------------------')
print(f'La solucion es: {xi}')
