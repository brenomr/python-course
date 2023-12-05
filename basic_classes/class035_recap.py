"""
Recaptilation class
"""

def generic_decorator(func):
    """Generic decorator for recap."""

    print('Initializing generic decorator...')

    def exec_function(*args, **kwargs):
        result = 0

        if kwargs:
            # for index in kwargs: result += kwargs[index] --> better way below
            for index, value in kwargs.items(): result += value

        return func(*args, result)

    return exec_function

@generic_decorator
def my_sum(*args):
    """Generic sum for recap."""

    result = 0

    for value in args:
        result += value

    print(result)

my_sum(10, 5, 15, b = 3, x = 14, j = 1, z = 2)
