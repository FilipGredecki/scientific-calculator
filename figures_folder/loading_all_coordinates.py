import numpy as np

def loading_all_coordinates():
    while True:
        try:
            vertices = int(input('enter the number of vertices: '))
            break
        except ValueError:
            print('the number of vertices must be a natural number')
            continue
    x_base = np.zeros(vertices)
    y_base = np.zeros(vertices)
    z_base = np.zeros(vertices)
    print('coordinates for base 1')
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
                z_base[i] = float(input('for z: '))
                break
            except ValueError:
                    print('z must be a number')
                    continue
    x_base = np.append(x_base,x_base[0])
    y_base = np.append(y_base,y_base[0])
    z_base = np.append(z_base,z_base[0])        
    
    x_top = np.zeros(vertices)
    y_top = np.zeros(vertices)
    z_top = np.zeros(vertices)
    print('coordinates for base 2')
    for i in range(vertices):
        print(f'enter the coordinates for vertex {i+1}')
        while True:
            try:
                x_top[i] = float(input('for x: '))
                break
            except ValueError:
                print('x must be a number')
                continue
        while True:
            try:
                y_top[i] = float(input('for y: '))
                break
            except ValueError:
                print('y must be a number')
                continue
        while True:
            try:
                z_top[i] = float(input('for z: '))
                break
            except ValueError:
                    print('height must be a number')
                    continue
    x_top = np.append(x_top,x_top[0])
    y_top = np.append(y_top,y_top[0])
    z_top = np.append(z_top,z_top[0]) 
    return x_base, y_base , z_base, x_top, y_top, z_top