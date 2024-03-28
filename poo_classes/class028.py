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

# with dataclass(init=False) we can create a class without __init__ method
# allowing us to create the class with a custom __init__


@dataclass
class Person:
    name: str
    lastname: str
    age: int

    # with __post_init__ we can define custom attributes, example
    # def __post_init__(self):
    #     self.full_name = f'{self.name} {self.lastname}'

    @property
    def full_name(self) -> str:
        return f'{self.name} {self.lastname}'

    @full_name.setter
    def full_name(self, full_name):
        name, *lastname = full_name.split(' ')
        self.name = name
        self.lastname = ' '.join(lastname)


if __name__ == '__main__':
    # Example of use
    fernando = Person('Fernando', 'Alonso', 30)
    fernando2 = Person('Fernando', 'Alonso', 30)
    print(fernando)
    print(fernando.full_name)

    # Since __eq__ is present, we can compare objects

    amelinda = Person('Amelinda', 'Almeida', 30)
    amelinda.full_name = 'Amelinda Araujo Azevedo'
    print(amelinda)
    print(fernando == amelinda)
    print(fernando == fernando2)
