import argparse
import random
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
    number = int(input('Please provide a number to calculate divsors for: '))
    divisors = []
    for testDivisor in range(1, number + 1):
        if number % testDivisor == 0:
            divisors.append(testDivisor)

    print(divisors)


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute Learning Python exercises')
    parser.add_argument('exercise', action='store', type=int)
    parser.add_argument('-extra', action='store', type=int)
    args = parser.parse_args()

    if args.extra is not None:
        eval('exercise' + str(args.exercise) + '_' + str(args.extra) + '()')
    else:
        eval('exercise' + str(args.exercise) + '()')
