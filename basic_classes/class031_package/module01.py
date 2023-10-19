"""
This is the Module 01 from a package class031.

- The absolute path is necessary in order to allow module01
be executed in any module inside basic_classes if the path
is like this: 'from module02 import say_hello' then only the
modules inside class031_package will see module02, and if
module01 is imported by any module of basic_classes a module
error will be raised.

With the import of line 17:
- Any direct run from module01 will raise an error.
- Everything inside module02 will be exposed to any module
using module01.
"""

from class031_package.module02 import say_hello

# With __all__ only things inside the list will be
# exposed on imports like: from module01 import *
__all__ = [ 'name', 'personal_sum' ]

print(f'Module: {__name__}')

say_hello()

name = 'John Doe'

def personal_sum(a, b):
    return a + b
