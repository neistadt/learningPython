import requests
import random
import string
import learning.tools.input as utils


def fetch_random_characters(random_configs):
    candidates = []
    for config in random_configs:
        pop = config['pop']
        min_rand = config['min']
        max_rand = config['max']
        random_num = random.randint(min_rand, max_rand)
        for i in range(random_num):
            candidates.append(random.choice(pop))

    random.shuffle(candidates)
    return ''.join(candidates)


def fetch_words(number_of_words):
    parameters = {
        'minLength': 6,
        'limit': number_of_words,
        'api_key': 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
    }
    r = requests.get('http://api.wordnik.com/v4/words.json/randomWords', parameters)
    r.raise_for_status()
    return [w['word'] for w in r.json()]


strength = utils.repeat_until_valid('Do you want a weak or strong password? ', 'weak', 'strong',
                                    output_change_case=True)
password = ''

if strength == 'weak':
    print('You want a weak password. Here you go:')
    print('Generating using 2 random words from WordNik...')
    words = fetch_words(2)
    password = words[0] + words[1]
else:
    print('You want a strong password. Here you go:')
    print('Generating using a series of random characters...')
    password = fetch_random_characters([
        {'pop': string.ascii_lowercase, 'min': 3, 'max': 6},
        {'pop': string.ascii_uppercase, 'min': 3, 'max': 6},
        {'pop': string.punctuation, 'min': 3, 'max': 6},
        {'pop': string.digits, 'min': 3, 'max': 6}
    ])

print('PASSWORD =', password)
