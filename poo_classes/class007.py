"""
Class getters and setters

Getter - to get an attribute
Setter - to set an attribute

To avoid problems, we can define getters,
and protect the class attribute from being
accessed directly by the client's code.

But the 'Pythonic' way @property allow us to
make the method acts like an attribute, and
with this feature we can change our attributes,
even if the client is already made use of it,
without break the code.
"""

class Pen:

    def __init__(self, color) -> None:
        self.color_attribute_changed = color

    # This one will need a setter property to use self.color (next class)    
    # def set_color(self, color):
    #     self.color = color
    
    def get_color(self):
        return self.color
    
    # With property the method acts like an attribute
    @property
    def color(self):
        return self.color_attribute_changed

pen1 = Pen('Blue')

# The code won't break with the color attribute changed
print(pen1.color)
print(pen1.get_color())

# This one will need a setter property (next class)
# print(pen1.set_color('Black'))
