import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import seaborn as sns

def main():
    arr = random.rand(100)
    x = np.arange(0, 100, 1)
    print(arr)

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            plt.bar(x, arr)
            plt.pause(0.001)
            plt.clf()
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    plt.show()

if __name__ == '__main__':
    main()