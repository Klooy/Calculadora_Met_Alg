import re
import math

def formatearFuncion(expresion, x=0):
    expresion = expresion.replace('e', '2.71828')
    expresion = expresion.replace('^', '**')

    # Patrones para encontrar 'sin(expresion_adentro)', 'cos(expresion_adentro)', 'tan(expresion_adentro)', 'ln(expresion_adentro)', 'log(expresion_adentro)', 'sqrt(expresion_adentro)' dentro de la expresión
    patron_seno = r'sin\((.*?)\)'
    patron_coseno = r'cos\((.*?)\)'
    patron_tangente = r'tan\((.*?)\)'
    patron_log = r'log\((.*?)\)'
    patron_sqrt = r'sqrt\((.*?)\)'

    # Funciones para reemplazar las funciones trigonométricas, el logaritmo, y la raíz cuadrada
    def reemplazar_seno(match):
        expresion_adentro = match.group(1)
        return f'math.sin({expresion_adentro})'

    def reemplazar_coseno(match):
        expresion_adentro = match.group(1)
        return f'math.cos({expresion_adentro})'

    def reemplazar_tangente(match):
        expresion_adentro = match.group(1)
        return f'math.tan({expresion_adentro})'

    def reemplazar_log(match):
        expresion_adentro = match.group(1)
        return f'math.log({expresion_adentro})'

    def reemplazar_sqrt(match):
        expresion_adentro = match.group(1)
        return f'math.sqrt({expresion_adentro})'

    # Reemplazar las funciones por sus equivalentes de math
    expresion = re.sub(patron_seno, reemplazar_seno, expresion)
    expresion = re.sub(patron_coseno, reemplazar_coseno, expresion)
    expresion = re.sub(patron_tangente, reemplazar_tangente, expresion)
    expresion = re.sub(patron_log, reemplazar_log, expresion)
    expresion = re.sub(patron_sqrt, reemplazar_sqrt, expresion)

    return expresion

