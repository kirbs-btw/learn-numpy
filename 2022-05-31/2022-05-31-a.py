import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    arr1 = random.chisquare(df=1, size=1000)
    arr2 = random.chisquare(df=5, size=1000)

    sns.distplot(arr1, hist=False, label='first')
    sns.distplot(arr2, hist=False, label='second')

    plt.show()


if __name__ == '__main__':
    main()