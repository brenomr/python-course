# Exercise 001, using vars

name = 'John'
surname = 'Doe'
birthday_year = 2010
current_year = 2023
age = current_year - birthday_year
height = 1.55

print('Name:', name)
print('Surname:', surname)
print('Age:', age)
print('Birthday Year:', birthday_year)
print(f'Legal age? {"Yes." if age > 17 else "No."}')
print('Height in meters:', height)