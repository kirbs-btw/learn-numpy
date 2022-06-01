from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

"""
used for signal processing
scale --> standard deviation
size --> shape to the array

"""

def main():
    arr = random.rayleigh(scale=3, size=100)

    sns.distplot(arr, hist=False)
    plt.show()

if __name__ == '__main__':
    main()