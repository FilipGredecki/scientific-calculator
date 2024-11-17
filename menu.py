import numpy as np
import sys
import plotly.graph_objects as go
sys.path.append(r'C:\Users\Filip\Desktop\np_calc')

from deri_folder.derivative import derivative
from poly_folder.polynomial import polynomial
from figures_folder.figures_3d import figures_3d
from integrals_folder.integrals import integrals
from measurable_functions_folder.measurable_function import measurable_function

def main():
    print('1 for deriative')
    print('2 for polynomial')
    print('3 for 3d figures')
    print('4 for integrals')
    print('5 for measurable functions')
    print('6 to exit')
    while True:
        x = int(input('choice: '))
        if x == 1:
            derivative()
        if x == 2:
            polynomial()
        if x == 3:
            figures_3d()
        if x == 4:
            integrals()
        if x == 5:
            measurable_function()
        if x == 6:
            break
        print('\n')


main()

