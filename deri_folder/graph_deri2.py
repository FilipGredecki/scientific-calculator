import numpy as np
import plotly.graph_objects as go

def draw_graph2(deri_poly, deri_roots, fig):
    x = np.linspace(-1000, 1000, 200000)
    y = deri_poly(x)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='deriative', 
        line=dict(
            dash='dash',     
            color='yellow',    
            )))

    if len(deri_roots) > 0:
        fig.add_trace(go.Scatter(
            x = deri_roots,
            y = [0]*len(deri_roots),
            mode='markers',
            marker=dict(color='orange',size=10),
            name='dariative roots'
        ))
    return fig