"""
Encapsulation - Process of restricting access to certain parts of an object.

In other programming languages we can have: public, protected and private.

In Python there are no strict modificators, but by convention, the protected
attributes are defined with a single underscore and the private with a double
underscore.

Summary:
- Public: public
- Protected: class, subclasses
- Private: class
"""

class Bar():

    def __init__(self) -> None:
        self.public = "Public: can be accessed anywhere"
        self._protected = "Protected: can be accessed in the class or subclasses"
        self.__private = "Private: can be accessed only in the class"
    
    def method_public(self):
        return "This is public"
    
    def _method_protected(self):
        return "This is protected"
    
    def __method_private(self):
        return "This is private"

bar_example = Bar()

# Wrong
# print(bar_example._protected)
# print(bar_example._method_protected())
# print(bar_example.__private)
# print(bar_example._Bar__method_private())