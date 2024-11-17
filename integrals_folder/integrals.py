import numpy as np
import sys  
import plotly.graph_objects as go

sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from loading_coefs import loading_coefs
from format_poly import format_poly

def calculating_the_integral(coefs):
    integral_coefs = []
    for i in range(len(coefs)+1):
        z = coefs[i]/(i + 1)
        integral_coefs.insert(0, z)
    integral_coefs.append(0)
    return np.poly1d(integral_coefs)

def print_integral(coefs, integral_coefs):
    print(f" function f'(x)={format_poly(coefs)}")
    print(f"indefinite integral ∫f'(x)={format_poly(integral_coefs)}+C")

def calculate_the_definite_integral(integral_coefs,a,b):
    definited_integral = integral_coefs(a) - integral_coefs(b)
    print('the definite integral is equal', definited_integral)

def draw_integral_graph(integral_coefs,c):
    fig = go.Figure()
    integral_coefs[0] = c
    x = np.linspace(-1000,1000,200000)
    y = integral_coefs(x)
    fig.add_trace(go.Scatter(x = x, y = y, mode='lines'))
    fig.show()

def integrals():
    coefs = loading_coefs()
    integral_coefs = calculating_the_integral(coefs)
    
    print_integral(coefs, integral_coefs)
    if input('if you want calculate definite integral press Y: ').lower() == 'y':
        while True:
            try:
                a = float(input('enter a value for a: '))
                break
            except ValueError:
                print('a must be a number')
                continue
        while True:
            try:
                b = float(input('enter a value for b: '))
                break
            except ValueError:
                print('b must be a number')
                continue
        calculate_the_definite_integral(integral_coefs, a, b)
    if input('if you want draw graph press Y').lower() == 'y':
        while True:
            try:
                c = float(input('enter a value for c (integration constant): '))
                break
            except ValueError:
                print('c must be a number')
                continue
        draw_integral_graph(integral_coefs, c)
    
if __name__ == '__main__':
    integrals()