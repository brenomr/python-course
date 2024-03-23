"""
Using enums
"""
import enum

# use case
def move(direction):
    if direction not in ['left', 'right', 'up', 'down']:
        raise ValueError(f'Invalid direction: {direction}.')
    print(f'Moving to: {direction}.')

# use case with enum
Directions = enum.Enum('Directions', ['LEFT', 'RIGHT', 'UP', 'DOWN'])

def move2(direction):
    if not isinstance(direction, Directions):
        raise ValueError(f'Invalid direction: {direction}.')
    print(f'Moving to: {direction}.')


# use case with class (type)

class Directions2(enum.Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

def move3(direction: Directions2):
    if not isinstance(direction, Directions2):
        raise ValueError(f'Invalid direction: {direction}.')
    print(f'Moving to: {direction.name}.')

move3(Directions2.LEFT)
