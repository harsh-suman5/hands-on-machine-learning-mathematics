import numpy as np

data = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 20, 12,12, 10]
print("data before removing duplicates: ", data)
data = list(dict.fromkeys(data))
print("data after removing duplicates: ", data)
mean = np.mean(data)
print("mean of the data: ", mean)