import numpy as np

"""
unique returns every item once like distinct in SQL 
union1d returns every unique item of two arrays 
intersect1d returns all items which are present in both arrays every unique item is dismissed
setdiff1d finds the difference of the two arrays and returns the unique ones of the first array 
setxor1d returns all items that are unique in both arrays 

"""

def main():

    arr = np.array([1, 1, 2, 2, 2, 3, 4, 2, 5, 6])

    print(np.unique(arr))

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([4, 5, 6, 7])

    print(np.union1d(arr1, arr2))

    print(np.intersect1d(arr1, arr2, assume_unique=True))

    print(np.setdiff1d(arr1, arr2, assume_unique=True))

    print(np.setxor1d(arr1, arr2, assume_unique=True))
    
if __name__ == '__main__':
    main()