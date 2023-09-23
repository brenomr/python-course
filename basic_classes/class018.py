# LIST, UNPACKING AND TUPLES
# Classes 048, 049, 050, 051, 052, 053, 054
""""
Empty list is always 
Lists are mutable
List are iterable
When deleting, Python reindexes all items within a list, the greater the list more processing power will be necessary
"""

string01, string02 = "ABCDE", "FGHIJ"
list_example01 = [string01, string02]
list_example02 = []

# print(f'TYPE: {type(list_example01)}\n'\
#       f'LIST: {list_example01}\n'\
#       f'BOOL EXAMPLE 02: {bool(list_example02)}'
# )

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
list_a = [1,2,3]
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

index_p = range(len(list_exercise))

# for i in index_p:
#     print(i, list_exercise[i][4:]) #[4:] to remove the first 4 characters added on line 78


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
#print(f'OUT OF THE FOR: {next(enumerated_list)}')

# for i in enumerated_list:
#     print(f'INSIDE FOR: {i}')

#########################
# Exercise LIST AND TUPLE
#########################
"""
PT/BR: Criar uma lista de compra com listas, usuário deve
ter possiblidade de: Adicionar, apagar ou listar itens.
Inpedir que programa retorn erros de indices inexistentes.
"""

import os
os.system('clear')

shopping_list = ['avoc']

while True:
    try:
        print('\n--------------------\n'\
              '| Select an option |\n'\
              '--------------------'
        )
        option = input('[I]nsert [R]emove [L]ist [E]xit: ').lower()

        if len(option) > 1 or option not in 'irle':
            os.system('clear')
            print('Invalid Option:\n'\
                  'Options are: I, R or L and one letter at time.'
            )
            continue

        if option == 'e':
            break

        if option == 'i':
            os.system('clear')
            item_to_add = input('Insert the item you want to buy: ')
            shopping_list.append(item_to_add)

        elif option == 'r':
            if len(shopping_list) == 0:
                os.system('clear')
                print('Nothing to be removed.')
                continue
            else:
                item_to_remove = int(input('Insert the item ID to be removed: '))
                shopping_list.pop(item_to_remove)
                os.system('clear')
                print('Item sucessfully removed!')
                continue

        elif option == 'l':
            os.system('clear')

            if len(shopping_list) == 0:
                print('Nothing to be listed.')
                continue
            else:
                enum_shopping_list = enumerate(shopping_list)
                for item in enum_shopping_list:
                    print(item)
                continue
    except Exception as err:
        if type(err) == IndexError:
            os.system('clear')
            print('No item found with given ID.')
            continue
        print(type(err))