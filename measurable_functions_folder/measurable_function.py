import numpy as np
import sys  
import plotly.graph_objects as go

sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from loading_coefs import loading_coefs
from format_poly import format_poly

def loading_numerator_and_denominator():
    print("state how many polynomials there will be in the numerator and how many in the denominator")
    while True:
        try:
            numerator = int(input('numerator: '))
            break
        except ValueError:
            print('numerator must be a number')
            continue
    while True:
        try:
            denominator = int(input('denominator: '))
            break
        except ValueError:
            print('denominatorr must be a number')
    numerators = np.poly1d([1])
    for i in range(numerator):
        print(f'coefficients for {i+1} polynomial in numerator')
        numerators = numerators * loading_coefs()
    denominators = np.poly1d([1])
    for i in range(denominator):
        print(f'coefficients for {i+1} polynomial in denominator')
        denominators = denominators * (loading_coefs())
    return numerators, denominators

def masking_x(denominator_roots):
    x = np.linspace(-1000,1000,200000)
    if len(denominator_roots) > 0:
        for root in denominator_roots:
            mask = (root + 1e-8 < x) &  (root -1e-8 > x)
            x = x[~mask]
    return x

def draw_graph(numerator, denominator, function_roots,denominator_roots):
    fig = go.Figure()
    x = masking_x(denominator_roots)
    y = numerator(x)/denominator(x)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='f(x)/g(x)'
    ))
    if len(denominator_roots) > 0:
        for i in range(len(denominator_roots)):
            fig.add_trace(go.Scatter(
                x = [denominator_roots[i]]*2,
                y = [-1000,1000],
                mode='lines',
                name=f'asymptote{i+1}; x={denominator_roots[i]}'
            ))
    if len(denominator_roots) > 0:
        for i in range(len(function_roots)):
            fig.add_trace(go.Scatter(
                x = [function_roots[i]],
                y = [numerator(function_roots[i])/denominator(function_roots[i])],
                mode='markers',
                marker=dict(
                    color='red',
                    size =10,
                ),
                name=f'zero place{i+1} ; x={function_roots[i]}'
            ))
    fig.update_layout(
        title = fr"$f(x)=\frac{{{format_poly(numerator)}}}{{{format_poly(denominator)}}}$ -graph of a rational function",
        xaxis_title="x",  
        yaxis_title="f(x)/g(x)",  
    )
    fig.show()

def measurable_function():
    numerator  ,denominator = loading_numerator_and_denominator()
    function_roots = np.roots(numerator).round(4)
    function_roots = function_roots[np.isreal(function_roots)].real
    denominator_roots = np.roots(denominator).round(4)
    function_roots = function_roots[~np.isin(function_roots, denominator_roots)]
    print(denominator_roots)
    draw_graph(numerator, denominator, function_roots,denominator_roots)

if __name__ == '__main__':
    measurable_function()