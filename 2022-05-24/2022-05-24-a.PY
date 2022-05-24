import numpy as np

"""
lesson: sorting arrays with np.sort()
    -it's non destructive, it creates a copy of the array not a view
    -it's form smallest to biggest
    -booleans: False is before True
        --> False == 0
        --> True == 1
        0 < 1 :) 
    
    -if you pass a multi dim array it sorts the arrays at the fist dimension
        -it does not change the shape! 
"""

def main():
    arr = np.array([2, 4, 1, 3, 9, 7])

    sorted_arr = np.sort(arr)
    print(arr, sorted_arr)

    bool_arr = np.array([True, False, False, True])
    sorted_arr = np.sort(bool_arr)
    print(sorted_arr)

    dim_arr = np.array([[2, 1, 5], [7, 0, 2]])
    sorted_arr = np.sort(dim_arr)
    print(sorted_arr)

if __name__ == '__main__':
    main()