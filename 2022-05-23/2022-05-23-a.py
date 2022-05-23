import numpy as np

"""
array search: 
    
    the np.where function gives back the index of the item 

"""


def main():
    arr = np.array([1, 2, 3, 4, 5, 6])

    print(np.where(arr == 4)[0][0])





    pass

if __name__ == '__main__':
    main()