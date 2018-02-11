import learning.tools.input as utils

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
        choice[i] = utils.repeat_until_valid('Player {}: Please enter rock, paper, '
                                             'or scissors: '.format(i + 1), *rules.keys())

    # Evaluate who won
    if rules.get(choice[0]) == choice[1]:
        print('Player 1\'s {} beat Player 2\'s {}!'.format(choice[0], choice[1]))
    elif rules.get(choice[1]) == choice[0]:
        print('Player 2\'s {} beat Player 1\'s {}!'.format(choice[1], choice[0]))
    else:
        print('It\'s a tie!')

    play_again = utils.repeat_until_valid('Do you want to play again (y/n)? ', 'y', 'n')
    if play_again.lower() == 'y':
        keep_playing = True
    else:
        keep_playing = False
