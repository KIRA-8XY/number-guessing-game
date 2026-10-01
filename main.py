import random
MAX_ATTEMPTS = 7

while True:
    print('Welcome to the number-guessing-game!')
    print('I have selected a number between 1 and 100')
    print('You have 7 attempts to guess it!')

    secret_number = random.randint(1, 100)

    user_guess = 0
    attempts = 1
    print('Guess a number between 1 and 100\n')
    while attempts <= MAX_ATTEMPTS:
        try:
            print('Guess {}/{}'.format(attempts, MAX_ATTEMPTS))
            user_guess = int(input('> '))

            if not 1 <= user_guess <= 100:
                print(f'The number between 1 and 100!')
                continue

            attempts += 1

            if user_guess < secret_number:
                print('Too low!\n')
            elif user_guess > secret_number:
                print('Too high!\n')
            else:
                print()
                print('Correct! You got it in {} attempts\n'.format(attempts))
                break

        except ValueError:
            print('Enter a number!')
            continue
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break

    if user_guess != secret_number:
        print()
        print("You've lost the game.")
        print(f'The secret number is {secret_number}\n')

    print('Play again? (enter y to continue)')
    if not input('> ').lower().startswith('y'):
        break
    

