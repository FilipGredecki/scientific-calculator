import numpy as np

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
            x = ''
            if poly[i] == float(1):
                if i == 0:
                    formated_poly = f'{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'x' + formated_poly
                else:
                    formated_poly = f'x^{i}' + formated_poly
            elif poly[i] != float(0):
                if i == 0:
                    formated_poly = f'{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'{coef}x' + formated_poly
                else:
                    formated_poly = f'{coef}x^{i}' + formated_poly
            
        else:
            if poly[i] == float(1):
                if i == 0:
                    formated_poly = f'{x}{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'{x}x' + formated_poly
                else:
                    formated_poly = f'{x}x^{i}' + formated_poly
            elif poly[i] != float(0):
                if i == 0:
                    formated_poly = f'{x}{coef}' + formated_poly
                elif i == 1:
                    formated_poly = f'{x}{coef}x' + formated_poly
                else:
                    formated_poly = f'{x}{coef}x^{i}' + formated_poly 
        
    return formated_poly