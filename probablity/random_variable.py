import numpy as np

tosses =  np.random.choice(['H','T'], size =10)
print("Tosses:", tosses)
random_variable = np.sum(tosses == 'T')
print("Random Variable:", random_variable)


#sample space
import itertools
sample_space = list(itertools.product(['H','T'],repeat = 2))
print("Sample Space:", sample_space)
event = [outcome for outcome  in sample_space if outcome == ('T','T')]
print("Event:", event)
prob = len(event)/len(sample_space)
print("Probability of getting two tails:", prob)
import matplotlib.pyplot as plt
plt.bar(['HH','HT','TH','TT'], [1/4, 1/4, 1/4, 1/4])
plt.xlabel("outcomes")
plt.ylabel("probability")
plt.title("sample space probablities")
plt.show()

