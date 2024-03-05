"""
Class Inheritance (lines 20 ~ 65)
Class method sobreposition (lines 67 ~ 122)

Inheritance allows us to define a class that inherits methods and properties from another.
"One object is a type of another object"

Super class(class above, e.g: Person):
- super class
- base class
- parent class

Sub class(class below, e.g: Student):
- sub class
- child class
- derived class

For details about the class: help(Client)
"""

class Person():

    def __init__(self, name, lastname = None, age = None) -> None:
        self._name = name
        self._lastname = lastname
        self._age = age

    @property    
    def full_name(self) -> str:
        return f'{self._name} {self._lastname}'

    @full_name.setter
    def full_name(self, fullname) -> None:
        name, lastname = fullname.split(' ')
        self._name = name
        self._lastname = lastname

    @property
    def age(self) -> int:
        return self._age    

    @age.setter
    def age(self, age) -> None:
        self._age = age
    
    def show_name(self) -> None:
        print(f'From class: {self.__class__.__name__}')
        print('Name:', self._name)

class Student(Person):
    def show_name(self) -> None:
        print(f'From class: {self.__class__.__name__}')
        print('Name:', self._name)

class Client(Person):
    ...

mike = Student('Mike', 'Smith', 25)
ana = Client('Ana', 'Silva', 33)

# In help(Student) we can see the # Method Resolution Order (MRO),
# valid for attributes and methods etc. Example: show_name()

# mike.show_name() # show_name from Student class
# ana.show_name() # show_name from Person class

class PersonalString(str):

    # This will "break" upper method from str class
    # def upper(self):
    #     ...

    # This will return the original upper (from super)
    # but allowing us to customize sumething in the way
    def upper(self):
        print('Calling personal UPPER method')
        result = super().upper()
        print('After super()')
        return result

niguel = PersonalString('Niguel')
# print(niguel.upper())

class A:
    cls_att_a = 'A'

    def __init__(self, attribute_a):
        self.att_a = attribute_a

    def method(self):
        print('A method')

class B(A):
    cls_att_b = 'B'

    # to keep the __init__ from A
    def __init__(self, attribute_a, attribute_b):
        super().__init__(attribute_a)
        self.att_b = attribute_b

    def method(self):
        print('B method')

class C(B):
    cls_att_c = 'C'
    def method(self):
        # implicity: super() == super(C, self)
        method_from_b = super(C, self).method
        method_from_a = super(B, self).method
        method_from_a()
        method_from_b()
        print('C method')

c = C('ATTRIBUTE A', 'ATTRIBUTE B')
c.method()
print(c.att_a, c.att_b)

# When calling super() without arguments, it will
# call the method from the next class in the MRO
print(C.mro())
print(B.mro())
print(A.mro())
