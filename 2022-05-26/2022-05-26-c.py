from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""

lesson: normal distribution 
    random.normal(size=item_count, loc=pos_of_the_high, scale=size_of_the_high)

"""


def main():
    arr = random.normal(size=5000, loc=0, scale=0.1)
    sns.distplot(arr, hist=False)
    plt.show()


if __name__ == '__main__':
    main()
