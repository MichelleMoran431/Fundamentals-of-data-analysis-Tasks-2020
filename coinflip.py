from scipy.stats import binom 
# setting the values of n and p 
n = 1000
p = 0.6
# defining the list of r values 
r_values = list(range(100)) 
# obtaining the mean and variance  
mean, var = binom.stats(n, p) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# printing the table 
print("r\tp(r)") 
for i in range(100): 
    print(str(r_values[i]) + "\t" + str(dist[i])) 
# printing mean and variance 
print("mean = "+str(mean)) 
print("variance = "+str(var))

# Plotting results 

from scipy.stats import binom 
import matplotlib.pyplot as plt 
# setting the values 
# of n and p 
n = 1000
p = 0.6
# defining list of r values 
r_values = list(range(100)) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# plotting the graph  
plt.bar(r_values, dist) 
plt.show()