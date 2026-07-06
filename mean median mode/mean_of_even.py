# mean of even numbers only
import numpy as np

a = [1,32,3,45,34,23,46,67,98,102]

if a:
    even_no = [num for num in a if num%2==0]
    even_mean = np.mean(even_no)
    print(even_mean)