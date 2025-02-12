import numpy as np
import matplotlib.pyplot as plt 

num_trials = 1000
num_toss = 100

heads_count = np.zeros(num_trials) # creates one dimensional array of len () and sets all values initially to zeroes

for trial in range(num_trials):
    tosses = np.random.randint(0,2,num_toss)
    heads_count[trial] = np.sum(tosses)


plt.hist(heads_count,bins=range(num_toss + 2),edgecolor='black',density=True)
plt.title(f'Distribution of Heads in {num_trials} Trials of {num_toss} Coin Tosses')
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
