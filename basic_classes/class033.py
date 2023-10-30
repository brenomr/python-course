"""
Global variables
https://docs.python.org/3.11/library/functions.html#globals

Free variables
https://docs.python.org/3.11/library/functions.html#locals
"""

def external_function(x):
    """Function to handle free variables."""

    # 'a' is a free variable, because can be used inside
    # other functions in addition to external_function
    a = x

    def internal_function():

        # To check free variables. Another way instead locals:
        # internal_function.__code__.co_freevars
        print(locals())

        return a
    return internal_function

# my_function1 = external_function('Value 1')
# my_function2 = external_function('Value 2')

# print(my_function1())
# print(my_function2())

def concatenate(initial_string):
    """Concatenate function."""
    result = initial_string

    def concat(new_string=''):
        # An UnboundLocalError will be raised, because this variable
        # (result) can't be changed inside concat, in order to avoid
        # such exception, we can define it as nonlocal
        # result += new_string

        nonlocal result
        result += new_string
        return result

    return concat

base_string = concatenate('base')
base_string(' to')
base_string(' concatenate.')

print(base_string())
