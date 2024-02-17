"""
Creating and managing files with method open()

---------------------
Modes to open a file:
---------------------
r (to read)
w (to write)
x (to create)
a (to add)
b (binary)
+ (read and write)

-------------------------
Context manager ('with'):
-------------------------

with open('file.txt', 'w') as file:
    file.write('Hello, world!')

In this example the file will be closed
automatically after the block.

-------------------------
Methods to manage files:
-------------------------
Will be added on next classes

"""

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

with open(file_path, 'w') as file:
    print('A file was created and closed on path:')
    print(file_path)
