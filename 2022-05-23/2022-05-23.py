import numpy as np

"""
lesson - array split:
    array_split(arr, 3)
    
    splits the array in three equal parts,
    if the len() is not divisible by the number the items are 
    distributed from the first item going on 
    
    axis=1 defines the axis around which you want to split the array 
    
    np.hsplit() => simple method of  a, b, c = np.array_split(arr, n, axis=1)
    
"""


def main():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    arr = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]])

    a, b, c = np.array_split(arr, 3, axis=1)


    print(a)
    print()
    print(b)
    print()
    print(c)

    print(np.hsplit(arr, 3))


if __name__ == '__main__':
    main()