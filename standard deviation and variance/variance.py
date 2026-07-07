import numpy as np
import matplotlib.pyplot as plt

data = [10,30,20,50,70,65,78,90,35]
data.sort()
print("dataset values given: ",data)

mean = np.mean(data)
print(mean)

std = np.var(data)
print(std)

plt.hist(data, bins=6, color='skyblue', edgecolor='black', alpha=0.7)



plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean:.2f}')
plt.axhline(std, color='red', linestyle='dashed',linewidth=2, label=f'std = {std:.1f}' )

# Labels and title
plt.xlabel('Arrival per minute')
plt.ylabel('Frequency')
plt.title('Histogram of Data Given')
plt.legend()
plt.grid(True, linestyle='--', alpha=0)

plt.show()