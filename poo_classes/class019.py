"""
Python Context Manager with classes

To create a context manager using classes, we need to
create a class with two methods: __enter__ and __exit__.
We can use these methods with "with", e.g.:
with open('file', 'w') as file: ...
"""

from pathlib import Path

FILE_PATH = f'{Path(__file__).parent}/misc/my_context_file.txt'

class MyContextManager:
    def __init__(self, file_path, mode) -> None:
        self.file_path = file_path
        self.mode = mode
        self.encoding = 'utf8'
        self._file = None

    def __enter__(self):
        print('Opening file...')
        self._file = open(self.file_path, self.mode, encoding=self.encoding)
        return self._file

    def __exit__(self, cls_exception, exception_, traceback_):
        print('Closing file...')
        self._file.close()

        # Forcing exception
        # raise TypeError('Type error occurs...')

        # DOING EXCEPTION STEPS
        # raise cls_exception
        # raise cls_exception(*exception_.args)
        # raise cls_exception(*exception_.args).with_traceback(traceback_)

        # EXPLANATION
        # cls_exception = class of exception
        # exception instance
        # traceback of exception
        # return True -> Will ignore the exception if it occurs

# EXAMPLE
# my_instance = MyContextManager()
# with my_instance as something:
    # The return of __enter__ will be stored in the
    # word after 'as', in this case, something
    # print(something)

with MyContextManager(FILE_PATH, 'w') as file:
    print('Writing file...')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
