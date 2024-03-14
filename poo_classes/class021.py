"""
Functions decorators for classes

Doing the same as decorator @add_repr:
Team = add_repr(Team)
Planet = add_repr(Planet)
"""

def add_repr(cls):
    def my_repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'({class_name}, {class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

@add_repr
class Team:
    def __init__(self, name) -> None:
        self.name = name

@add_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name

brazil = Team('Brazil')
england = Team('England')

earth = Planet('Earth')
jupter = Planet('Jupter')

print(brazil)
print(england)
print(earth)
print(jupter)
