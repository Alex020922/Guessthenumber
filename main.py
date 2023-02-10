import random


def guess(x):
    random_number = random.randint(1, x)
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input(f'Guess a number between 1 and {x}:  '))
        print(random_number)
    guess(10)
