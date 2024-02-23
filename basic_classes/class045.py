"""
Positional only arguments
We can 'protect' the args from be named by
adding a slash '/'. Some references at PEP0570
(peps.python.org/pep-0570).

The problem: We can rename the param as the code
changes, e.g:

def my_func(a, b) --> to --> def my_func(x, b)
my_func(a=5, b=5) --> ok --> my_func(a=5, b=5) --> error
"""

# Args can be positional or named
def my_sum(a, b):
    print(a + b)

# Works
my_sum(1,2)
my_sum(b=10, a=15)
my_sum(a=55, b=5)

# Only positional
def my_sub(a, b, /):
    print(a - b)

# Works
my_sum(1,2)

# Error: TypeError: my_sub() got some positional-only
# arguments passed as keyword arguments: 'a, b'
my_sub(a=5, b=2)


# Before slash only positional (args) are accepted,
# after we can use the named args (kwargs)
def my_sum2(a, b, /, c, d):
    print(a + b + c + d)

# Works
my_sum2(1, 2, c=2, d=5)

# Error
my_sum2(1, b=2, c=2, d=4)
