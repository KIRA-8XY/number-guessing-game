import random, sys
MAX_ATTEMPTS = 7
MIN_NUMBER = 1
MAX_NUMBER = 100

while True:
    print('Welcome to the number-guessing-game!')
    print(f'I have selected a number between {MIN_NUMBER} and {MAX_NUMBER}')
    print(f'\nYou have {MAX_ATTEMPTS} attempts to guess it!')

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    user_guess = 0
    attempts = 1
    print(f'Guess a number between {MIN_NUMBER} and {MAX_NUMBER}\n')
    while attempts <= MAX_ATTEMPTS:
        try:
            print('Guess {}/{}'.format(attempts, MAX_ATTEMPTS))
            user_guess = int(input('> '))

            if not MIN_NUMBER <= user_guess <= MAX_NUMBER:
                print(f'\nThe number between {MIN_NUMBER} and {MAX_NUMBER}!')
                continue


            if user_guess < secret_number:
                print('Too low!\n')
            elif user_guess > secret_number:
                print('Too high!\n')
            else:
                print()
                print('Correct! You got it in {} attempts\n'.format(attempts))
                break

            attempts += 1

        except ValueError:
            print('\nEnter a number!')
            continue

        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit()

    if user_guess != secret_number:
        print("\nYou've lost the game.")
        print(f'The secret number is {secret_number}\n')

    print('Play again? (enter y to continue)')
    if not input('> ').lower().startswith('y'):
        break
    

