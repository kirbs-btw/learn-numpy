import numpy as np

"""
joining arrays



"""


def main():
    arr = np.array([2, 3, 4])
    arr2 = np.array([5, 6, 7])

    newArr = np.concatenate((arr, arr2))

    print(newArr)

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    newArr = np.concatenate((a, b), axis=1)

    print(newArr)

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])

    # like zipping
    newArr = np.stack((a, b), axis=1)
    print(newArr)


    # row stacking
    newArr = np.hstack((a, b))
    print(newArr)

    # column stacking
    newArr = np.vstack((a,b))
    print(newArr)

    # stacks in depth --> 3rd axis
    newArr = np.dstack((a, b, c))
    print(newArr)

if __name__ == '__main__':
    main()