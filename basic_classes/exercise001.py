# EXERCISE, ordering the numbers (ASC)

while True:
    try:
        first_value = input('Insert the first value: ')
        second_value = input('Insert the second value: ')

        first_value_parsed = float(first_value)
        second_value_parsed = float(second_value)
        
        if first_value_parsed < second_value_parsed:
            print(f"The first value: {first_value_parsed} is less than the second one: {second_value_parsed}.")
            break
        elif first_value_parsed > second_value_parsed:
            print(f"The second value: {second_value_parsed} is less than the first one: {first_value_parsed}.")
            break
        else:
            print(f"Both values: {first_value_parsed} and {second_value_parsed} are equal.")
            break
    except Exception as err:
        if type(err) == ValueError:
            print('You must insert only numbers!')
            exit = input('Type 0 to exit or any other key. ')
            if exit == '0':
                break
        else:
            raise Exception(err)