import numpy as np
import sys
import plotly.graph_objects as go
from .graph_deri1 import draw_graph1 
  
sys.path.append(r'C:\Users\Filip\Desktop\np_calc')
from loading_coefs import loading_coefs 
from format_poly import format_poly 

def chuj():
    print('2')

def finding_critical_points(poly, deri_roots):
    critical_points = [(x, poly(x)) for x in deri_roots]

    if len(critical_points) > 0:
        min_point = min(critical_points, key=lambda item: item[1])
        max_point = max(critical_points, key=lambda item: item[1])
        return list(min_point), list(max_point)
    else:
        return [], []

def set_min_or_max(deri_roots,poly):
    if poly(deri_roots[0] + 1) > poly(deri_roots[0]):
        return -1
    else:
        return 1

def print_deri_and_poly(poly, deripoly, min_, max_, ch):
    print(f'polynomial formula f(x)={format_poly(poly)}','\n')
    print(f'dariative formula f(x)={format_poly(deripoly)}')
    if min_ == max_:
        if ch == -1:
            print(f'polynomial have local minimum in  {min_[0]}  and the value for this point is  {min_[1]}')
        elif ch == 1:
            print(f'polynomial have local maximum in  {max_[0]}  and the value for this point is  {max_[1]}')
    else:
        print(f'polynomial have local minimum in  {min_[0]}  and the value for this point is  {min_[1]}')
        print(f'polynomial have local maximum in  {max_[0]}  and the value for this point is  {max_[1]}')

def derivative():
    poly = loading_coefs()
    deri_poly = np.polyder(poly)
    print(deri_poly)
    deri_roots = np.roots(deri_poly)
    if np.any(np.iscomplex(deri_roots)):
        elements_choice = input('do you want to display complex elements? [Y/N]')
        if elements_choice.lower() == 'n':
            deri_roots = deri_roots[np.isreal(deri_roots)].real

    min_ , max_ = finding_critical_points(poly, deri_roots)
    ch = 0
    if len(min_)> 0 or len(max_)> 0:
        if min_ == max_:
            ch = set_min_or_max(deri_roots, poly)
            if ch == -1:
                print('min w punkcie', min_)
            elif ch == 1:
                print('max w punkcie ', max_)
    
    print_deri_and_poly(poly, deri_poly, min_, max_, ch)
    if np.any(np.iscomplex(deri_roots)):
        print('cant draw a graph because there are imaginary roots')
    else:
        choice = input('want to draw a graph? [Y/N]: ')
        if choice.lower() == 'y':
            draw_graph1(poly, min_, max_,ch, deri_poly, deri_roots)
        else:
            return
    
if __name__ == '__main__':
    derivative()