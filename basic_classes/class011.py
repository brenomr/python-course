# INPUT() METHOD, IF, ELSE AND ELIF
# Classes 014, 015, 016, 017, 018,
# 019, 020, 021, 022, 023 and 024

"""
Annotations:

Operator    Meaning             E.G.
>           greater than        5 > 3
>=          greater/equal       5 >=
<           less than           3 < 66
<=          less/equal          6 <= 20
==          equal               5 == 5
!=          different           12 != 7
and         all condit. true    True and True == True
or          at least one cond.  True or False == True
not         for false condit.   not False == True
"""
#################################
# simple input data
#################################
#
# while True:
#     name = input("Enter your name: ").strip()
#
#     if(len(name) == 0 or name == ' '):
#         print("You must enter at least one letter.")
#     else:
#         print(f'Your name is: {name}')
#         break

#################################
# input data with 3 tries
#################################
#
# count = 3
# while True:
#     option = input("Do you want to login? (yes or no): ").strip().lower()
#     if(option == 'yes'):
#         print("Login...")
#         break
#     elif(option == 'no'):
#         print("Closing terminal...")
#         break
#     else:
#         if count > 1:
#             print("You need to enter a valid option!")
#             count -= 1
#             print(f"Tries until process be terminate: {count}")
#         else:
#             print("Process terminated...")
#             break

#################################
# Testing logic operators:
#################################

# login = input('Login? [Y]es | [N]o ').lower()
# password = input('Insert your password: ')
# base_password = '123456'

# if login == 'y' and password == base_password:
#     print('Welcome! \n You are logged in!')
# else:
#     print('Exiting...')

# print(True and True, end="\n"+"-"*10+"\n")
# print(True and False, end="\n"+"-"*10+"\n")
# print(True or False, end="\n"+"-"*10+"\n")
# print(False or False, end="\n"+"-"*10+"\n")
# print(True and (False or True), end="\n"+"-"*10+"\n")

"""
Using AND the values will be checked until
a False be found, if not find a False the
last value True will be shown
"""
# print('1' and 0 and 'Tree')

"""
Using OR the values will be checked until
a True be found, if not find a True the last
value False will be shown
"""
# print(0 or False or 'word' or True)

# NOT invert the logic value
# print(not True and True)
# print(not 0 and True)

# IN return True if the value exists
# fruits = ['orange', 'lime', 'grape']
# print('avocado' in fruits)
# print(50 in [1,2,4,50])
# print('b' not in 'avocado')
# print('v' in 'avocado')

word = input('Enter any word: ')
find = input ('What do you want to find in the given word? ')

if find in word:
    print(f'{find} was found in the {word}.')
else:
    print(f"{find} wasn't found in {word}.")    