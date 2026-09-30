import random

secret_number = random.randint(0, 100)

user_guess = int(input('Guess a number between 1 and 100: '))
print('Secret number: {}'.format(secret_number))

if user_guess < secret_number:
    print('Too low!')
elif user_guess > secret_number:
    print('Too high!')
else:
    print('Correct!')
