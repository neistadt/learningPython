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
