import re
import math

def formatearFuncion(expresion, x=0):
    expresion = expresion.replace('e', '2.71828')
    expresion = expresion.replace('^', '**')
 
    
    # Patrones para encontrar 'sin(expresion_adentro)', 'cos(expresion_adentro)', 'tan(expresion_adentro)', 'ln(expresion_adentro)' dentro de la expresión
    patron_seno = r'sin\((.*?)\)'
    patron_coseno = r'cos\((.*?)\)'
    patron_tangente = r'tan\((.*?)\)'
   
    
    # Funciones para reemplazar las funciones trigonométricas y el logaritmo
    def reemplazar_seno(match):
        expresion_adentro = match.group(1)
        return f'math.sin({expresion_adentro})'
    
    def reemplazar_coseno(match):
        expresion_adentro = match.group(1)
        return f'math.cos({expresion_adentro})'
    
    def reemplazar_tangente(match):
        expresion_adentro = match.group(1)
        return f'math.tan({expresion_adentro})'
    
 

    # Reemplazar las funciones por sus equivalentes de math
    expresion = re.sub(patron_seno, reemplazar_seno, expresion)
    expresion = re.sub(patron_coseno, reemplazar_coseno, expresion)
    expresion = re.sub(patron_tangente, reemplazar_tangente, expresion)
 
    return expresion
