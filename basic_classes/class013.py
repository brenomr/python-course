# USING INDEX, SLICE AND LEN()
# Classes 027 and 028

"""
Annotations:
Slicing string: [s:e:sp]
s = start | e = end (limit) | sp = spaces (how many characters will be passed through, default == 1)
Get by index: 'word'[0]
"""

# text = 'hello world'

# Get by index
# print(text[0])

# Get by index with range (slice)
# print(text[1:5])

# Nothing == 0, same as text[0:5]
# print(text[:5])

# From 0 to 10 (11 from len is the limit), 'jumping' 2 characters
# print(text[0:len(text):2])

# Reverse selection
# print(text[::-1])

# print(len(text))

# Exercise
# Ask for user name and age, check if both fields 

name = input('Insert your name: ')
age = input('Insert your age: ')

if name.strip() and age:
    print(f"""
            Your name is {name}.
            Your inverted name is: {name[::-1]}.
            Your name has{"" if " " in name else " no"} spaces.
            Your name contains {len(name.replace(" ", ""))} letters without spaces.
            The first letter of your name is {name.strip()[0]}.
            The last letter of your entire name is {name[-1]}.
    """)
else:
    print('You need to insert name and age.')