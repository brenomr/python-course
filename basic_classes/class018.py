# DEFINING AND USING FUNCIONS
# Classes 065, 066, 067, 068, 069, 070

"""
Annotations:
- Functions name must star with lower case
- Functions can have parameters to receive arguments
"""

def Prints():
    print('A function who calls multiple methods... 1')
    print('A function who calls multiple methods... 2')

def welcome(user_name=None):
    print(f'Hello {user_name}, welcome!' if user_name else 'Welcome visitor!')

# Prints()
# welcome("Igor")
# welcome()

# Functions with default value, named and positional arguments
# Try to avoid  (0, ''), using None to validate "not defined" value

def soma(x, y, z=None):
    if z is not None:
        return f'{x=} + {y=} {z=} | x + y + z = {x + y + z}'
    else:
        return f'{x=} + {y=} | x + y = {x + y} | z not defined.'

# Positional arguments
# print(soma(10, 5, 25))

# Named arguments
# print(soma(y=10, x=5))


x = 1
def scope():

    # Changing external variable
    global x

    x = 2
    
    def other_scope():
        x = 3
        y = 4
        print(x, y)
    
    other_scope()
    print(x)

print(x)
scope()
print(x)