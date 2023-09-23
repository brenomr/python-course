# ROUND, SPLIT, JOIN, STRIP, TERNARY
# Classes 055, 056, 057


#######################
# ROUND
#######################

# Dealing with float imprecision using round

import decimal, os

# Just need to import "this" in order to show Zen of Python
# import this

num_a = 0.1
num_b = 0.7
sum_numbs = num_a + num_b

num_c = decimal.Decimal('0.1')
num_d = decimal.Decimal('0.7')
sum_decs = num_c + num_d

# Expected 0.8, but will returns 0.7999999...
# print(sum_numbs)
# print(round(sum_numbs, 3))
# print(sum_decs)

#######################
# SPLIT JOIN STRIP
#######################

# strip to remove spaces from start and end of a string
# lstrip remove space from left and rstrip from right

base_phrase = 'Lets split strings, and then join everything...'
word_list = base_phrase.split(', ')

# getting index and phrase from a list
# for index, phrase in enumerate(word_list):
#     print(phrase)
#     print(word_list[index])

# print(word_list)
# print(' '.join(word_list))

#########
# TERNARY
#########

os.system('clear')
cpf = input('Inser your CPF (just numbers): ')
valid_cpf = len(cpf) == 11
print(f'You have {"a valid" if valid_cpf else "an invalid"} cpf.')