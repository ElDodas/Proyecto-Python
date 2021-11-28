import random

def dice_sides():
    sides = int(input("\n\tHow many sides would you like on your dice:\t"))
    return sides

def dice_number():
    number_of_dice = int(input("\tHow many dice would you like to roll:\t"))
    return number_of_dice

def roll_dice(dice_sides:int,dice_count:int):
    dice_values = []
    print(f"\tYou rolled {dice_count} {dice_sides} sided dice. ")
    print(f"\n\t-----Results are as followed-----")
    for dice in range(dice_count):
        rolled_number = random.randint(1,dice_sides)
        print(f"\t\t{rolled_number}")
        dice_values.append(rolled_number)
    return dice_values    

def sum_dice(dice_values:list):
    total = sum(dice_values,0)
    print(f"\n\tThe total value of your roll is {total}")

def roll_again():
    response = input("\n\tWould you like to roll again ? (y/n)\t").lower()
    if response.startswith("y"):
        return True
    else:
        return False

#main program
if __name__ == "__main__":
    print("\tWelcome to the Python Dice App\n")
    condition=True
    while condition:
        #prepare dice
        no_of_sides = dice_sides()
        no_of_dices = dice_number()

        rolled_values = roll_dice(no_of_sides,no_of_dices)
        sum_dice(rolled_values)
        condition = roll_again()
    print("\n\tThank you for using the Python Dice App\n") 