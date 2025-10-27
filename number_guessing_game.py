import random

number_to_guess = random.randint(1, 100)

while True:
  try:
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < 1 or guess > 100:
        print("please enter a number between 1 and 100")
        continue

    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too high!')
    else:
      print('Congratulations! You guessed the number.')
      break
  except ValueError:
    print('Please enter a valid number')
