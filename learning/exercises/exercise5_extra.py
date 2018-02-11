import random

a = [random.randint(1, 100) for x in range(random.randint(1, 50))]
b = [random.randint(1, 100) for x in range(random.randint(1, 50))]
print('a:', a)
print('b:', b)
print('intersection:', {x for x in a if x in b})
