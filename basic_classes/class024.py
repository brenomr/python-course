# LAMBDA FUNCTIONS
"""
Annotations:
- It is a simple anonymous function, with one line and an expression
"""

#####################################################################
# Handle list using built in Python methods (not lambda function yet)
#####################################################################

number_list = [25, 42, 33, 53, 11, 2]

# sort the original list
number_list.sort()

# creates a sorted copy of a list
new_number_list = sorted(number_list)

##############################################
# Using lambda function to sort the dict list
##############################################

user_list = [
    {"name": "Rafaela", "surname": "Silva"},
    {"name": "José", "surname": "Alencar"},
    {"name": "Sílvia", "surname": "Fontelle"},
    {"name": "Fabrício", "surname": "Santos"},
]

# Using regular function to handle sort of a dict
def user_sort(item):
    return item["name"]

user_list.sort(key=user_sort)

# Same example, but with lambda using surname
# user_list.sort(key=lambda item: item["surname"])
new_user_list = sorted(user_list, key=lambda item: item["surname"])

# for user in new_user_list:
#     print(user)


####################################
# Using more complex lambda function
####################################

def execute(function, *args):
    return function(*args)

def addition(x, y):
    return x + y

# Runing multiples functions inside print with functions and lambda, both do the same thing
# print(execute(addition, 10, 12), execute(lambda x, y: x + y, 100, 15))

print(execute(lambda *args: sum(args), 10, 25, 15, 12))
