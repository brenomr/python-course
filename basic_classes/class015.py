# USING WHILE/ELSE
# Classes 039, 040, 041, 042

"""
Annotations:
The ELSE statement will be reached once WHILE finishes
without a break, based on the condition passed to it
"""

##############################
# Iterating string with WHILE
##############################

# iterable_word = 'MarianaPeixoto'
# new_word = '-'
# i = 0

# while i < len(iterable_word):
#     if iterable_word[i] == ' ':
#         print(f'Breaking WHILE. The new word before a space: {new_word}')
#         break
    
#     new_word += f'{iterable_word[i]}-'
#     i += 1
# else:
#     print(f"WHILE statement finished, the new word is: {new_word}")

##############################
# Exercise
##############################

# Make a program using WHILE statement to show which letter
# has the greatest amount on a given phrase

phrase = 'O Python é uma linguagem de programação, '\
    'multiparadigma. Foi criado por Guido van Rossum. '\
    'Repeated letters for test: zzzzzzzzzzzzzzzzzz'

i = 0
letter_repeated = []
letter_list = []
letter_count = 0
phrase = phrase.replace(' ', '')

try:
    while i < len(phrase):
        if i == 0:
            letter_repeated.append(phrase[i])
            letter_count = phrase.count(phrase[i])
            letter_list.append(phrase[i])
            i += 1
        else:
            current_letter = phrase[i]

            # This IF its for performance, avoiding run multiples unnecessary .count() on letter already in the list
            if current_letter not in letter_list:
                letter_list.append(current_letter)
                current_letter_count = phrase.count(current_letter)
                
                if current_letter_count > letter_count:
                    letter_repeated = [current_letter]
                    letter_count = current_letter_count
                elif current_letter_count == letter_count:
                    letter_repeated.append(current_letter)
            i += 1
    print(f"The letter{'s' if len(letter_repeated) > 1 else ''} {letter_repeated} is repeated {letter_count} times.")
except Exception as err:
    print(err)