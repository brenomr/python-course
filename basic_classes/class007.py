# VARS, PEP8
# Using vars, some explanations about PEP8 Style Guide --> https://peps.python.org/pep-0008/

name = 'John Doe'
age = 13 + 22

print(name, age)
print(f'{name} is {age} year{"s" if age > 1 else ""} old.')