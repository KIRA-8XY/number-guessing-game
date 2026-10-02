import random, sys
MAX_ATTEMPTS = 7
MIN_NUMBER = 1
MAX_NUMBER = 100

def show_instruction():
    print('Welcome to the number-guessing-game!')
    print(f'I have selected a number between {MIN_NUMBER} and {MAX_NUMBER}')
    print(f'\nYou have {MAX_ATTEMPTS} attempts to guess it!')

while True:

    show_instruction()

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    user_guess = 0
    attempts = 1
    print(f'Guess a number between {MIN_NUMBER} and {MAX_NUMBER}\n')
    while attempts <= MAX_ATTEMPTS:
        try:
            print('Guess {}/{}'.format(attempts, MAX_ATTEMPTS))
            user_guess = int(input('> '))

            if not MIN_NUMBER <= user_guess <= MAX_NUMBER:
                print(f'\nThe number must be between {MIN_NUMBER} and {MAX_NUMBER}!')
                continue


            if user_guess < secret_number:
                print('Too low!\n')
            elif user_guess > secret_number:
                print('Too high!\n')
            else:
                print()
                if attempts > 1:
                    print('Correct! You got it in {} attempts\n'.format(attempts))
                else:
                    print('Correct! You got it in 1 attempt\n')
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
    try:
        answer = input('> ')
    except KeyboardInterrupt:
        print('Goodbye!')
        sys.exit()
        
    if not answer.lower().startswith('y'):
        break
    

