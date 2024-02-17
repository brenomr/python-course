"""
Counting letters in a word.

Based on a discuss in this vídeo:
https://www.youtube.com/watch?v=PHQGBrzhSIg
"""

letters = {}
stored_letter = { 'letter': '', 'count': 0 }

word = input('Insert a word: ')

for letter in word:
    if not letters.get(letter):
        letters[letter] = 1
    else:
        letters[letter] += 1

for letter in letters:
    if letters.get(letter) > stored_letter['count']:
        stored_letter = { 'letter': letter, 'count': letters.get(letter) }

print(f'The letter that is repeated most often is ({stored_letter.get("letter")}), it repeats ({stored_letter.get("count")}) times.')
print(f'The rank of all letters in general is: {letters}.')

# Obs. Theres an issue where if two letters are repeated the same amount of times, the last one will be printed.

# -----------------------------------
# Same solution, a little bit verbose
# -----------------------------------

# letters = {}
# letter_stored = None
# letter_count = 0

# word = input('Insert a word: ')

# for letter in word:
#     if not letters.get(letter):
#         letters[letter] = 1
#     else:
#         letters[letter] += 1

# for letter in letters:
#     if letters.get(letter) > letter_count:
#         letter_count = letters.get(letter)
#         letter_stored = letter

# print(f'The letter ({letter_stored}) repeats ({letter_count}) times.')
