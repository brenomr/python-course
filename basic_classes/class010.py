# Basic uses of strings and numbers. Formatting strings and using hexadecimal

"""
Annotations:
Classes 010, 011, 012, 013 and 025
Calculus Precedence:
    1) (n + n)
    2) **
    3) * / // %
    4) + -
Symbols to use with % format:
    s - string
    d and i - int
    f - float
    x and X - hexadecimal (0123456789ABCDEF)
"""

####################
# Concatenating
####################

# concat_name = "John " + "Doe"
# print(concat_name)

####################
# Repeating terms
####################

# repeated_words = "Some words... " * 3
# print(repeated_words)

####################
# Exercise
####################

# Params
name = "John Doe"
height = 1.65
weigth = 67
imc = round((weigth / (height)**2), 2)
imc_result = "normal."

# Checking IMC and returning message
# if(imc < 18.5):
#     imc_result = "below normal."
# elif(imc > 24.99):
#     imc_result = "above normal."
# print(f'{name} based on your height: {height} and your weigth: {weigth} your IMC is {imc}, meaning your weigh is: {imc_result}')

####################
# Formatting strings with f strings
####################

# text1 = f'Your name is {name}.'
# print(text1)

####################
# Formatting strings with format method (obsolete)
####################

# text2 = 'Your name is {name}'.format(name = "Richarlisson")
# print(text2)

# text3 = 'Your name is {name} and your weigth is: {weigth:.2f}'
# print(text3.format(name="Rolland", weigth=46.775))

# text4 = 'Your name is {} and your weigth is: {:.2f}'
# print(text4.format("Rolland", 46.775))

# Adding characters or spaces with strings, this
# will complete the word with the size given

# word = "avocado"
# print(f'This is an {word:!>10}.')
# print(f'This is an {word:x^10}.')

####################
# Formatting strings with % (obsolete)
####################

# text5 = '%s your heigh is 1.85' % name
# print(text5)

# text6 = '%s your high is %.2f' % (name, height)
# print(text6)

####################
# Hexadecimal
####################

# text_hex01 = 'Showing two numbers %i and %x' % (13, 13)
# print(text_hex01)

# text_hex02 = 'Showing two numbers %i and %04X' % (1200, 1200)
# print(text_hex02)
