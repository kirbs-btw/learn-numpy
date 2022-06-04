import numpy as np

"""
lesson product:

np.prod()

multiplies every array item with each other 
even with multi dim arrays 

with axis = 
you can define the axis where is should multiply 

np.cumprod returns the partial sum of every item like faculty would 

"""


def main():
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    arr2 = np.array([7, 8, 9, 10, 11, 12])

    print(np.prod(arr1))
    print(np.prod([arr1, arr2]))
    print(np.prod([arr1, arr2], axis=1))

    print(np.cumprod(arr1))

if __name__ == '__main__':
    main()