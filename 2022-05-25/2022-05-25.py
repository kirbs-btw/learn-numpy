import numpy as np

"""
lesson: Filter array

bool array - used as a filter for an other array

"""


def main():
    arr = np.array([0, 1, 2, 3, 4, 5])
    filter_arr = np.array([True, False, True, True, False, False])

    print(arr[filter_arr])

    second_filter = []

    for item in arr:
        if item > 3:
            second_filter.append(True)
        else:
            second_filter.append(False)

    print(arr[second_filter])

    even_filter = []

    for item in arr:
        if item % 2 == 0:
            even_filter.append(True)
        else:
            even_filter.append(False)

    print(arr[even_filter])

    """
    filter without loop
    """

    filter_quick = arr % 2 == 0
    print(arr[filter_quick])




    pass

if __name__ == '__main__':
    main()