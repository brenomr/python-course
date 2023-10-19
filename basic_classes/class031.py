"""
PACKAGES
- Once module01 is imported an exception will be raised,
"ModuleNotFoundError: No module named 'module02'" because
module01 imports module02 and class031 on the main module
(basic_classes) don't know about module02
"""

from sys import path

# say_hello from module02 can be imported, once the absolute
# path was provided
from class031_package.module01 import personal_sum, name, say_hello
from class031_package import module01
import class031_package.module01

print(f'\nModule: {__name__}', end='\n'*2)
print(*path, sep='\n', end='\n'*2)

# can't be used in this way if not present in __all__ of module
print(personal_sum(15, 25))
print(class031_package.module01.personal_sum(10, 2))
print(module01.personal_sum(1, 3))
print(name)

say_hello()
