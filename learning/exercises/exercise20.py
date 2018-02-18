def search(numbers, target):
    print('Search:', numbers)

    if len(numbers) == 0:
        return False

    mid_index = len(numbers) // 2
    mid = numbers[mid_index]
    print('-- Mid:', mid)
    if mid == target:
        return True
    elif mid > target:
        return search(numbers[:mid_index], target)
    else:
        return search(numbers[mid_index+1:], target)


a = [56, 72, 90, 94, 105, 132, 145, 189, 190, 201, 234, 235, 236]
print(search(a, int(input('Enter number to search for: '))))
