def mean(data):
    n =len(data)
    total_sum = sum(data)
    mean = total_sum/n
    return mean
data = [1,2,3,4,5,5,6,10,4,12,30]
print("mean of data:", mean(data))

import matplotlib.pyplot as plt
plt.hist(data)
plt.xlabel("data values")
plt.ylabel("frequency")
plt.title("histogram of data values")
plt.show()
