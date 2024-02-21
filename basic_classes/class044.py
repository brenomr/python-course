"""
The problem of mutable params on Python functions
"""

def append_to_list(value, list=[]):
    list.append(value)
    return list

value1 = append_to_list('George')
append_to_list('Paul', value1)

print(value1) # ['George', 'Paul']

# The problem here is, every time the function
# is called, the list is the same, so the result
# isn't what we expect:

value2 = append_to_list('Emily')
append_to_list('Elizabeth', value2)

print(value2) # ['George', 'Paul', 'Emily', 'Elizabeth']

# So to avoid this behavior, we can create a new
# list every time the function is called:

def append_to_list2(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

value3 = append_to_list2('George')
append_to_list2('Paul', value3)

print(value3) # ['George', 'Paul']

value4 = append_to_list2('Emily')
append_to_list2('Elizabeth', value4)

print(value4) # A new list ['Emily', 'Elizabeth']
