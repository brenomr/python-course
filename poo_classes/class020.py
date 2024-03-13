"""
Context Manager with functions (generators)
"""
from pathlib import Path
from contextlib import contextmanager

FILE_PATH = f'{Path(__file__).parent}/misc/my_func_context_file.txt'

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file...')
        my_file = open(file_path, mode, encoding='utf8')
        yield my_file # yield turn the function into a generator
        print('Closing file...')
    except Exception as err:
        print(err)
    finally:
        file.close()

with my_open(FILE_PATH, 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    print('with', file)
