import numpy as np

"""
GCD - Greatest Common Denominator 

gcd of 8 an 4 would be 2
its the smallest div contained in thees numbers

combined with reduce it's the gcd of all items 
"""

def main():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    print(np.gcd(arr1, arr2))
    print(np.gcd.reduce(arr1))


if __name__ == '__main__':
    main()