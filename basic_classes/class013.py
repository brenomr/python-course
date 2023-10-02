# TRY/EXCEPT BASIC USES, BUILT-IN TYPES AND LOOP WITH WHILE
# https://docs.python.org/3/library/stdtypes.html
# Classes 030, 031, 032 and 033, 034, 035, 036, 037, 038

########################
# TRY/EXCEPT
########################

# try:
#     number = input('Enter a number: ')
#     number = float(number)

#     print(f'Your number multiplied by 2 is: {number*2}')
# except Exception as err:
#     print(err)

########################
# LOOP WITH WHILE
########################
# With the 'continue' declaration we can skip the rest of the 'while' on a specific loop
# Some operators to use with 'while': +=, -=, *=, /=, //=, **= %=

# Regular count iterator
count = 10
while count >= 1:
    count -= 2
    
    if count == 4:
        print(f'Skip COUNT: {count}')
        continue

    print(f'COUNT: {count}')


# Using multiple 'while's

qtt_lines = 4
qtt_col = 3
line = 1

while line <= qtt_lines:
    col = 1
    print(f'LINE {str(line).zfill(2)}: ', end='')

    while col <= qtt_col:
        print(f'COLUMN: {str(col).zfill(2)}', end=' | ')
        col += 1
    
    print('')
    line += 1

# while True:
#     text = input('Enter a text: ')
#     print(f'Your text in uppercase: {text.upper()}')

#     keep_running = input('Do you want to continue? [Y]es: ')

#     if keep_running != 'Y' and keep_running != 'y':
#         break
