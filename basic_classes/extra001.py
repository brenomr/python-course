"""Module providing a function to return the sum of numbers in a string."""

from os import system

system('cls')

def sum_digits_from_string(string):
    """
    Return the sum of numbers in a string.
    """

    sum_of_digits = 0

    # --------------------
    # Not a good practice:
    # --------------------

    # for i in range(0, len(string)):
    #     sum_of_digits += int(string[i])

    # --------------
    # Good practice:
    # --------------

    # for i in string:
    #     sum_of_digits += int(i)

    # ----------------------------------
    # Good practice (if you need index):
    # ----------------------------------

    # for i, number in enumerate(string):
    #     sum_of_digits += int(number)

    for number in string:
        try:
            sum_of_digits += int(number)
        except ValueError:
            continue

    return sum_of_digits

RESULT = sum_digits_from_string('1,2,3,4,5,10')

print(RESULT)
