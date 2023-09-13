# Basic uses of strings and numbers. Formatting strings

"""
Annotations:
Classes 010, 011, 012 and 13
Calculus Precedence:
    1) (n + n)
    2) **
    3) * / // %
    4) + -
"""

concatenate_name = "John" + " " + "Doe"
print(concatenate_name)

repeated_words = "Some words... " * 3
print(repeated_words)

account_result_1 = 1 + 2 ** 3 + 2
print(account_result_1)


# Exercise

name = "John Doe"
hight = 1.65
weigth = 67
imc = round((weigth / (hight)**2), 2)
imc_result = "normal."

if(imc < 18.5):
    imc_result = "below normal."
elif(imc > 24.99):
    imc_result = "above normal."

print(f'{name} based on your hight: {hight} and your weigth: {weigth} your IMC is {imc}, meaning your weigh is: {imc_result}')


# Formatting strings with f strings
text1 = f'Your name is {name}.'

# Formatting strings with format method (obsolete)
text2 = 'Your name is {name}'.format(name = "Richarlisson")
text3 = 'Your name is {name} and your weigth is: {weigth:.2f}'
text4 = 'Your name is {} and your weigth is: {:.2f}'

# Formatting strings with #

print(text1)
print(text2)
print(text3.format(name="Rolland", weigth=46.775))
print(text4.format("Rolland", 46.775))