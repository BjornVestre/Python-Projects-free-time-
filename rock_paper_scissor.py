import random



while True:
    computer_choice = random.choice(["r", "p", "s"])

    while True:
        player_choice = input("Choose Rock, paper or scissor (r/p/s) :").lower().strip()
        if player_choice in ["r", "p", "s"]:
            break
        else:
            print("please enter r, p or s")


    if computer_choice == player_choice:
        print("TIE! \n both players choose the same option")
    elif computer_choice == "r" and player_choice == "p":
        print("YOU WIN!\n your choice = paper \n computer choice = rock ")
    elif computer_choice == "p" and player_choice == "s":
        print("YOU WIN  !\n your choice = scissor \n computer choice = paper) ")
    elif computer_choice == "s" and player_choice == "r":
        print("YOU WIN!\n Your choice = rock \n computer choice = scissor ")
    else:
        print("YOU LOSE! ")

