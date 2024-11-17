import numpy as np
import plotly.graph_objects as go
import sys

sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from format_poly import format_poly

def draw_graph(roots,poly):
    x = np.linspace(-1000, 1000, 200000)
    y = poly(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x)'))
    fig.update_layout(
        title=f"polynomial graph with the formula f(x)={format_poly(poly)}",
        xaxis_title="x",
        yaxis_title="f(x)"
    )
    if len(roots) > 0:
        fig.add_trace(go.Scatter(
            x=roots,
            y=[0] * len(roots),
            mode='markers',
            marker=dict(color='red', size=10),
            name='Zero places'
        ))
    fig.show()