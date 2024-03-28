"""
Using dataclasses

The module dataclasses is a decorator that allows you to create classes with
less code. It's implementes all the methods that we've seen in the previous
classes. Methods like __init__, __str__, __repr__, even others not used like
__eq__ and __hash__.

dataclass == syntactic sugar

Described in PEP 557, it's available from Python 3.7.
More details: https://docs.python.org/3/library/dataclasses.html

From Person from exercise 003, we can create a class with the same attributes
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

# Example of use


fernando = Person('Fernando', 30)
fernando2 = Person('Fernando', 30)
print(fernando)

# Since __eq__ is present, we can compare objects

amelinda = Person('Amelinda', 30)
print(fernando == amelinda)
print(fernando == fernando2)
