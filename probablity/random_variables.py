import numpy as np
import scipy.stats as stats
from scipy.stats import binom

n = 10
p = 0.5

x = np.arange(0,n+1)

pmf_values = binom.pmf(x,n,p)
print(pmf_values)
import matplotlib.pyplot as plt
plt.bar(x, pmf_values)
plt.xlabel("number of success(k)")
plt.ylabel("Probability")
plt.title("binomial distribution pmf")
plt.show()
