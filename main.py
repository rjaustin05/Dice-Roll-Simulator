"""
Dice Game

requirments
    user selects how many die to roll
    user selects how many sides on dice
    user selects how many times to roll their selections
    print results of each roll
"""

import random
# allows for validation checks on user input use py.ip.numputType() instead of using input()
import pyinputplus as pyip



def roll_dice():

    dice_quantity = int(pyip.inputNum("How many dice would you like to roll? "))
    sides = int(pyip.inputNum("How many sides with the dice have? "))
    roll_quantity = int(pyip.inputNum("How many times would you like to roll? "))

    for i in range(roll_quantity):
        print(f"\nRoll Number: {i+1}\n")
        
        for i in range(dice_quantity):
            result = random.randrange(1,sides)  
            print(f"Dice:{i+1} Result: {result}\n")
        print("--------------")

roll_dice()

