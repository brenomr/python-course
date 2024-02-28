"""
Defining and Using classmethod

With classmethod, we can invoke the
method without an object (instance),
like calling attribute year.

Classmethod is usefull to define
factories, where we can create other
instance, like the example bellow with
people with 50 years

"""

class Person:
    # class attribute
    year = 2024

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # regular method, used in objects (instances)
    def regular_method_hello(self) -> None:
        print('Hello traveler!')
    
    # with this decorator we can call this method
    # without self but cls (class) is necessary
    @classmethod
    def class_method_hello(cls) -> None:
        print('Hello without instance traveler!')
    
    # factory method
    @classmethod
    def person_with_50_years(cls, name):
        return cls(name, 50)
    
    @classmethod
    def anonymous_person(cls, age):
        return cls('Anonymous', age)

# calling year without instance
print(Person.year)

# this will work without instance
Person.class_method_hello()

# this will not work without instance
# Person.regular_method_hello()

Bob = Person.person_with_50_years('Bob')
print(Bob.__dict__)
Bob.regular_method_hello()

Anonymous = Person.anonymous_person(25)
print(Anonymous.__dict__)
