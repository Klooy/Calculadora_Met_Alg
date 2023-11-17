import math

#FUNCION BISECCION
def f_biseccion(x):
    bi = math.cos (2/x) - 2 * math.sin (1/x) + (1/x)
    return bi

#CALCULAR PUNTO MEDIO
def f_puntoMedio(a,b):
    m = ((a + b)/2)
    return m

#CALCULAR ERROR
def f_error(b,a):
    e = ((b-a)/2)
    return e


#Datos
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
err=float(input('digite el error: '))
errorCalculado=100
iteracion=1;
xnAnterior=0;

while errorCalculado>err:

   m =  f_puntoMedio(a,b);
   fa = f_biseccion(a);
   fb = f_biseccion(b);
   fm = f_biseccion(m);
   e = f_error(b,a);

   if fa*fm <0:
        a=a
        b=m
   else:
        a=m
        b=b
        
   if iteracion>0:
        errorCalculado=e
    
    
   print('---------------------')
   print(f'Iteracion:{iteracion}')
   print(f'El valor del punto medio es: {m}')
   print(f'El valor de la fa es: {fa}')
   print(f'El valor de la fb es: {fb}')
   print(f'El valor de la fm es: {fm}')
   print(f'El valor del porcentaje de error  es: {e}')
   iteracion=iteracion+1

print('---------------------')
print(f'La solucion es: {m}')
