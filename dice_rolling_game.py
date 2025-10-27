import random

while True:
    roll = input("roll the dice (y/n)? ").strip().lower()

    if roll == "y":
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(dice_1, dice_2)
    elif roll == "n":
        print("thanks for playing")
        break
    else:
        print("please enter y or n")

