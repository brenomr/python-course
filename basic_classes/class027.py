"""
Uses of TRY/EXCEPT/FINALLY
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
    except Exception as err:
        print(err)

    finally:
        print('Finishing the process knowing about the error and...')

pasing_value()
