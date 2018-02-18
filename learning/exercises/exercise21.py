import learning.exercises.exercise17 as nyt

path = input('Provide path to output NYT articles: ')
with open(path, 'w') as f:
    f.write('\n'.join(nyt.find_stories()))
