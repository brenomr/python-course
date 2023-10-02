# DICT more methods
# Classes 076 (pt-02)

import copy

person = {
    'name': 'Lorenzo',
    'surname': 'Santos',
    'age': 45,
    'lucky_numbers': [1, 7, 10]
}

# number of keys. Also could be print(person.__len__())
# print(len(person))

# show the keys name
# print(person.keys())

# show the keys values
# print(person.values())

# to return keys and values in tuples
# print(person.items())

# get keys and values in items
# for key, value in person.items():
    # print(f'{key} -- {value}')

# setdefult: add a key if it not exists
# person.setdefault('nickname', 'Not defined...')
# print(person['nickname'])

# simple copy
person_copy = person.copy()

# copy method == shallow copy, it doesn't copy mutable object
# inside a object, both will change, print them to see
person_shallow_copy = person.copy()
person_shallow_copy['lucky_numbers'][1] = 55

# in order to COPY EVERYTHING (use print)
person_deep_copy = copy.deepcopy(person)
person_deep_copy['lucky_numbers'][1] = 33

# pop to remove a key from dictionary
removed_key = person.pop('name')

# pop item to remove the last key from dict
removed_last_key = person.popitem()

# can update a key, or add new ones
person.update({ 'name': 'Marcelo', 'car': 'CPX-4454'})

# another ways to update
person.update(car='JBW-5555', surname='Alencar')
name_to_update = ('name', 'Marcos'),
person.update(name_to_update)
