## Fundamentals-of-data-analysis-Tasks-2020

### Task No. 1 Creation of a Function called Counts ##

Aim: Without the use of any module in python :write a python function called counts that takes in a list as keys and the number of times each item appears as values


----------------



#### Section Lists and Dictionaries : 

The example codes given show the differences between list and Dictionaries. Inputs for Lists uses square brackets [] and dictionaries uses {}.
The outputs for list [0] ( position) is A , however for Dictionary [A] is 3, the no. of times it appears

#### Section: Development


##### Code Example no.1

A list is created (using values from task details). 
F={} - to creat a empty dictionary
For loop to pass the item through the dictionary f and count how many times it appears.
Print the results. 


##### Code Example no.2

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
    
    
    
    
    
   










