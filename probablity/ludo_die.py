import numpy as np

x = np.random.choice([1,2,3,4,5,6])
print("Random Variable:", x)

sample_space = [1,2,3,4,5,6]
event = [x for x in sample_space if x%2 == 0]
print("Event:", event)
prob = len(event)/len(sample_space)
print("Probability of getting an even number:", prob)

import matplotlib.pyplot as plt
plt.bar([1,2,3,4,5,6], 6*1/6)
plt.xlabel("dice outcomes")
plt.ylabel("probablities")
plt.title("sample space probablities")
plt.show()