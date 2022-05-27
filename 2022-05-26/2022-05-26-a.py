import numpy as np
from numpy import random

"""
lesson: shuffling arrays - permutation
    random.shuffle == changes the original array
    
    random.permutation == returns the re-arranged array
    
"""



def main():
    arr = np.array([1, 2, 3, 4, 5, 6])
    random.shuffle(arr)
    print(arr)
    print(random.shuffle(arr))  # does not return anything
    print(random.permutation(arr))





    pass


if __name__ == '__main__':
    main()