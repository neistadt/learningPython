def remove_duplicates_using_lists(list_to_examine):
    result = []
    for x in list_to_examine:
        if x not in result:
            result.append(x)
    return result


def remove_duplicates_using_sets(list_to_examine):
    return list(set(list_to_examine))


a = [1, 2, 3, 4, 5, 5, 1, 4, 4, 5, 3, 0]
print('Original:             ', a)
print('Removed (using lists):', remove_duplicates_using_lists(a))
print('Removed (using sets): ', remove_duplicates_using_sets(a))
