"""
Checking if this class project is using camelCase
in an given file.

Some parts of this code was provided by Copilot.
"""

import re
import os

path = os.path.dirname(os.path.realpath(__file__))
path = f'{path}/class011.py'

def find_camelcase_functions(filename):
    with open(filename, 'r') as file:
        content = file.read()

    pattern = re.compile(r'def ([a-z]+[A-Z][a-zA-Z0-9_]*)\(')
    matches = pattern.findall(content)

    return matches

functions = find_camelcase_functions(path)
for function in functions:
    print(function)
