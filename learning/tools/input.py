def repeat_until_valid(input_prompt, *valid_values, case_insensitive=True, output_change_case=True):
    choice, raw_choice = '', ''
    compare_values = valid_values
    invalid_choice = True
    if case_insensitive:
        compare_values = {str(v).lower() for v in valid_values}

    while invalid_choice:
        raw_choice = input(input_prompt)
        if case_insensitive:
            choice = raw_choice.lower()
        else:
            choice = raw_choice

        if choice not in compare_values:
            print('"{}" is not a valid choice. Please choose one of {}'.format(raw_choice, list(valid_values)))
            invalid_choice = True
        else:
            invalid_choice = False

    if output_change_case:
        return raw_choice.lower()
    else:
        return raw_choice
