# FUNCTION PARAMETER OPTION *ARGS
# Classes 071, 072, 073

# In order to sent N arguments in a function, we can define paramater as:

def soma(*args):
    acc = 0

    for number in args:
        acc += number
    
    return acc

results = soma(1, 2, 10, 5, 3)
# print(results)

"""
Exercise:
1) Make a function to multiply all arguments not named,
return the result of the multiplication
2) Make a function to return if a number is even or odd
"""

def calc(*args):
    # To simplify, acc could be == 1
    acc = 0

    for index, number in enumerate(args):
        if index == 0:
            acc = number
        else:
            acc *= number
    
    return acc

def even_odd(number):
    return f"The number {number} is: {'Even' if number % 2 == 0 else 'Odd'}"

# Example of higher order function
def welcome(message):
    return message

print(welcome('Good morning...'))