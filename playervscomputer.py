from random import randint

def computer_guess(low, high):
    num = randint(low, high)
    return num
def computer_ia(random_number, cguess, low, high):
    if cguess > random_number:
        high = cguess - 1
        return high
    elif cguess < random_number:
        low = cguess + 1
        return low
def batle_guess(x):
    random_number = randint(1, x)
    guess = 0
    cguess = 0
    low = 1
    high = x
    while guess != random_number and cguess != random_number:
        guess = int(input(f'guess a number bethween 1 and {x}: '))
        print(guess)
        cguess = computer_guess(low, high)
        print(cguess)
        if guess == random_number and cguess != random_number:
            print(f'Congrats! You have guessed the number {random_number}')
            break
        elif cguess == random_number and guess != random_number:
            print(f'The computer guessed  the number {random_number}')
            break
        elif guess == random_number and cguess == random_number:
            print(f'You and the computer guessed the number {random_number}')
            break
        elif guess < random_number:
            print('Sorry, guess again. Too low.')
            if cguess > random_number:
                high = cguess - 1
            elif cguess < random_number:
                low = cguess + 1
        elif guess > random_number:
            print('Sorry, guess again. Too high .')
            if cguess > random_number:
                high = cguess - 1
            elif cguess < random_number:
                low = cguess + 1

batle_guess(10)
