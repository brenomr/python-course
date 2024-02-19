"""
Creating and managing files with method open()

---------------------
Modes to open a file:
---------------------
r (to read)
w (to write, it will always overwrite the file)
x (to create)
a (to add, it will add (append) new lines to the file)
b (binary)
+ (read and write)
encoding (to specify the encoding, e.g: utf-8)

-------------------------
Context manager ('with'):
-------------------------

with open('file.txt', 'w') as file:
    file.write('Hello, world!')

In this example the file will be closed
automatically after the block.

-------------------------
Usefull methods to manage files:
-------------------------
write() and read() (self explanatory)
writelines() (write a list of strings)
seek() (move the cursor)
readline() (read a line)
readlines() (read all lines)
os.remove or os.unlink (to remove a file)
os.rename (to rename a file)


"""

import os

path = '/home/rodrigues/Documents/Projects/python-course/basic_classes/data'
file_name = 'class042.txt'
file_path = f'{path}/{file_name}'

# to write a file
# file = open(file_path, 'w')

# to close a file
# file.close()

# if a file can be opened (or writed) than it can be closed,
# so we can use 'with' to open a file and it will be closed
# automatically, like commented on the steps above

# Writing on a file (create if not exists)
# with open(file_path, 'w') as file:
#     print('Writing a file...')
#     file.write('Hello, world!\n')
#     file.write('This is a test\n')

#     # we can use list or tuple to write multiple lines
#     file.writelines(
#         ['This is a test\n', 'With more than one line\n', 'Check this out!\n']
#     )

with open(file_path, 'a', encoding='utf8') as file:
    file.write('Add new line 1\n')
    file.write('Add new line 2\n')

# Reading a file (.read() will not work on open with 'w' mode)
with open(file_path, 'r') as file:
    print('Reading a file...')
    print('-'*17,'\n')
    print(file.read())

    # Returning to the start of the file
    # file.seek(0,0)

    # Reading one line at time

    # print('Line 1:')
    # print(file.readline(), end='')
    # print('Line 2:')
    # print(file.readline().strip())

    # print('Reading all lines:')
    # for line in file:
    #     print(line.strip())

# to remove a file
# os.remove(file_path)
# os.unlink(file_path)

# to rename a file
os.rename(file_path, f'{path}/class042_renamed.txt')
