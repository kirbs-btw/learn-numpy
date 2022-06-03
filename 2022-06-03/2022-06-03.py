import numpy as np

"""
Lesson Log: 

log2() # finds the exponents to the base 2 
log10() # same here with the base 10
log() # base = e (2.718..)

numpy it self has no log with any base you can get you own
"""

def main():
    arr = np.arange(1, 10)
    print(arr)
    print(np.log2(arr))
    print(np.log10(arr))
    pass

if __name__ == '__main__':
    main()