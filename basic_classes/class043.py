"""
Uses of method jdumps

The json.dumps is used to convert a Python object (dict) to
a string representation of a JSON object, parsing attributes
like True/False to true/false (some of JSON standards).
"""

import os
import json
from data.person import person

# Defining path and file name
path = os.path.dirname(os.path.realpath(__file__))
file_path = f'{path}/data/person.json'

# Converting dict to json and creating file
with open(file_path, 'w', encoding='utf8') as file:
    json.dump(person, file, indent=2, ensure_ascii=False)
    print(f'File created at: {file_path}')

# Reading file and converting json to dict
with open(file_path, 'r', encoding='utf8') as file:
    data = json.load(file)
    print(f'File readed: {data}')
