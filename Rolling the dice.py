#creating code for rolling a dice without a function
import numpy as np
import random

NUM_ROLLS = 1000 # Change how many rolls of die
DIE_SIDES = 12 # 12 to simulate 2 dice

# Create the dictionary to store the results of each roll of the dice.
rolls = {}

#Loop for rolling the die NUM_ROLLS times
for r in range(NUM_ROLLS):
    roll_result = random.randint(1, DIE_SIDES)
    if roll_result in rolls:
        # Add to the count for this number.
        rolls[roll_result] += 1

    else:

        # Record the first roll result for this number.
        rolls[roll_result] = 1

# Print how many times each number was rolled for both dice
for roll_result in range(2, 13):
    print("The number", str(roll_result), "was rolled", str(rolls[roll_result]), "times.")