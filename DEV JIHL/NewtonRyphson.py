import math

#FUNCION NEWTON RYPHSON
def f_fx(x):
    y = ((1/math.exp(x))) - x
    return  y

#FUNCION NEWTON RYPHSON DERIVADA
def f_ffx(x):
    y1 = (-math.exp(-x)) - 1
    return  y1

#FUNCION
def f_x2(x):
    xi = x - (fx/ffx)
    return xi

#CALCULAR ERROR
def f_error(x,xi):
    e = abs((xi - x)/abs(xi))
    return e


#Datos
i = 0
x = float(input('Ingrese el valor de x{i}: '))
err= float(input('digite el error: '))
errorCalculado=100
iteracion=1;
xiAnterior=0;
i = i+1
while errorCalculado>err:

   fx =  f_fx(x);
   ffx = f_ffx(x);
   xi = f_x2(x);
   e = f_error(x,xi);
   

   if fx*xi >0:
        x = xi
    
  
        
        
   if iteracion>0:
        errorCalculado=e
    
    
   print('---------------------')
   print(f'Iteracion:{iteracion}')
   print(f'El valor de la fx es: {fx}')
   print(f'El valor de la ffx es: {ffx}')
   print(f'El valor de la x{i} es: {xi}')
   print(f'El valor del porcentaje de error  es: {e}')
   iteracion=iteracion+1
   

print('---------------------')
print(f'La solucion es: {x}')
