import numpy as np
import plotly.graph_objects as go

from .loading_all_coordinates import loading_all_coordinates

def loading_values():
    while True:
        try:
            vertices= int(input('enter the number of vertices: '))
            break
        except ValueError:
            print('the number of vertices must be a natural number')
            continue
    while True:
        try:
            height = float(input('enter the height of the figure: '))
            break
        except ValueError:
            print('height must by a number')
            continue
    while True:
        try:
            base_radius = float(input('enter the radius of the circle in which the attitude will be described: '))
            break
        except ValueError:
            print('radius must by a number')
            continue
    return vertices, height, base_radius

def loading_base_coordinates():
    while True:
        try:
            vertices = int(input('enter the number of vertices: '))
            break
        except ValueError:
            print('the number of vertices must be a natural number')
            continue
    x_base = np.zeros(vertices)
    y_base = np.zeros(vertices)
    for i in range(vertices):
        print(f'enter the coordinates for vertex {i+1}')
        while True:
            try:
                x_base[i] = float(input('for x: '))
                break
            except ValueError:
                print('x must be a number')
                continue
        while True:
            try:
                y_base[i] = float(input('for y: '))
                break
            except ValueError:
                print('y must be a number')
                continue
    while True:
            try:
                height = float(input('enter the height of the figure: '))
                break
            except ValueError:
                print('height must be a number')
                continue
    x_base = np.append(x_base, x_base[0])
    y_base = np.append(y_base, y_base[0])
    z_base = np.zeros(vertices+1)
    z_top = np.full_like(z_base, height)
    x_top = x_base
    y_top = y_base
    return x_base, y_base , z_base, x_top, y_top, z_top

def creating_coordinates():
    vertices, height, base_radius = loading_values()
    theta = np.linspace(0, (2 * np.pi), vertices, endpoint=False)
    x_base = base_radius * np.cos(theta)
    y_base = base_radius * np.sin(theta)
    z_base = np.zeros(vertices+1)
    x_base = np.append(x_base,x_base[0])
    y_base = np.append(y_base,y_base[0])
    z_top = np.full_like(z_base, height)
    x_top = x_base
    y_top = y_base
    return x_base, y_base , z_base, x_top, y_top, z_top
    
def draw_figure(x_base, y_base , z_base, x_top, y_top, z_top):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x_base, y=y_base, z=z_base, mode='lines', name='bot', line=dict(color='blue')))
    fig.add_trace(go.Scatter3d(x=x_top, y=y_top, z=z_top, mode='lines', name='top', line=dict(color='green')))
    for i in range(len(x_base)-1):
        x = [x_base[i],x_top[i]] 
        y = [y_base[i],y_top[i]] 
        z = [z_base[i],z_top[i]]
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', showlegend=False,line=dict(color='red')))
    fig.update_layout(scene=dict(aspectmode='cube'))
    fig.show()

def figures_3d():
    print('what do you want to do?')
    print('draw a figure with a regular base [1]')
    print('provide the base coordinates yourself [2]')
    print('provide all the coordinates yourself[3]')
    while True:
        try:
            choice = int(input('give a nummber: '))
            break
        except ValueError:
            continue
    if choice == 1:
        x_base, y_base , z_base, x_top, y_top, z_top = creating_coordinates()
        draw_figure(x_base, y_base , z_base, x_top, y_top, z_top)
    if choice == 2:
        x_base, y_base , z_base, x_top, y_top, z_top = loading_base_coordinates()
        draw_figure(x_base, y_base , z_base, x_top, y_top, z_top)
    if choice == 3:
        x_base, y_base , z_base, x_top, y_top, z_top = loading_all_coordinates()
        draw_figure(x_base, y_base , z_base, x_top, y_top, z_top)

if __name__ == '__main__':
    figures_3d()