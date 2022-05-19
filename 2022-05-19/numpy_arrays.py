import numpy as np

"""
lesson: How to numpy, why? 

Why? 
It's faster! 

How? 
Pretty similar to a normal python array, you only have to put np.array([...])

Index works the same way as a normal array.
arr[0, 1]
arr[0][1]
works the same.

Working with multi dim arrays: 

ndin = ? 

argument for the dimensions of the array
no need for a big for loop

slicing is the same: 
well it's the same! no more to say 

2022-05-19
"""


def getting_started():
    arr = np.array([1, 2, 3, 4, 5])

    # print(arr[0])

    arr2 = np.array([[1, 2, 3], [4, 5, 6]])

    # print(arr2[0, 1])
    # print(arr2[0][1])

    arr3 = np.array(1, ndmin=4)
    # print(arr3)
    # print(arr3[0, 0, 0, 0])
    # print(arr3.ndim)

    arr4 = np.array([0, 1, 2, 3, 4, 5])
    print(arr4[0::])
    print(arr[1:3])


if __name__ == '__main__':
    getting_started()