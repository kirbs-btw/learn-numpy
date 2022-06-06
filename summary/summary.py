import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

"""
Summary:

########## normal arrays

np.array([1, 2, 3, 4])                  # creates a numpy array

Data Types: 
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

arr.dtype                              # returns the data type of the array
np.array([1, 2, 3], dtype='S')         # example for defining the data type


arr.copy()                             # creates a copy of the array changing the original does not effect the new one!
arr.view()                             # creates an instance of the array changing the original does effect the new one!

arr.shape                              # returns the shape of the array meaning the item count at each dimension
arr.reshape(2, 3)                      # reshape the original array the original shape of the array can be found
arr.base                               # returns the original shape of the array reshape does not destroy it
arr.reshape(-1)                        # flattens the array from n-dimensions to one 

np.nditer(arr)                         # flattens the array for iteration 
np.nditer(arr, flags=['buffered'],  op_dtypes=['S']) # returns the real buffer

for i, j in np.ndenumerate(arr):       # same as enumerate for normal arrays 

np.concatenate((arr, arr2))            # joins the two arrays to one, it stays one dimensional 
np.concatenate((a, b), axis=1)         # joins them only on the defined axis
np.stack((a, b), axis=1)               # like zipping 
np.hstack((a, b))                      # horizontal stack   x-axis 
np.vstack((a, b))                      # vertical stack     z-axis
np.dstack((a, b))                      # depth stack        y-axis

a, b = np.array_split(arr, 2, axis=1)  # splits the array into two equal parts on the first axis 
np.hsplit(arr, 3)                      # horizontal split 
np.vsplit(arr, 3)                      # vertical split
np.dsplit(arr, 3)                      # depth split  
    => return an array containing all splits
        -> assign to var like in the fist example 
    
np.where(arr == 4)                      # returns the index where the condition is true
np.searchsorted(arr, 2, side='left')    # returns position where number should be inserted, only use on sorted arrays

np.sort()                               # sorts the array does not destroy the shape (False before True)

arr[filter_arr]                         # you can filter items with a filter array containing True and False 
filter_quick = arr % 2 == 0             # set up a filter array through conditions 

########### random arrays 
from numpy import random

random.rand(2, 3)                       # multi dim array filled with floats between 0 and 1
random.randint(0, 100, size=(2, 3))     # multi dim array filled with int between 0 and 100 
random.choice(arr, size=(2, 4))         # picks at random from a given array size = shape of the returned array 
random.choice(choices, p=distribution, size=(100))  # p = distribution array, custom probabilities

random.shuffle(arr)                     # shuffles array - original array is shuffled no return of this func
random.permutation(arr)                 # returns the shuffled array 

random.normal(size=item_count, loc=pos_of_the_high, scale=size_of_the_high)
random.binomial(n=item_count, p=probability, size=shape_of_the_array)
random.poisson(lam=rate_of_occurrences, size=shape)  
random.uniform(size=shape_of_the_returned_array)
random.logistic(loc=peak, scale=deviation, size=shape)
random.multinomial(n=number_of_possible_outcomes, pvals=list_of_probabilities)
random.exponential(scale=inverse_of_rate, size=shape)
random.chisquare(df=degree_of_freedom, size=shape) -> 80/20 rule 
random.rayleigh(scale=deviation, size=shape)
random.pareto(a=2, size=shape) a=shape_parameter
random.zipf(a=distribution_parameter, size=shape) --> 1/n

############### UFUNC ##

np.frompyfunc(test_function, 0, 0)      # add to ufunc list of numpy 

np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.power(a, b)
np.mod(a, b)                        # --> modulo a % b the returned array is filled with the remainders
np.remainder(a, b)                  # np.mod == np.remainder
np.divmod(a, b)                     # return the result of the mod calculation and the rest of the mod calculation
np.absolute(c))                     # returns the absolute value of every item in a new list --> -1 = 1...
 
np.trunc(arr)                       # just returns the number without the decimal place 3.31 --> 3.
np.fix(arr)                         # np.fix == np.trunc
np.around(arr, 2)                   # normal school rounding -> 1.4 -> 1; 1.5 -> 2; it takes a second arg for the num
                                    # of digits
np.floor(arr)                       # rounding down 3.1 --> 3; 3.6 --> 3
np.ceil(arr)                        # rounding up 3.1 --> 4; 3.6 --> 4

log2(arr)                              # finds the exponents to the base 2 
log10(arr)                             # same here with the base 10
log(arr)                               # base = e (2.718..)
   
np.sum([a, b])                      # sums every item of the arrays 
np.sum([a, b], axis=1)              # sums only on the axis     
np.cumsum(a)                        # partially adding numbers 4 = 4 + 3 + 2 + 1

np.prod(arr1)                       # product of every item combined
np.prod([arr1, arr2], axis=1)       # product of every item constrained by the axis 
np.cumprod(arr1)                    # returns the partial sum of every item like faculty would 

np.diff(arr1)                       # e.g. arr1 = [1, 2, 3, 4] --> [2-1, 3-2, 4-3] -> [1, 1, 1]
np.diff(arr1, n=1)                  # n defines how often this happens -> like a loop

lcm(arr1, arr2)                     # takes two args and returns the 'lowest common multiple' of the two numbers
lcm.reduce(arr)                     # returns the lcm of every element combined 
np.gcd(arr1, arr2)                  # Greatest Common Denominator gcd of 8 an 4 would be 2
np.gcd.reduce(arr1)                 # returns the gcd of every element combined 

np.sin,
np.cos 
np.tan 
np.pi 
np.arcsin 
np.arcos 
np.arctan
np.deg2rad                         # converts degree to radiant 
np.rad2deg                         # the complement to it 
np.hypot                           # find the hypotenues takes two arg, side a and b to calc c 

np.sinh
np.cosh 
np.tanh 
np.arcsinh 
np.arccosh 
np.arctanh

np.unique(arr1, arr2)            # returns every item once like distinct in SQL 
np.union1d(arr1, arr2)           # returns every unique item of two arrays 
np.intersect1d(arr1, arr2)       # returns all items which are present in both arrays every unique item is dismissed
np.setdiff1d(arr1, arr2)         # finds the difference of the two arrays and returns the unique ones of the first array 
np.setxor1d(arr1, arr2)          # returns all items that are unique in both arrays 
"""

