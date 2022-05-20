import numpy as np

"""
you can define the data type like in a not dynamically typed language.
    --> saves space and makes it more efficient

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

you can force a float value to an int value, the value will be the same as if
you do an absolute rounding.     

View vs Copy: 
    -view builds an instance of the object if you edit the instance the original is changed 
    -copy copies the object if you change the copy the original is not changed
    
use .base to check for a copy or view: 
    -if its a view it returns an array
    -if its a copy it returns None
    
    ! Remember arrays can't be compared with anything without an .all() or sth. 
        --> use  if type(b.base) == type(None):
            -just compare the types
"""

def dataTypes():
    arr = np.array([1, 2, 3, 4], dtype="i2")
    print(arr.dtype)

    arr2 = np.array([1.1, 5.2, 9.9], dtype="i")
    print(arr2)

def view_copy():
    a = np.array([1, 2, 3, 4])
    b = a.copy()
    c = a.view()

    b[0] = 5
    c[0] = 6
    print(a)
    print(b)
    print(c)


    if type(b.base) == type(None):
        print("b is a copy")
    else:
        print("b is just an instance")

    if type(c.base) == type(None):
        print("c is a copy")
    else:
        print("c is just an instance")



if __name__ == '__main__':
    view_copy()