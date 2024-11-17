import numpy as np
    
def create_empty_poly1d(degree):
    return np.poly1d(np.zeros(degree+1))

def update_coefficient(poly, index, value):
    poly[index] = value
    return poly

def display_polynomial(poly):
    print('current polynomial: ')
    print(poly,'\n')

def loading_coefs():
    degree = int(input('give the degree of the polynomial: '))
    polynomial = create_empty_poly1d(degree)
    while True:
        display_polynomial(polynomial)
        try:
            index = int(input(f'enter the index of the coefficient you want to change from 0 to {degree} or -1 to exit: '))
        except ValueError:
            print('index must be a integer')
            continue
        if index == -1:
            break
        if 0 <= index <= degree:
            try:
                value = float(input(f"Enter a new value for the x^{index} factor: "))
                polynomial = update_coefficient(polynomial, index, value)
            except ValueError:
                print('value must be a number(float)')
                continue
        else:
            print(f"index must be from 0 to {degree}")
    return polynomial

if __name__ == "__main__":
    loading_coefs()