import argparse
import random
import sys
from datetime import date


def exercise1():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    repeats = int(input('How many times do you want to repeat the next message? '))

    current_year = date.today().year
    year_100 = current_year + (100 - age)

    for i in range(repeats):
        print('Hello {}! You will turn 100 in the year {}'.format(name, year_100))


def exercise2():
    number = int(input('Please provide a number: '))
    if number % 4 == 0:
        print(number, 'is a multiple of 4')
    elif number % 2 == 1:
        print(number, 'is an odd number')
    else:
        print(number, 'is an even number')


def exercise3():
    limit = int(input('Provide limit: '))
    print([x for x in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if x < limit])


def exercise4():
    number = int(input('Please provide a number to calculate divisors for: '))
    print(divisors(number))


def divisors(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


def exercise5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print({x for x in a if x in b})


def exercise5_1():
    a = [random.randint(1, 100) for x in range(random.randint(1, 50))]
    b = [random.randint(1, 100) for x in range(random.randint(1, 50))]
    print('a:', a)
    print('b:', b)
    print('intersection:', {x for x in a if x in b})


def exercise6():
    input_string = input('Input a string to test whether its a palindrome: ')
    is_palindrome = True
    for index, character in enumerate(input_string[:int(len(input_string) / 2)]):
        if character != input_string[-(index+1)]:
            is_palindrome = False
            break

    if is_palindrome:
        print('The word', input_string, 'is a palindrome')
    else:
        print('The word', input_string, 'is NOT a palindrome')


def exercise7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([x for x in a if x % 2 == 0])


def exercise8():
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    print('Let\'s play rock paper scissors!')
    keep_playing = True
    while keep_playing:
        choice = ['', '']
        for i in [0, 1]:
            choice[i] = repeat_until_valid('Player {}: Please enter rock, paper, '
                                           'or scissors: '.format(i+1), *rules.keys())

        # Evaluate who won
        if rules.get(choice[0]) == choice[1]:
            print('Player 1\'s {} beat Player 2\'s {}!'.format(choice[0], choice[1]))
        elif rules.get(choice[1]) == choice[0]:
            print('Player 2\'s {} beat Player 1\'s {}!'.format(choice[1], choice[0]))
        else:
            print('It\'s a tie!')

        play_again = repeat_until_valid('Do you want to play again (y/n)? ', 'y', 'n')
        if play_again.lower() == 'y':
            keep_playing = True
        else:
            keep_playing = False


def repeat_until_valid(input_prompt, *valid_values):
    choice = ''
    invalid_choice = True
    while invalid_choice:
        choice = input(input_prompt).lower()
        if choice not in valid_values:
            print('"{}" is not a valid choice. Please choose one of {}'.format(choice, list(valid_values)))
            invalid_choice = True
        else:
            invalid_choice = False

    return choice


def exercise9():
    winning_number = str(random.randint(1, 9))
    guesses = 0
    while True:
        guess_string = repeat_until_valid('Guess the value from 1 to 9 (type "exit" to quit): ',
                                          *(str(x) for x in range(1, 10)), 'exit')
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


# skipping exercise10 because it is identical to 5
def exercise11():
    number = int(input('Please provide a number to test whether its prime: '))
    if divisors(number) == [1, number]:
        print(number, 'is a prime number!')
    else:
        print(number, 'is NOT a prime number!')


def exercise12():
    choice = ''
    choices = []
    while choice != 'done':
        choice = input('Provide a number. Type "done" to stop: ')
        if choice.isnumeric():
            choices.append(choice)
        elif choice != 'done':
            print('Not a number or the word "done". Try again.')
        else:
            print('Finished List')

    print('Original List is:', choices)
    if len(choices) > 0:
        first_and_last = [choices[0], choices[-1]]
        print('First and Last elements are: ', first_and_last)
    else:
        print('Not enough elements')


def exercise13():
    number_to_generate = int(input('How many fibonacci numbers do you want to generate? '))
    fibonacci = []
    while number_to_generate > 0:
        if len(fibonacci) in [0, 1]:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        number_to_generate -= 1

    print('Fibonacci sequence:', fibonacci)


def exercise14():
    a = [1, 2, 3, 4, 5, 5, 1, 4, 4, 5, 3, 0]
    print('Original:             ', a)
    print('Removed (using lists):', remove_duplicates_using_lists(a))
    print('Removed (using sets): ', remove_duplicates_using_sets(a))


def remove_duplicates_using_lists(list_to_examine):
    result = []
    for x in list_to_examine:
        if x not in result:
            result.append(x)
    return result


def remove_duplicates_using_sets(list_to_examine):
    return list(set(list_to_examine))


def exercise15():
    sentence = input('Provide a long sentence:\n')
    print('Here\'s the sentence backwards:')
    print(" ".join(sentence.split()[::-1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute Learning Python exercises')
    parser.add_argument('exercise', action='store', type=int)
    parser.add_argument('-extra', action='store', type=int)
    args = parser.parse_args()

    if args.extra is not None:
        eval('exercise' + str(args.exercise) + '_' + str(args.extra) + '()')
    else:
        eval('exercise' + str(args.exercise) + '()')
