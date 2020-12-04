## Fundamentals-of-data-analysis-Tasks-2020

### Task No. 1 Creation of a Function called Counts ##

##### Aim:

Without the use of any module in python :write a python function called counts that takes in a list as keys and the number of times each item appears as values


----------------

##### Lists and Dictionaries : 

The example codes given show the differences between list and Dictionaries. Inputs for Lists uses square brackets [] and dictionaries uses {}.
The outputs for list [0] ( position) is A , however for Dictionary [A] is 3, the no. of times it appears

##### Code Development

###### Code Example no.1

A list is created (using values from task details). 
F={} - to creat a empty dictionary
For loop to pass the item through the dictionary f and count how many times it appears.
Print the results. 

###### Code Example no.2

This code is to show the limitations of creating a dictionary.Examples of limitations is the data types in a initial list

Define function called CountFrequency with object my _list
Again create an empty dictionary using {}

Create 2 sample lists and outputs : 
1st list :showing boolean expressions true/False followed  by integers and strs = output shows that the True is counted 6 times but actually only present 3.

Looking at the 2nd list : where str is before the boolean expressions = output true is counted 3 times correctly

###### Code Example no. 3

This is another limitation example of a case sensitivity . by converting the string to lower case and then counting the frequencies: 
Using :
my_list.lower() - converts the str input from user all to lower case
my_list.split("") - splits the sentence

Returning the items and frequencies in the string as keys and values in a dictionary.

nb: if__name__ == "__main__": - this ensures that the above function is the main one to use. 

##### Code Example no. 4

Using the get () function to return a value for the given key. 

for i in l: 
    d[i]=d.get(i,0)+1 #get() tells code to get the key, value and input into the dictionary called d{}.
    
    
##### Code Example no. 5
   
  Code example no. 5 is another example of using if/else statement in a for loop to output keys and values into a dictionary.
    
    
### Task No. 2 Rolling the dice 
  

#### Aim: 

- Write a python function called Dicerolls that simulates rolling a dice
- Taking in 2 parameters : (k) number of dice and (n) the number of times to roll the dice (n)
- the function should simulate randomly rolling (k) dice (n) times and keeping track of each total face value occured
- the output is in the form of a dictionary with the number of times each possible total face value occurs
 -Any module from the python library can be used
 
#### Code Development :

 - Import the following python modules : numpy and random to produce random numbers (integers)
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
     
     
     
 


    
   










