"""
Exercise 011

The functions from the base code are returning errors because
one argument is missing 'y', in this exercise is necessary to
suspend the function in order to allow future use of it with
the missing argument (closure).

Base code:

def own_sum(x, y):
    return x + y

def own_multiplication(x, y):
    return x * y

def execution(function, *args):
    return function(*args)

execution(own_sum, 2)
execution(own_multiplication, 2)
"""

def own_sum(x, y):
    """Sum function."""
    return x + y

def own_multiply(x, y):
    """Multiply function."""
    return x * y

def function_creator(function, x):
    """Function to create other functions."""
    def execution(y):
        return function(x, y)
    return execution

execute_sum = function_creator(own_sum, 3)
execute_multiplication = function_creator(own_multiply, 2)

print(execute_sum(7))
print(execute_multiplication(5))
