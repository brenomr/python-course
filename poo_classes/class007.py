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

        # By convention attributes starting with one
        # or two underlines are private / protected

        # Setting att directly when creating an instance
        self._color_att_changed = color

        # Setting attributre by using the setter method
        # self.color = color

    # With property the method acts like an attribute
    @property
    def color(self):
        print(f'Color accessed directly by client: {self._color_att_changed}.')
        return self._color_att_changed
    
    # color is the name of 'attribute' expose to client
    @color.setter
    def color(self, new_color):
        print(f'Color changed directly by client to: {new_color}.')
        self._color_att_changed = new_color

pen1 = Pen('Blue')
color = pen1.color
pen1.color = 'Black'
