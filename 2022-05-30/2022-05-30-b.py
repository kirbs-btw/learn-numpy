from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
equal to the normal distribution except for the peak
"""



def main():
    arr = random.logistic(loc=1, scale=2, size=(3, 5))
    print(arr)

    sns.distplot(arr, hist=False)

    plt.show()

if __name__ == '__main__':
    main()