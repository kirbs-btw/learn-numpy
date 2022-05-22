import numpy as np

"""
lesson one:
    iterating arrays
    
    iterating is equal to a normal array
    
    np.nditer(arr) 
    flattens the array for iteration just like reshape[-1]
    
     for i in np.nditer(arr, flags=['buffered'],  op_dtypes=['S']):
    => gives back the real buffer 

    for i in np.nditer(arr[:, ::2]):
    => not sure what it does, except for jumping over certain items 
    
    
    for i, j in np.ndenumerate(arr):
    => is the same as enumerate     


"""


def lesson_one():

    arr = np.array([1, 2, 3])

    for item in arr:
        print(item)

    arr2d = np.array([[1, 2, 3], [4, 5, 6]])

    for i in arr2d:
        print(i)

    for i in arr2d:
        for j in i:
            print(j)

    print("---")

    arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    for i in np.nditer(arr3d):
        print(i)

    print("---")
    for i in arr3d.reshape(-1):
        print(i)


def lesson_one_part2():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    for i in np.nditer(arr, flags=['buffered'],  op_dtypes=['S']):
        print(i)

    for i in np.nditer(arr[:, ::2]):
        print(i)

    for i, j in np.ndenumerate(arr):
        print(i)
        print(j)


if __name__ == '__main__':
    lesson_one_part2()