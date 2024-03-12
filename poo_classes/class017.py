"""
What is 'dunder' or magic methods

Dunder == double underscore == __dunder__

Dunder is used on methods that's already exists
on Python, some examples:

__lt__(self,other) -> less than (self < other)
__le__(self,other) -> less than or equal (self <= other)
__gt__(self,other) -> greater than (self > other)
__ge__(self,other) -> greater than or equal (self >= other)
__eq__(self,other) -> equal (self == other)
__ne__(self,other) -> not equal (self != other)
__add__(self,other) -> addition (self + other)
__sub__(self,other) -> subtraction (self - other)
__mul__(self,other) -> multiplication (self * other)
__truediv__(self,other) -> division (self / other)
__new__(cls, *args, **kwargs) -> create a new instance
__str__(self) -> return a string representation of the object
__repr__(self) -> return a string representation of the object
__init__(self) -> initialize a new instance

More info:
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""

class Coordinates:
    """
    __repr__ if more important than __str__ because it shows
    how the object needs to be created, with one example
    """

    def __init__(self, x, y, z = "String") -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        """Simple representation of the object. It overrides the __repr__"""
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        """To communicates with other developers, how the object needs to be created."""

        # The next lines of class_name do the same thing
        class_name = type(self).__name__
        class_name = self.__class__.__name__

        # return f'{class_name}(x={self.x}, y={self.y}, z={self.z})'
        # !r to show the representation ('String' != String)        
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinates(new_x, new_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other

p1 = Coordinates(1,1)
p2 = Coordinates(2,2)

#__str__ of p1
# print(str(p1))
# print(p1.__str__())
# print(f'{p1!s}')

#__repr__ of p2
# print(repr(p2))
# print(p2.__repr__())
# print(f'{p2!r}')

# using __add__
p3 = p1 + p2

print(p3)
print(f'P1 > P2: {p1 > p2}.')
print(f'P2 > P1: {p2 > p1}.')
