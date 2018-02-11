def divisors(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]
