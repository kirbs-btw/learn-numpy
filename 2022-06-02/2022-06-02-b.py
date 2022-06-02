import numpy as np

"""
to compare for the type use np.ufunc

simple arithmetic is applied to the elements next to each other 

[1, 2, 3, 4]
[5, 6, 7, 8]

1 + 5 = 6
2 + 6 = 8
...

"""


def comp():
    if np.ufunc == type(np.add):
        print("yes it is!")
    else:
        print("no it's not")

def arith():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    print(np.add(a, b))
    print(np.subtract(a, b))
    print(np.multiply(a, b))
    print(np.divide(a, b))
    print(np.power(a, b))

    print(np.mod(a, b))  # --> modulo a % b the returned array is filled with the remainders
    print(np.remainder(a, b))  # np.mod == np.remainder

    print(np.divmod(a, b))  # return the result of the mod calculation and the rest of the mod calculation

    c = [-1, -2, 0.5, 0, 1, 2]
    print(np.absolute(c))  # returns the absolute value of every item in a new list --> -1 = 1...



if __name__ == '__main__':
    arith()