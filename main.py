import random
MAX_ATTEMPTS = 7

while True:
    print('Welcome to the number-guessing-game!')
    x, y = map(int, input(
'''Enter the lower and upper range of the number that you want to guess!
(ex: 1 100, 20 55, etc.)
> ''').split()) 
    secret_number = random.randint(x, y)

    # print('Secret number: {}'.format(secret_number))

    user_guess = 0
    attempts = 1
    print(f'Guess a number between {x} and {y}: ')
    while attempts <= MAX_ATTEMPTS:
        try:
            print('Guess #{}'.format(attempts))
            user_guess = int(input('> '))
            if not x <= user_guess <= y:
                print(f'The number between {x} and {y}!')
                continue
            attempts += 1
            if user_guess < secret_number:
                print('Too low!')
            elif user_guess > secret_number:
                print('Too high!')
            else:
                print('Correct! You got it in {} attempts'.format(attempts))

            if attempts > MAX_ATTEMPTS:
                print('You\'ve lost the game.')
                print('The secret number is {}'.format(secret_number))

            print('Play again? (y/n)')
            if not input('> ').lower().startswith('y'):
                break

        except ValueError:
            print('Enter a number!')
            continue
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break
    

