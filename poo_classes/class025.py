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
# print(type(f))
# print(type(Fae))

# How python creates a class
Bart = type('Bart', (object,), {})

bart = Bart()
# print(type(bart))
# print(type(Bart))


# Full example Metaclass

def custom_repr(self):
    return f'{type(self).__name__}({self.name})'

# The new from Metaclass returns the class itself
# We can do tasks before the class creation
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Metaclass New')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 'Value' # Add an attribute to the cls
        cls.__repr__ = custom_repr # Add a method to the cls
        if 'talk' not in cls.__dict__ or not callable(cls.__dict__['talk']):
            raise NotImplementedError('You need to implement the talk method')
        return cls
    
    # without call we can't access the instance (self)
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        print(instance.__dict__)
        return instance

class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Person New')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name) -> None:
        print('Person Init')
        self.name = name

    def talk(self):
        print("I'm talking...")

# even not creating an instance, the __new__ from metaclass is called
p1 = Person('Anna')
print(p1)
