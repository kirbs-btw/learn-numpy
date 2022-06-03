import numpy as np

"""
lesson - summation:

"""

def main():
    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.array([7, 8, 9, 10, 11, 12])

    print(np.add(a, b))
    print(np.sum([a, b]))
    print(np.sum([a, b], axis=1))  # sums only on the axis

    print(np.cumsum(a))  # partially adding numbers 4 = 4 + 3 + 2 + 1

if __name__ == '__main__':
    main()