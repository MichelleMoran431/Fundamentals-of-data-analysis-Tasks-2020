
import numpy as np
import random
def Diceroll (NUM_ROLLS,DIE_SIDES):
    NUM_ROLLS = 1000
    DIE_SIDES = 12
# Create the dictionary to store the results of each roll of the die.
rolls = {}
#Loop for rolling the die NUM_ROLLS times
for r in range (100):
    roll_result = random.randint(1, 13)
    if roll_result in rolls:
        # Add to the count for this number.
        rolls[roll_result] += 1
    else:
        # Record the first roll result for this number.
        rolls[roll_result] = 1

# Print how many times each number was rolled
for roll_result in range(1, 13):
    print("The number", str(roll_result), "was rolled", str(rolls[roll_result]), "times.")

#How many times the 3 was rolled
print("The number three was rolled", str(rolls[3]), "times.")

#Total roll between all of them
sum = 0
for roll_result in rolls:
    sum += roll_result * rolls[roll_result]

print("The total roll result was", str(sum))




    