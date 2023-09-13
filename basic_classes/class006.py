# DATA CONVERTION

"""
Annotations:
Python is a language strongly typed it can't simply change from one type to another
Topics: type convertion, typecasting, coercion
"""

# Converting string to int
numeric_text = '245'
print(type(numeric_text))
print(type(int(numeric_text)), end='\n'+'-'*10+'\n')

# Converting string in boolean
print(type(bool('')))
print(type(bool('some text')), end='\n'+'-'*10+'\n')

# String
print('abo' + 'bora', end='\n'+'-'*10+'\n')

# Number (int, float)
print(10 + 2)
print(10.5 + 1.5, end='\n'+'-'*10+'\n')

# Boolean
print('ada' == 'ada')
print(10 != 11, end='\n'+'-'*10+'\n')

# Forcing an error, because of different types
print('1' + 1)