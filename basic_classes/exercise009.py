# Exercise Duplicated Number

"""
Return the first duplicated number of a list
"""

all_lists = [
    [2, 3, 1, 2, 5, 9, 7, 1, ],
    [1, 4, 9, 8, 9, 4, 8],
    [1, 4, 9, 4, 7, 8, 9, 4, 8],
    [1, 5, 7, 6, 5, 7, 8],
    [1, 2, 3, 4, 5],
]

def check_duplicated_number(list_of_numbers):
    """ Function to check the first duplicated number."""

    checked_numbers = []
    result = -1

    for number in list_of_numbers:
        if number in checked_numbers:
            result = number
            break

        checked_numbers.append(number)

    return result

for base_list in all_lists:
    print(check_duplicated_number(base_list))
