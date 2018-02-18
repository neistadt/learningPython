import learning.tools.project as project

with project.resource('Training_01.txt') as f:
    categories = {}

    for line in f:
        category = str(line).split('/')[2]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

print(categories)
