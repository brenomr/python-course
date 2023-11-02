"""
Decorators - part II
"""

from os import system

system('cls')

def function_factory(func):
    """Decorator. Function factory to an easily understand."""

    print('Executing the decorator.')

    def inner_function(*args, **kwargs):
        """Inner (or nested) function."""

        print('Executing an inner function...')

        return func(*args, **kwargs)

    return inner_function

# When a decorator is defined, Python will always execute the
# first function (in this example decorator) at the start, try
# run this script without calling own_sum
@function_factory
def own_sum(x, y):
    """Simple sum."""
    print(f'The sum is { x + y }.')

own_sum(5, 5)

# Using the decorator with the 'complex' method
multiply = function_factory(lambda x, y: f'The multiplication is {x * y}.')
print(multiply(3,3))
