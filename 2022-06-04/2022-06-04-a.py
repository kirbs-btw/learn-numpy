import numpy as np

"""
differences: 

np.diff() for an array like [1, 2, 3, 4]
                would be like this -->
                [2-1, 3-2, 4-3]

you can do that multiple times with n 

np.diff([1, 2, 3, 4], n=2)

1. [2-1, 3-2, 4-3] => [1, 1, 1]
2. [1-1, 1-1] => [0, 0]

"""


def main():
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    arr2 = np.array([7, 8, 9, 10, 11, 12])

    print(np.diff(arr1))
    print(np.diff(arr1, n=1))


if __name__ == '__main__':
    main()