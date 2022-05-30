from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
multinomial distribution --> pwals= probabilities
n=the range of numbers

"""

def main():
    arr = random.multinomial(n=6, pvals=[0.1, 0.1, 0.3, 0.2, 0.2, 0.1], size=500)
    print(arr)

    sns.distplot(arr)
    plt.show()

    pass

if __name__ == '__main__':
    main()