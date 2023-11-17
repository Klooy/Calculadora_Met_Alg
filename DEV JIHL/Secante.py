import math

#FUNCION SECANTE
def f_fx(x):
    y = y = x - 0.8 - 0.2*math.sin(x);
    return  y


#FUNCION
def f_x1(x0, x1, p0, p1):
    x0 = p1 - (x1*(p1-p0))/(x1-x0)
    return x0



#CALCULAR ERROR
def f_error(fx0,x1):
    e = abs((fx0 - x1)/abs(fx0))
    return e


#Datos
i = 0
p0 = float(input('Ingrese el valor de x{i}: '))
p1 = float(input('Ingrese el valor de x{i}: '))
err= float(input('digite el error: '))
errorCalculado=100
iteracion=1;
xiAnterior=0;
i = i+1
while errorCalculado>err:

    x0 =  f_fx(p0);
    x1 =  f_fx(p1);
    fx0 = f_x1(x0,x1,p0,p1);
    e = f_error(fx0,x1);
   

    if x0*fx0 < 0:
      p0 = p1
      p1 = fx0
    
  
        
        
    if iteracion>0:
       errorCalculado=e
    
    
    print('---------------------')
    print(f'Iteracion:{iteracion}')
    print(f'El valor de la x0 es: {x0}')
    print(f'El valor de la x1 es: {x1}')
    print(f'El valor de la fx0 es: {fx0}')
    print(f'El valor del porcentaje de error  es: {e}')
    iteracion=iteracion+1
   

print('---------------------')
print(f'La solucion es: {fx0}')
