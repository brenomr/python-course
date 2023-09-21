# LIST
# Classes 048, 049, 050
""""
Empty list is always 
Lists are mutable
List are iterable
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

# In this example we don't have a copy of the list, we just
# define 2 variables pointing to the same list, if we change
# anything in list_a it will be reflected on list_b
list_a = [1,2,3]
list_b = list_a

list_b.append('add something in list_b')
print(list_a)

# In order to copy any object (list) we should use .copy()
list_c = list_a.copy()
list_c.append('add something in list_c')
print(list_a)

####################
# Exercise
####################
# Using the basic methods already explained, try to show
# the indexes of a list, without any list method.

list_exercise = ['Manuela', 'Érika', 'Regina', 'Felipe']
index = 0

for item in list_exercise:
    # print(f'{index} - {item}')
    list_exercise[index] = f'{str(index).zfill(3)} {item}'
    index += 1

print(list_exercise)

# Professor suggestion

index_p = range(len(list_exercise))

for i in index_p:
    print(i, list_exercise[i][4:]) #[4:] to remove the first 4 characters added on line 78