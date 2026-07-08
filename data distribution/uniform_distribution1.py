# practical illustration of uniform distribution

import numpy as np

import matplotlib.pyplot as plt


df = np.random.normal(-10.0,10.0,10000)
plt.hist(df,50)
plt.show()