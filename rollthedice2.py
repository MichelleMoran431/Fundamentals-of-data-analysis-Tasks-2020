import random
import numpy as np
#import collections
#from collections import Counter


def roll_dice(rolls, sides):
    Dicerolls = eval(input("Please enter the number of dierolls:"))
    for x in range(0,Dicerolls):
        dice = {i:0 for i in range(1,11)}
        dice[random.randint(1, sides)] += 1
    return(dice)
print(roll_dice(50, 10))