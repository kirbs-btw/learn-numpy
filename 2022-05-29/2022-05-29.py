from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    arr_bin = random.binomial(n=100, p=0.5, size=1000)
    arr_normal = random.normal(loc=50, scale=5, size=1000)


    sns.distplot(arr_bin, hist=False, label='binomial')
    sns.distplot(arr_normal, hist=False, label='normal')

    plt.show()



if __name__ == '__main__':
    main()