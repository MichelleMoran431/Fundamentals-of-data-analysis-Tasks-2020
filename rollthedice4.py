import random
i = False
saveDice={}
while i == False:
    print("\nHow many dices u want to roll?")
    x = int(float(input())
    y = 1
    while y <= x:
        dice = random.randint(1, 6)
        savedDice (saveDice.append(dice))
        print("Dice " + str(y) + " value is " + str(dice))
        y += 1
    print("Total from rolling " + str(x) + " dice: ", sum(saveDice))
    saveDice.clear()