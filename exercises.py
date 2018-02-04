import argparse
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute Learning Python exercises')
    parser.add_argument('exercise', action='store', type=int)
    args = parser.parse_args()

    eval('exercise'+str(args.exercise)+'()')
