import random

secret_number = random.randint(0, 100)

user_guess = int(input('Guess a number between 1 and 100: '))

print('You guessed', user_guess)