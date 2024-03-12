"""
Using classes with __init__ and __new__

__init__ and __new__ it's similar to
the constructor in other languages.

init it's more common to use

new - creates and return the object, because
of that new receives 'cls' instead of 'self'.
New makes the 'self' for init.

init - initialize the object

__new__ is good if you need to intercept
the object before before it's initialized.

__new__ always need to return an object

remember: __new__ occurs before __init__

__init__ always need to return None

"""

class A:
    def __new__(cls, *args, **kwargs):
        print('Creating the instance of A()')
        instance = super().__new__(cls)
        print('Doing something before returning A()')
        return instance

    def __init__(self) -> None:
        print(f'Initializing {self.__class__.__name__}')

    def __repr__(self) -> str:
        return 'Instance of A()'

# basic instancing
# a = A()
# print(a)

# what is Python doing above:
# a = object.__new__(A)
# a.__init__()
# print(a)

a = A()
print(a)
