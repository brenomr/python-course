# USING FOR, RANGE
# Classes 043, 044, 045, 046

"""
Annotations:
Iterable: str, range, list or any object (with __iter__()) capable of return
one member at a time allowing it to be iterated (in a loop).
Reference: https://www.w3schools.com/python/python_iterators.asp
 FOR can make use of continue and break, like WHILE
"""

# Iterating on a range of numbers
# numbers = range(0, 10, 2) 
# for n in numbers:
#     print(n)

text = "Base" # Iterable

# Iterating a string.
# for l in text:
#     print(l)

# __iter__() and __next__()
iterator = iter(text) # Iterator

# Reaching the last letter from iterator
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# The next print will raise a StopIteration (no more letter to show)
# print(text.__next__())

# 'RECREATING FOR' behavior
while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break