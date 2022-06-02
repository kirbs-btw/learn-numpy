import numpy as np

"""
rounding numbers 

truncation 
fix
rounding 
floor 
ceil

"""

def main():
    arr = [0.7231, 3.141592, 5.71340798, -21.3131, -4.70732]

    print(np.trunc(arr))  # just returns the number without the decimal place 3.31 --> 3.
    print(np.fix(arr))  # np.fix == np.trunc

    print(np.around(arr, 2))  # normal school rounding --> 1.4 --> 1; 1.5 --> 2 ; it takes a second arg for the num
                                # of digits

    print(np.floor(arr))  # rounding down 3.1 --> 3; 3.6 --> 3
    print(np.ceil(arr))  # rounding up 3.1 --> 4; 3.6 --> 4

if __name__ == '__main__':
    main()