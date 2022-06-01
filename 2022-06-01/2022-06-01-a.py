from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

"""
pareto distribution 
a distribution following the 80-20% rule 

--> power law

"""

def main():
    arr = random.pareto(a=2, size=100)

    sns.distplot(arr)
    plt.show()




if __name__ == '__main__':
    main()