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

def own_sum(x):
    """Sum function generator."""
    def exec_sum(y):
        return x + y
    return exec_sum

def own_multiply(x):
    """Multiply function generator."""
    def exec_multiply(y):
        return x * y
    return exec_multiply

def execution(function, *args):
    """Function to execute other functions"""
    return function(*args)

execute_sum = execution(own_sum, 3)
execute_multiplication = execution(own_multiply, 2)

print(execute_sum(7))
print(execute_multiplication(5))
