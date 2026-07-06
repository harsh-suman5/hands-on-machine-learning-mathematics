import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.random.randint(18, high=90, size=500)
print(data)
mode = stats.mode(data)
print(mode)

plt.hist('data')
plt.xlabel('data values')
plt.ylabel('frequency')
plt.title("hist of data")
plt.show()