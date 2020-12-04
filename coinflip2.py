import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt 
np.random.seed(42)

#n = 1
#p = 0.5
#x= np.random.binomial(n,p)
# print(x)

# Tossing a unbiased coin ( fair)

#rng = np.random.default_rng()
#n=10
#p = 0.5  # number of trials, probability of each trial
#s = rng.binomial(n, p, 1000)
#print(s)

#Tossing a biased coin (unfair)
#rng = np.random.default_rng()
#n=10
#p = 0.7  # number of trials, probability of each trial
#s = rng.binomial(n, p, 1000)
#print(s)

# Tossing a coin 1000 times where in each experiment we toss the coin 100 times. How many heads in each of the 100 experiments ?

rng = np.random.default_rng()
n=100
p=0.5
# let us repeat our experiment for 1000 times
size=1000
dist=rng.binomial(n=n, p=p, size=size)
#print(dist)

#calculating the probability of seeing x heads out of n=100 tosses
HeadProb=[np.equal(dist,i). sum() for i in range(n)]
print(HeadProb)
 
#Estimating the probability of getting heads in n=100 coin tosses dividing by the no. of experiments
probs_1000 = [np.equal(dist,i).mean() for i in range(n)]
print(probs_1000)

#Plotting the probability of head (successes)
plt.xticks(range(n))
plt.plot(list(range(n)), probs_1000, color='blue', marker='o')
plt.xlabel('Number of Heads',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.show()


