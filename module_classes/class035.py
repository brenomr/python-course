"""
Using OS module - part 01
The OS module allow python to interact with the operating system.

Some functions:
os.path - To work with paths.
os.path.exists - To check if a path exists.
os.listdir - To list directories.
os.system - To run shell commands.
os.path.join - To join paths.
os.path.walk - To walk through directories recursively.

https://docs.python.org/3/library/os.html
"""

import os

# Send shell command to clear the terminal
os.system('clear')
print('*' * 40)

# Using shell to show message with echo
os.system('echo "Hello World from shell!"')
print('*' * 40)

# Creating path
custom_path = os.path.join('home', 'user', 'someuser', 'file.txt')
print(custom_path)

# Splitting path
directory_path, file_name = os.path.split(custom_path)
print(directory_path)

# Splitting file name and extension
file_name, file_extension = os.path.splitext(file_name)

print(file_name)
print(file_extension)

# Checking if path exists
print(os.path.exists(custom_path))
print(os.path.exists('/home/'))

# Return the absolute path
abs_file_path = os.path.abspath('file.txt')
print(os.path.exists(abs_file_path))

# Show the current working directory (final path)
print(os.path.basename(custom_path))

# Show the name of directories in the path
print(os.path.dirname(custom_path))

# Remove this in order to see the above output
os.system('clear')

real_path_to_project = os.path.realpath('./')

# List everything in the current directory
# print(os.listdir(real_path_to_project))

# Listing files and directories
# for fol in os.listdir(real_path_to_project):
#     if os.path.isdir(fol):
#         if fol in ['module_classes', 'basic_classes']:
#             for item in os.listdir(fol):
#                 print(item)

real_path_to_module = os.path.realpath('./module_classes')

# Root = main directory, dirs = directories, files = files (if any
for root, dirs, files in os.walk(real_path_to_module):
    print(root)
    for file in files:
        print(file)
