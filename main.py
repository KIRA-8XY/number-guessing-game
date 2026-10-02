import random
MAX_ATTEMPTS = 7
MIN_NUMBER = 1
MAX_NUMBER = 100

def show_instruction():
    print('Welcome to the number-guessing-game!')
    print(f'I have selected a number between {MIN_NUMBER} and {MAX_NUMBER}')
    print(f'\nYou have {MAX_ATTEMPTS} attempts to guess it!')

def get_guess(attempts):
    while True:
        try:
            print('Guess {}/{}'.format(attempts, MAX_ATTEMPTS))
            user_guess = int(input('> '))
            return user_guess
        except ValueError:
            print('\nEnter a number!')

def play_round():

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    user_guess = 0
    attempts = 1

    while attempts <= MAX_ATTEMPTS:
        user_guess = get_guess(attempts)

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

    if user_guess != secret_number:
            print("\nYou've lost the game.")
            print(f'The secret number is {secret_number}\n')

def ask_play_again():

    print('Play again? (enter y to continue)')
    answer = input('> ')
        
    if answer.lower().startswith('y'):
        return True
    
    return False  

    # or more simple: 
    # return answer.lower().startswith('y')

def main():
    try:
        while True:
            show_instruction()
            play_round()
            if not ask_play_again():
                break

    except KeyboardInterrupt:
            print('\nGoodbye!')


if __name__ == "__main__":
    main()

    

    

