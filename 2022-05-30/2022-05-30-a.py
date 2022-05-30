from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
uniform distribution
    --> lower bound = 0
    --> upper bound = 1
    
    used for possibilities with equal chance 

"""

def main():
    arr = random.uniform(size=(2, 3))
    print(arr)

    sns.distplot(arr, hist=False)
    plt.show()

if __name__ == '__main__':
    main()