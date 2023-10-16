"""
Using MODULES (import, from, as, and *)
https://docs.python.org/3/py-modindex.html
"""

# import everything
import os
import sys

# import specific methods
from os import system

# import specific methods with alias
from sys import platform as plataforma

# avoid import everything with *, it's a bad practice
from os import *

system('clear')
print('Hello cleaned bash!\n')

# Import the entire module (sys) has some good uses,
# e.g we can define variables with the same method
#  name from the imported module without conflict:

platform = 'Somewindows'
print(sys.platform)
print(platform, end='\n\n')
print(plataforma)
