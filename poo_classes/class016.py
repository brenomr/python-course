"""
Creating Exceptions

It's a good practice to create your own exceptions
adding at the word "Error" at the end of name

https://docs.python.org/3/library/exceptions.html

A new feature of exception from Python 3.11,
we can add notes on exceptions, e.g.:
var_exceptino.add_note('note')
"""

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def raise_exception():
    my_err = MyError('a', 'n', 'One error occured')
    my_err.add_note('Something wrong occured...')
    raise my_err


try:
    raise_exception()
except (MyError, TypeError) as err:
    print(err.__class__.__name__)
    print(err.args)
    ant_err = AnotherError('Occured again...')
    ant_err.add_note('Another note...')
    raise ant_err from err
