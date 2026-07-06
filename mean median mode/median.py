#finding the median using python script
import numpy as np

income = np.random.choice([100,250,270,300,350,370,400], size=37)
print("==============================================")
print("\n income before sorting: ",income)
income.sort()

print('income dataset after sorting is: ', income)

n = len(income)
print("length of the dataset: ",n)

mid = n//2
print("the mid of the dataset", mid)

median = (income[mid-1] + income[mid])/2 if n%2==0 else income[mid]
print(median)

import matplotlib.pyplot as plt

plt.boxplot(income)

plt.ylabel("income")
plt.title("Boxplot of income")
plt.show()