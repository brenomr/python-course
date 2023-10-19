"""
Understanding your own MODULE

Annotations:
- The first module know by Python will be always: __main__
- You can import the entire module or some parts (like class028 with os and sys)
- The Python Know the folder where the __main__.
- Python doesn't know modules on parent folders (above folder where __main__ is)
- Python know all modules and packages on sys.path
"""
import sys

# You need to create a module in this path in order to avoid errors
sys.path.append(r"d:\projects\custom-module")

import custom_module
import class029_module
from class029_module import hello_traveler

print(f'Showing THIS MODULE name by special variable __name__: {__name__}', end='\n'*2)
print('Paths on sys reconized by Python:', *sys.path, sep='\n', end='\n'*2)
class029_module.hello_traveler('CJ')
hello_traveler('John Doe!')
