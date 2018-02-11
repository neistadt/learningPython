number_to_generate = int(input('How many fibonacci numbers do you want to generate? '))
fibonacci = []
while number_to_generate > 0:
    if len(fibonacci) in [0, 1]:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    number_to_generate -= 1

print('Fibonacci sequence:', fibonacci)
