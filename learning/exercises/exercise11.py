import learning.tools.math as learning_math

number = int(input('Please provide a number to test whether its prime: '))
if learning_math.divisors(number) == [1, number]:
    print(number, 'is a prime number!')
else:
    print(number, 'is NOT a prime number!')
