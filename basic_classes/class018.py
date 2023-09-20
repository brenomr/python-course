# LIST
# Classes 048
""""
Empty list is always 
Lists are mutable
When deleting, Python reindexes all items within a list, the greater the list more processing power will be necessary
"""

string01, string02 = "ABCDE", "FGHIJ"
list_example01 = [string01, string02]
list_example02 = []

print(f'TYPE: {type(list_example01)}\n'\
      f'LIST: {list_example01}\n'\
      f'BOOL EXAMPLE 02: {bool(list_example02)}'
)

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
print(list_03)