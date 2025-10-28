import random

ROCK ='r'
SCISSOR = 's'
PAPER = 'p'

emojis = { ROCK :'🪨', SCISSOR: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys())

player_score = 0
computer_score = 0

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper or scissor (r/p/s) :").lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Please enter a valid choice')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')



def determine_winner(user_choice, computer_choice):
    global player_score, computer_score

    if user_choice == computer_choice:
        print('tie')
    elif \
        (user_choice == ROCK and computer_choice == SCISSOR) or \
        (user_choice == SCISSOR and computer_choice == PAPER) or \
        (user_choice == PAPER and computer_choice == ROCK):
        print('you win')
        player_score += 1
    else:
        print('you lose')
        computer_score += 1

    print(f"SCORE = You: {player_score} | Computer Score : {computer_score}")

def play_game():

    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'y':
            continue
        if should_continue == 'n':
          break
        else:
            print('Please enter y or n')

play_game()