import numpy as np
from numpy import random

"""
lesson: random distribution

random.choice(choices, p=distribution, size=(100))

you can describe the distribution of items in a random generated array

"""


def main():
    choices = np.array([2, 4, 6, 8, 0])
    distribution = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

    arr = random.choice(choices, p=distribution, size=(100))

    print(arr)
    print(np.sort(arr))

    arr = random.choice(choices, p=distribution, size=(5, 10))
    print(arr)

if __name__ ==  '__main__':
    main()