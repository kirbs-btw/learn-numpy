import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

"""
well it's a exponential distribution...

"""


def main():
    arr = random.exponential(scale=5, size=500)

    sns.distplot(arr)
    plt.show()

if __name__ == '__main__':
    main()