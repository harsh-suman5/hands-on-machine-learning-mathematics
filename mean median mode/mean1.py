import numpy as np

data = np.random.randint(1,30, size = 5)
print("random variable: ", data)
mean = np.mean(data)
print("mean of the data: ",mean)

import matplotlib.pyplot as plt

plt.hist(data)
plt.xlabel("data values")
plt.ylabel("frequency")
plt.title("histogram of data values")
plt.show()