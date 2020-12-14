## Fundamentals-of-data-analysis-Tasks-2020

NB: I had a number of issues with notebook and importing the different packages and functions. Resulting in removing anaconda and reinstalling it. I now have to call the command line via anaconda prompt.
Currently I have had to import all packages in each code cell to insure it works in the cell in the notebook. 


References are all documented in the notebook


### Task No. 1 Creation of a Function called Counts ##

##### Aim:

Without the use of any module in python :write a python function called counts that takes in a list as keys and the number of times each item appears as values


##### Lists and Dictionaries : 

The example codes given show the differences between list and Dictionaries. Inputs for Lists uses square brackets [] and dictionaries uses {}.
The outputs for list [0] ( position) is A , however for Dictionary [A] is 3, the no. of times it appears

##### Code Development

**Code Example No.1**

A list is created (using values from task details). 
F={} - to creat a empty dictionary
For loop to pass the item through the dictionary f and count how many times it appears.
Print the results. 

**Code Example No.2**

This code is to show the limitations of creating a dictionary.Examples of limitations is the data types in a initial list

Define function called CountFrequency with object my _list
Again create an empty dictionary using {}

Create 2 sample lists and outputs : 
1st list :showing boolean expressions true/False followed  by integers and strs = output shows that the True is counted 6 times but actually only present 3.

Looking at the 2nd list : where str is before the boolean expressions = output true is counted 3 times correctly

**Code Example No. 3**

This is another limitation example of a case sensitivity . by converting the string to lower case and then counting the frequencies: 
Using :
my_list.lower() - converts the str input from user all to lower case
my_list.split("") - splits the sentence

Returning the items and frequencies in the string as keys and values in a dictionary.

nb: if__name__ == "__main__": - this ensures that the above function is the main one to use. 

**Code Example No. 4**

Using the get () function to return a value for the given key. 

for i in l: 
    d[i]=d.get(i,0)+1 #get() tells code to get the key, value and input into the dictionary called d{}.
    
    
**Code Example No. 5**
   
  Code example no. 5 is another example of using if/else statement in a for loop to output keys and values into a dictionary.
  
  ------------------------------------------------------------------------------------------------------------------------------------
  
    
    
### Task No. 2 Rolling the dice 
  

#### Aim: 

- Write a python function called Dicerolls that simulates rolling a dice
- Taking in 2 parameters : (k) number of dice and (n) the number of times to roll the dice (n)
- the function should simulate randomly rolling (k) dice (n) times and keeping track of each total face value occured
- the output is in the form of a dictionary with the number of times each possible total face value occurs
 -Any module from the python library can be used
 
#### Code Development :

Packages used : 
import numpy as np
import random

 - Import the following python modules : numpy.random to produce random numbers (integers) we get from the dice
 - Create the function calling it Dicerolls and define the parameters in brackets :
         - NUM_ROLLS - the number of dice rolls ( any no. )
         - DIE_SIDES - the number of dice sides ( e.g 1 dice = 6 sides , 2 dice = 12 sides)
         
 - Create a dictionary to store results: using {}
 - Create a loop for rolling the die NUM_ROLL Times - range is 1000 times. 
 - Define what the roll_result is , using random.randint and inputing the low and high limits.Which are dependent on the no. of DIE_SIDES.
     e.g so if DIE_SIDES is 6 , then the nos. is (1,7)  , 7 is used so that 6 will be included.
 - As the dice rolls , a count is started/ incremented for each roll result
 - The output is for the roll_result in the range (1,7) which is dependent on the DIE_SIDES , so calling the roll result and how many times
     it was rolled. 
     
     ---------------------------------------------------------------------------------------------------------------------------------
     
 
### Task No. 3 Stimulate Flipping a Coin


###### Reference : https://cmdlinetips.com/2018/12/simulating-coin-toss-experiment-with-binomial-random-numbers-using-numpy/
  

#### Aim: 

Aim : 
 - Write a python code that simulates flipping a coin 1000 times
 - Run this code 1000 times - keeping track of the number of heads in each of the 1000 simulations
 - Plot to depict the resulting list of 1000 numbers showing that it roughly follows a bell-shaped curve
 - Give a detailed explanation
     
 
#### Code Development :

Packages used : 

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


**Code No. 1**

Demonstrating using numpy.random. Generator.binomial distribution which allows us to simulate multiple experiments with the size ption.
Setting the n (size), p ( probability) and no. of experiments.

Here we looked at a unbiased (fair) coin , by setting the p value as 0.5 and then by increasing the p value , we can increase of chances for success of achieving heads. 

**Code No. 2**
Again using numpy.random.Generator. binomial function , and also seaborn distplot to graph the results of head successes , resulting in a bellshaped curve. 

We looked at calculating the probability of seeing x heads out of n=100 tosses : using np.equal and distribution and calculating i as the sum for i in the range n= 100. 

Next taking into account the number of experiments ( 1000) using the same code as for 100 tosses, except looking at the mean of the range and then using matplotlib to plot number of heads vs Probability. The result was a bell shaped curve with highest success of heads at 70.  

------------------------------------------------------------------------------------------------------------------------------------------


### Task No. 4  Demonstrating Simpsons Paradox


#### Aim: 

Aim : 
 - Use Numpy tp create 4 datasets
 - Each with an x array and a corresponding y array
 
Suggested : create the x arrays using numpy.linspace and to create the y arrays using notation y=a*x+b


#### Code development

Packages used : 

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


**Code No. 1**

To create 4 sets of data: 

Using np.linspace to create evenly spaced numbers over a specifed interval for values of x and x1.
Using the equation of the line to create variables for y and y2 and including some noise via np.random.normal. 

TO ensure a best fit line , incorporating np.polyfit and creating coefficients.

Next to combine the data above using np. concatenate.

Result: To plot all datasets on the one graph along with the best fit line

**Code No. 2**

An example of BMI Measurement

Using Pandas and seaborn to show the relationship between height and weight and the calculated BMI. 

The figures using in the np.random.normal , were Irish men and women height and weight averages. A sample size was picked at random. 

The BMI was calculated = Weight/[height]**2 for men and women

A new variable /dataset was added to the dataframe of gender , 'male' or 'female' and using seaborn , the height and bmi was plotted for combined , and there was a reversal of the relationship between the height and BMI for both.









    
   










