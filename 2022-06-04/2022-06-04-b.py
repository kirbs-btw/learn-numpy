import numpy as np

"""
LCM - lowest common multiple 

lcm() takes two args and returns the LCM of the two numbers
lcm.reduce() returns the lcm of every element combined 

"""


def main():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    print(np.lcm(arr1, arr2))
    print(np.lcm.reduce(arr1))


if __name__ == '__main__':
    main()