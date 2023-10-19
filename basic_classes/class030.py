"""
Mode about MODULE (reloading a module)

Annotations:
- Modules are singleton, there is just one instance of them on the entire program
- In order to import a module again, we can make use of importlib
"""

import importlib

import class030_module

print(class030_module.name)

for i in range(10):
    # This will not work, because import module in Python is singleton
    # import class030_module

    importlib.reload(class030_module)
    print(i)

print('\nFinish')
