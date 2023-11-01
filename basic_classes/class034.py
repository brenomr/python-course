"""
Decorators

This example shows how to create a decorator function.
"""

from os import system

system('cls')

def string_inverter(string: str):
    """"A simple function to invert a string."""
    return string[::-1]

def is_string(string=None):
    """A simple function to check string type."""
    if not isinstance(string, str):
        raise TypeError("The given argument is not a string.")

def generate_inverter(function):
    """
    A simple decorator function to generate another
    function to validate a string type before inverting it.
    """

    def validate_and_invert_string(*args, **kwargs):
        """A closure function to validate and invert a string."""
        for arg in args:
            is_string(arg)

        return function(*args, **kwargs)

    return validate_and_invert_string

# This is te most complex way to decorate the function string_inverter
string_to_inverter = generate_inverter(string_inverter)
print(string_to_inverter('John Doe'))

# This is the simple and best way to decorate a function

@generate_inverter
def string_inverter_two(string: str):
    """A simple decorated function to invert a string."""
    return string[::-1]

print(string_inverter_two('Robinson Crusoe'))
