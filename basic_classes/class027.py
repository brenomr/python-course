"""
Uses of TRY/EXCEPT/FINALLY
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

def pasing_value():
    """ Base function to raise an error."""
    try:
        # Raising exception ZeroDivisionError
        result = 10 / 0
        print(result)

        # Raising exception ValueError
        wrong_parsed_number = int('Forcing an error.')
        print(f'If you reached this print, something is wrong... {wrong_parsed_number}')

    except ValueError:
        print('Wrong data was provide to parse int...')

    except (ZeroDivisionError, IndexError) as err:
        #Catching some error details

        print(f'NAME: {err.__class__.__name__}. MESSAGE: {err}.')
    except TypeError:
        print('Handle this error and then raise it...')
        raise

    except Exception as err:
        print(f'Generic exception: {err}.')

    finally:
        print('Finishing the process regardless of an error... It will be always executed...')

        # forcing an exception
        raise ValueError('Here, take this forced exception!')

# pasing_value()

def my_division(a: int, b: int):
    """Personal division..."""
    check_number_type(a, b)
    check_zero(b)

    return a/b

def check_zero(number):
    """Manual error handling."""
    if number == 0:
        raise ZeroDivisionError("You're trying to make a division by zero...")


def check_number_type(*numbers):
    """Check number type."""
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError(f"One of the arguments >> {number} << aren't number.")

my_division("test", 0)
