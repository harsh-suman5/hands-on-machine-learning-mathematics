#mean of odd numbers

import numpy as np

a = [1,2,3,4,5,6,7,8,9,10]
print("the data set value is: ",a)
if a: 
    odd_no = [nums for nums in a if nums%2!=0]
    print("the odd numbers of dataset which is used for calculating mean value: ", odd_no)

    odd_mean = np.mean(odd_no)
    print("the mean calculation of odd numbers are: ", odd_mean)