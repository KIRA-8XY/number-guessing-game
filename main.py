import random

secret_number = random.randint(0, 100)

print('Secret number: {}'.format(secret_number))
user_guess = 0
attempts = 0
while user_guess != secret_number:
    try:
        user_guess = int(input('Guess a number between 1 and 100: '))
        attempts += 1
        if user_guess < secret_number:
            print('Too low!')
        elif user_guess > secret_number:
            print('Too high!')
        else:
            break
    except ValueError:
        print('Enter a number!')
        continue
    except KeyboardInterrupt:
        print('\nGoodbye!')
        break
    

print('Correct! You got it in {} attempts'.format(attempts))
