#calculate the mean value of only possitive numbers

import numpy as np

a = [-1, -2, -3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if a:
    possitive_no = [nums for nums in a if nums>=0]
    mean = np.mean(possitive_no)
    print(mean)