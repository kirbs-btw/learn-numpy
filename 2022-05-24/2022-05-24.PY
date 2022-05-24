import numpy as np

"""
lesson: search
    
    -np.where(condition)
    -returns an array with all the Indices where the condition is true
    
    -np.searchsorted(arr, num)
    -returns the index where the num should be inserted to be correct in the order of the array
        --> binary search algorithm 
        --> is used only on sorted lists if not there is no point! 
        --> start from the left of the array vat normal 
    
    -with side you can define the direction it is going
        e.g. np.searchsorted(arr, 2, side='right')
        
        there is a difference because the index if with left whe first one and with right the last one in the order
    
    -you can search for multiple values if you give a list as a param.
    
"""

def where_method():

    """
    old method
    :return:
    """
    arr_old = [1, 2, 3, 4, 5, 6]
    hold_arr = []

    for item, i in enumerate(arr_old):
        if item % 2 == 0:
            hold_arr.append(i)

    print(hold_arr)

    """
    numpy method
    :return: 
    """
    arr = np.array([1, 2, 3, 4, 5, 6])
    x = np.where(arr%2 == 0)
    print(x)

def searchSorted_method():
    arr = np.array([1, 2, 3, 5, 6])
    x = np.searchsorted(arr, 4)
    print(x, "\n")


    arr = np.array([0, 1, 2, 3, 4, 5])
    x = np.searchsorted(arr, 2, side='left')
    y = np.searchsorted(arr, 2, side='right')
    print(x)
    print(y)

    x = np.searchsorted(arr, [1, 3, 5])
    print(x)


if __name__ == '__main__':
    searchSorted_method()