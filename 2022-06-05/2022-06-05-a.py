import numpy as np

"""
Trigonometric function

numpy has the normal math functions like sin, cos, tan, pi, arcsin, arcos, arctan

deg2rad --> converts degree to radiant 
rad2deg --> the complement to it 

hypot --> find the hypotenues takes two arg, side a and b to calc c 
                    --> pythagoras theorem
"""

def main():
    arr1 = np.array([np.pi/1, np.pi/2, np.pi/3, np.pi/4])
    arr2 = np.array([90, 180, 270, 360])

    print(np.sin(np.pi/2))
    print(np.sin(arr1))

    print(np.deg2rad(arr2))

    print(np.hypot(3, 4))


if __name__ == '__main__':
    main()