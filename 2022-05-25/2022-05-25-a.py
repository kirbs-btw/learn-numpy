from numpy import random
import numpy as np

"""
lesson random:
random.rand() => num between 0 and 1
random.rand(2, 3) => multi dim array filled with floats between 0 and 1

random.randint(0, 100, size=(2, 3))
=> array filled with integers between 0, 100 
    => with the shape 2, 3

choice array

random.choice(arr, size=(2, 4))
    => random numbers picked out of an array with the shape (2, 4)

"""

def main():
    n = random.randint(0, 100)
    print(n)
    n = random.rand()
    print(n)


    arr = random.randint(0, 100, size=5)
    print(arr)

    multi = random.randint(0, 100, size=(2, 4))
    print(multi)

    arr = random.rand(5)
    print(arr)

    arr = random.rand(2, 3)
    print(arr)

    choice_arr = np.array([2, 4, 6, 7, 9])
    n = random.choice(choice_arr)
    print(n)

    arr = random.choice(choice_arr, size=(3, 5))
    print(arr)


if __name__ == '__main__':
    main()