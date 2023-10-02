# SET() METHOD
"""
Annotations:
- set() is like list() and dict()
- Values are unique
- Don't have indexes
- No guaranteed ordering
- Doesn't accept mutable values
- Is iterable (for, in)
- Useful methods: add, update, clear and discard
- Useful operators: union, intersection, difference
"""

# create a iterable set with a mutable string
# s1 = set('John')

# Values are unique
# s1 = { 1,2,3,3,3,4,5,6,7,8,7,9,7,1,2,3,10 }
# parsed_phrase = set('This is a regular phrase to be used with the method set.')


# Convertion: No guarantee ordering. Only mutable values, and
# if a mutable object is given a TypeError will be raised
l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'j', 'b']
s2 = set(l1)
l2 = list(s2)

s2.add('Name')
s2.update('John')
s2.discard('Name')
s2.clear()

# Operators
r1 = {1, 2, 3}
r2 = {2, 3, 4}

# Union (|)
r3 = r1 | r2

# Intersection (&)
r4 = r1 & r2

# Difference - shows the values present only on the left side
r5 = r1 - r2
r6 = r2 - r1

# Symmetric Difference - shows the different values from both sides
r7 = r1 ^ r2

###############################
# Case of use of set()
###############################

letters = set()

while True:
    letter = input('Insert a letter: ')
    letters.add(letter.lower())

    if 'x' in letters:
        print('Secret letter found.')
        print(f'Typed letters: {letters}')
        break
