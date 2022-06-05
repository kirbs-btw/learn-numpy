import numpy as np

"""
other functions are sinh, cosh and tanh, arcsinh, arccosh, arctanh
"""

def main():

    arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
    print(np.sinh(np.pi/2))
    print(np.cosh(arr))
    print(np.arcsinh(arr))

if __name__ == '__main__':
    main()