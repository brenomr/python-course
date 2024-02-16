"""
Recursive functions
It's a kind of function that calls itself

Warning: a recursive function without a base case will cause a stack
overflow, where too many functions are called and the stack gets full.

Obs: Stack alocates memory for each function call.

By default Python has a limit of 1000 recursive calls, but it can be
changed with the setrecursionlimit function from the sys module, but
is recommended to avoid using it.

from sys import setrecursionlimit
setrecursionlimit(100)
"""

def recursive_function(value):
    print('Value in:', value)
    
    if value == 0:
        return None
    else:
        return recursive_function(value - 1)

def counter(start, limit):
    print('Start in:', start)

    if start == limit:
        return None
    else:
        return counter(start + 1, limit)


def factorial(value):
    if value <= 1:
        return 1
    else:
        return value * factorial(value - 1)

# recursive_function(5)
# counter(9, 15)
print(factorial(10))
