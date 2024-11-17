import numpy as np
import plotly.graph_objects as go
import sys

from .graph_poly import draw_graph
# x^5 - 3x^4 -23x^3 + 51x^2 + 94x - 120

sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from loading_coefs import loading_coefs
from format_poly import format_poly

def dividing_polynomials(poly, roots):
    divided_polynomial = []
    new_poly = poly
    for root in roots:
        divisor = np.poly1d([1, -root])
        divided_polynomial.append(divisor)
        quotient, remainder = np.polydiv(new_poly, divisor)
        new_poly = quotient
    divided_polynomial.append(new_poly)
    return divided_polynomial

def format_poly(poly):
    formated_poly = ''
    for i in range(len(poly)+1):
        coef = poly[i]
        if poly[i]%1 == 0:
            coef = int(coef)
        if coef > 0:
            x = '+'
        else:
            x= ''
        if i == len(poly):
            if poly[i] != 0:
                if i == 0:
                    formated_poly = f'{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'{coef}x' + formated_poly
                else:
                    formated_poly = f'{coef}x^{i}' + formated_poly
        else:
            if poly[i] != 0:
                if i == 0:
                    formated_poly = f'{x}{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'{x}{coef}x' + formated_poly
                else:
                    formated_poly = f'{x}{coef}x^{i}' + formated_poly
        
    return formated_poly

def polynomial():
    poly = loading_coefs()
    roots = np.roots(poly)
    if np.any(np.iscomplex(roots)):
        elements_choice = input('do you want to display complex elements? [Y/N]')
        if elements_choice.lower() == 'n':
            roots = roots[np.isreal(roots)].real
    divided_polynomial = dividing_polynomials(poly, roots)
    d = ''
    for z in divided_polynomial:
        
        d += '('+format_poly(z)+')'
    print(d.replace('\n', '').replace(' ',''))
    
    if np.any(np.iscomplex(roots)):
        print('cant draw a graph because there are imaginary roots')
    else:
        choice = input('want to draw a graph? [Y/N]: ')
        if choice.lower() == 'y':
            draw_graph(roots, poly)
        else:
            return

if __name__ == '__main__':
    polynomial()
