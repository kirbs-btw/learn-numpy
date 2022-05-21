import numpy as np

"""
Lesson 1: 
    -array shaping 
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.shape)
    => 2, 3
     the first array has 2 items and the second layer has 3
    
    if the shape of the array is not symmetrical it throws an error 
    
Lesson 2:
   -reshaping arrays 
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    newArr = arr.reshape(2, 5)
        
    => 
    [
        [ 1  2  3  4  5]
        [ 6  7  8  9 10]
    ]    
    
    it gets you a two dim array
    the numbers you give the reshape have to multiply to the len of the original array 
    
    reshaping the array do not destroy its original form it contains it and you can get the original with .base
    
    with reshape(-1) you can reset the shape to a one dim array
"""

def lesson_one():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.shape)

def lesson_two():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    newArr = arr.reshape(2, 5)
    # this just creates an instance if you change newArr you change arr too

    print(arr)
    print(newArr)

    print(newArr.base)

    newArr[0,0] = 5

    print(newArr)

    print(newArr.reshape(-1))




if __name__ == '__main__':
    lesson_two()