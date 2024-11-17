import numpy as np
import plotly.graph_objects as go
from .graph_deri2 import draw_graph2  
import sys

sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from format_poly import format_poly


def draw_graph1(poly, min_, max_,ch, deri_poly, deri_roots):
    x = np.linspace(-1000, 1000, 200000)
    y = poly(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, 
        y=y, 
        mode='lines', 
        name='polinominal'
        ))
    fig.update_layout(
        title=f"f(x)={format_poly(poly)}         f'(x)={format_poly(deri_poly)}",
        xaxis_title="x",
    )
    
    if min_ == max_:
        if ch == -1:
            fig.add_trace(go.Scatter(
                x = [min_[0]],
                y = [min_[1]],
                mode='markers',
                marker=dict(color='red', size=10),
                name='local minimum'
            ))
            
        if ch == 1:
            fig.add_trace(go.Scatter(
                x = [max_[0]],
                y = [max_[1]],
                mode='markers',
                marker=dict(color='blue', size=10),
                name='local maximum'            
            ))
    else:
        fig.add_trace(go.Scatter(
                x = [min_[0]],
                y = [min_[1]],
                mode='markers',
                marker=dict(color='red', size=10),
                name='local minimum'
            ))
        fig.add_trace(go.Scatter(
                x =[max_[0]],
                y =[max_[1]],
                mode='markers',
                marker=dict(color='blue', size=10),
                name='local maximum'            
            ))
    fig = draw_graph2(deri_poly, deri_roots, fig)
    fig.show()