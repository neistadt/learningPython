input_string = input('Input a string to test whether its a palindrome: ')
is_palindrome = True
for index, character in enumerate(input_string[:int(len(input_string) / 2)]):
    if character != input_string[-(index + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print('The word', input_string, 'is a palindrome')
else:
    print('The word', input_string, 'is NOT a palindrome')
