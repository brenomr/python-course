"""
This is the documentation for the module.

With this module you can do the following:
- Test the docstrings module in main.
- See the docstrings of the module and its functions.

PEP8 recommends using triple double quotes for docstrings.
"""

general_variable01 = 10

def custom_sum(a: int | float, b: int | float) -> int | float:
    """
    Custom sum (a, b)

    This function receives two numbers (a, b) and returns the sum of them.

    Arguments:
        a (int | float): The first number, can be integer or float.
        b (int | float): The second number, can be integer or float.

    Returns:
        int | float: The sum of the two numbers, can be integer or float.
    """
    return a + b

general_variable02 = 11
general_variable03 = 13
general_variable04 = 19

class Planes:
    """
    Planes

    Simple example class to describe a plane and allow the creation of docstring
    to compare with the docstrings from the rest of the module.
    """
    def __init__(self, name: str, model: str) -> None:
        self.name = name
        self.model = model
        self.flying = False

    def fly(self) -> bool:
        """
        Fly

        This method changes the flying attribute to True.

        Returns:
            bool: True if the plane is flying, False otherwise.
        """
        if not self.flying:
            self.flying = True
        return self.flying

if __name__ == '__main__':
    print('This is the docstrings module.')
