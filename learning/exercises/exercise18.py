import random

answer = '{0:04d}'.format(random.randint(0, 9999))
# print('DEBUG:', answer)
num_guesses = 0
game_over = False
while not game_over:
    guess = input('Enter your guess:\n')
    num_guesses += 1
    if len(guess) != len(answer):
        print('Guess must be {} digits long'.format(len(answer)))
    elif guess == answer:
        print('Congrats! You guessed it in {} guesses!'.format(num_guesses))
        game_over = True
    else:
        letters = list(answer)
        not_matched = []
        cows = 0
        bulls = 0
        for place, letter in enumerate(guess):
            if answer[place] == letter:
                cows += 1
                letters.remove(letter)
            else:
                not_matched.append(letter)

        for letter in not_matched:
            if letter in letters:
                bulls += 1
                letters.remove(letter)

        cow_msg = 'cows'
        bull_msg = 'bulls'
        if cows == 1:
            cow_msg = 'cow'
        if bulls == 1:
            bull_msg = 'bull'
        print('{} {}, {} {}'.format(cows, cow_msg, bulls, bull_msg))
