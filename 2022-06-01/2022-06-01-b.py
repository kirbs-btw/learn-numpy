from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

"""
a distribution following the 1/n law of Zipf
it's about the distribution to letter in a dict or the occurrence of names in a population 

1: 1/1
2: 1/2
3: 1/3
4: 1/4
5: 1/5
...

"""

def main():
    arr = random.zipf(a=2, size=1000)
    sns.distplot(arr[arr<10], kde=False)
    plt.show()


if __name__ == '__main__':
    main()