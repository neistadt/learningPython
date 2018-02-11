import random
import sys
import learning.tools.input as utils

winning_number = str(random.randint(1, 9))
guesses = 0
while True:
    guess_string = utils.repeat_until_valid('Guess the value from 1 to 9 (type "exit" to quit): ',
                                            *range(1, 10), 'exit')
    if guess_string == 'exit':
        print('Quiting the game. The answer was {} and you made {} guesses'.format(winning_number, guesses))
        sys.exit()
    elif guess_string == winning_number:
        guesses = guesses + 1
        print('You won! It took you {} guesses'.format(guesses))
        sys.exit()
    else:
        guesses = guesses + 1
        print('Wrong! Try again!')
