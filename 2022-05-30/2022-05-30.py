import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

"""
poissom --> continuous trial
binomial --> discrete trial    


"""


def main():
    arr_normal = random.normal(loc=50, scale=7, size=1000)
    arr_poisson = random.poisson(lam=50, size=1000)

    sns.distplot(arr_normal, hist=False, label="normal")
    sns.distplot(arr_poisson, hist=False, label="poission")

    plt.show()


if __name__ == '__main__':
    main()