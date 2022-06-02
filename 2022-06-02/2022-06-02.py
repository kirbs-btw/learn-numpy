import numpy as np

"""
ufuncs. there are 

add()
example for compare

"""
def main():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]


    arr = []

    for i in zip(a, b):
        arr.append(i[0] + i[1])


    print(arr)

    print(np.add(a, b))



if __name__ == '__main__':
    main()