"""
Using Metaclasses

How Python creates a class
type('class_name', ('typle with inheritance',), {'dict of class': 'values'})

__new__ of metaclass creates the class
__call__ of metaclass calls the __new__ of class an then the __init__ to initialize the class instance
__new__ of class creates and return the class instance
__init__ of class initializes the attributes of class instance
__call__ of metaclass finishes the class instance initialization

__new__(cls, name, bases, dct) creates a new class
__call__(cls, *args, **kwargs) creates and initializes a new class instance

"If you are asking if you need to use metaclasses, you don't.
Who really needs to use metaclasses, already knows what they
are and how to use them".
"""

class Fae:
    ...

f = Fae()
print(type(f))
print(type(Fae))

# How python creates a class
Bart = type('Bart', (object,), {})

bart = Bart()
print(type(bart))
print(type(Bart))


# Full example Metaclass

class Person:
    def __new__(cls, *args, **kwargs) -> Self:
        print('Custom New')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name) -> None:
        print('Custom Init')
        self.name = name

p1 = Person('Anna')