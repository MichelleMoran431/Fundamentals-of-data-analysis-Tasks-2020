import numpy as np
import random
def roll(die, sides,dierolls):  # Define roll function
    r = 0  # Start r at 0 

    while r < die:  # Start While loop to roll based on number of dice selected
        rolls = random.randint(1,sides)  # Store random roll to variable rolls
        r += 1  # Increase by 1 each loop through until loop validates false
        print(np.sum(sides))  # Print out the rolls for each die selected


def main():  # Define main function/program
    rolling = True  # set variable to test True for initial loop
    while rolling:  # start while loop while condition evaluates True
        answer = input("Ready to roll? Y or N: ")  # Receive answer to begin program
        if answer.lower() == "y":  # If user says yes, run program
            die = eval(input("Please enter the amount of dice you wish to roll: "))  # create variable for amount of die
            sides = eval(input("Please enter the number of sides on your dice: "))  # create variable for sides
            dierolls = eval(input("Please enter the number of dierolls:"))
            roll(die,sides,dierolls)  # Pass user input variables to roll function
        else:  # If user selected anything other than Y or y
            print("Thank you for playing!")  # Print Thank you
            break  # End while loop/program


main()  # Call main function/program upon importing