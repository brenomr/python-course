# EXERCISE, ordering the numbers (ASC)

while True:
    try:
        first_value = input('Insert the first value: ')
        second_value = input('Insert the second value: ')

        first_is_valid_number = type(first_value) == int or type(first_value) == float
        second_is_valid_number = type(second_value) == int or type(second_value) == float

        if not first_is_valid_number:
            raise Exception("The first value isn't a valid number!")
        elif not second_is_valid_number:
            raise Exception("The second value isn't a valid number!")
        
        if first_value < second_value:
            print(f"The first value: {first_value} is less than the second one: {second_value}.")
            break
        elif first_value > second_value:
            print(f"The second value: {second_value} is less than the first one: {first_value}.")
            break
        else:
            print(f"Both values: {first_value} and {second_value} are equal.")
            break
    except:
        raise Exception("Error...")
