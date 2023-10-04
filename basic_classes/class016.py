# LIST, UNPACKING AND TUPLES
# UNPACKING DICT. ARGS AND KWARGS
# LIST COMPREHENSION, MAPPING AND FILTERING LISTS
# Classes 048, 049, 050, 051, 052, 053, 054, 083, 084

""""
Annotations:
Empty list is always 
Lists are mutable
List are iterable
When deleting, Python reindexes all items within a list, the greater the list more processing power will be necessary
"""

import pprint

string01, string02 = "ABCDE", "FGHIJ"
list_example01 = [string01, string02]
list_example02 = []

####################
# Methods and loops
####################

for item in list_example01:
    list_example02.append(item)

# Manual insert
list_example02[0] = 'any value'

# Deleting an value
del list_example02[1]

# Adding new value at the end of list
list_example01.append('new value at the end of list')

# Remove the last item of a list if one index isn't informed
removed_value = list_example01.pop(0)

# Remove all items from a list
list_example01.clear()

# Adds a new value to the list based on a given index
index = 0
value = 'new value'

list_example02.insert(index, value)

# Extend a list
list_03 = ['ABJJJ']
list_03.extend(list_example02)
# print(list_03)

# In this example we don't have a copy of the list, we just
# define 2 variables pointing to the same list, if we change
# anything in list_a it will be reflected on list_b
list_a = [1, 2, 3]
list_b = list_a

list_b.append('add something in list_b')
# print(list_a)

# In order to copy any object (list) we should use .copy()
list_c = list_a.copy()
list_c.append('add something in list_c')
# print(list_a)

####################
# Exercise LIST
####################
# Using the basic methods already explained, try to show
# the indexes of a list, without any list method.

list_exercise = ['Manuela', 'Érika', 'Regina', 'Felipe']
index = 0

for item in list_exercise:
    # print(f'{index} - {item}')
    list_exercise[index] = f'{str(index).zfill(3)} {item}'
    index += 1

# print(list_exercise)

# Professor suggestion
# index_p = range(len(list_exercise))
# for i in index_p:
#     print(i, list_exercise[i][4:]) #[4:] to remove the first 4 characters


######################
# UNPACKING
######################

list_to_unpack = ['John', 'Alan', 'Richie']

# More variables than values or vice versa will lead to a ValueError exception
name1, name2, name3 = list_to_unpack

"""
To avoid ValueError exception, we can keep all unwanted values using "*" before
var name, by convention, store unnecessary data in "*_"
The issue here is all unnecessary stored data
"""
name4, *unwanted_values = list_to_unpack
_, second_name, *_ = list_to_unpack

# print(name4, unwanted_values, second_name)

# Unpacking multiple values inside a method
# print(*list_to_unpack)

######################
# TUPLES
######################
#
# Tuples are immutable, trying to change it will end in TypeError
# e.g tuple_of_names[0] = 'New name...'

tuple_of_names = ('Bob', 'Marley')

tuple_from_list = tuple(list_to_unpack)
# print(tuple_from_list)

######################
# ENUMERATE METHOD
######################

enumerated_list = enumerate(list_to_unpack)

# Calling next option on enumerated_list
# print(f'OUT OF THE FOR: {next(enumerated_list)}')

# for i in enumerated_list:
#     print(f'INSIDE FOR: {i}')

########################
# UNPACKING DICTIONARIES
########################

person = {
    "name": "John",
    "surname": "Doe",
}

details = {
    'height': 1.76,
    'weight': 78,
}

# Getting keys. Because with iterable (for) we catch on return the keys
name, surname = person

# Getting values
name, surname = person.values()
# print(name, surname)

# Getting items() --> return tuples, we need to unpack it
(kname, vname), (ksur, vsur) = person.items()

# Getting values with iterable
# for key, value in person.items():
#     print(f'{key}: {value}', '\n------------')

# Extracting multiples dictionaries, and adding new keys
complete_person = {**person, **details, 'city': 'New York'}
# print(complete_person)

##############################
# ARGS AND KWARGS in functions
##############################

# KWARGS, named arguments


# def show_words(*args, **kwargs):
# print(f'Your positional args: {args}')
# print(f'Your named kwargs: {kwargs}\n')

# for key, value in kwargs.items():
#     print(f'{key}: {value}', '\n------------\n')

# show_words(10, 12, 'lime', name="John", surname="Sullivan", age=25)
# show_words('positional argument 1', 2, **complete_person)


####################
# LIST COMPREHENSION
####################

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

# base insert data on list
custom_list = []
for number in range(10):
    custom_list.append(number)

# Creating a new list using list comprehension, based on another list, doubling its values
new_list = [number * 2 for number in custom_list]

# print(custom_list)
# print(new_list)

products = [
    {'name': 'Product 001', 'price': 105},
    {'name': 'Product 002', 'price': 55},
    {'name': 'Product 003', 'price': 92},
    {'name': 'Product 004', 'price': 115},
]

# creating a new list with dict, without change the first one
new_products = [
    {**product, 'price': round(product['price'] * 1.1, 2)}
    if product['price'] > 100 else {**product} for product in products
]

# Filtering data before create new list
# Elements before FOR are mappings, and after are filters, e.g:
# new_list = [ MAPPINGS for n in range(10) ]
# new_list = [ n for n in range(10) FILTERS ]
evens_list = [ number for number in range(10) if number % 2 == 0 ]

lower_price_products = [ product for product in products if product['price'] < 100 ]

# pprint.pprint(lower_price_products)


#######################################
# List comprehension with multiples FOR
#######################################

#Regular method, without list comprehension
# list_for_for = []
# for x in range(3):
#     for y in range(3):
#         list_for_for.append((x, y))

# print(list_for_for)

# With list comprehension
list_for_for = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(list_for_for)
