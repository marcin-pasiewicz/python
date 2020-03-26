from random import randint
import sys


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return
    else:
        print(f'hey bozo, I said {sys.argv[1]}~{sys.argv[2]}')


if __name__ == '__main__':
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
            run_guess(guess, answer)

        except ValueError:
            print('please enter a number')
            continue
