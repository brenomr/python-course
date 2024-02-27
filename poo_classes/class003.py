"""
Class attribute

We can define an attribute to the class.

Be warned, the attribute can be changed externally or be
override if another attribute with the same name be defined
on the __init__
"""

class Person:
    current_year = 2024

    def __init__(self, name, birthday_year) -> None:
        self.name = name
        self.birthday_year = birthday_year
        # current year being override here
        self.current_year = 1800 
    
    def get_age(self):
        # Person.current_year to avoid the self.current_year
        print(f'Person year: {Person.current_year}. Person self year: {self.current_year}.')
        print(f'You have: {Person.current_year - self.birthday_year} years.')

fernando = Person('Fernando', 1995)
# fernando.get_age()

"""
Uses of __dict__ and vars in instances attributes

We can use __dict__ and vars to access the attributes of an instance
"""

print(fernando.__dict__)
print(vars(fernando))
fernando.__dict__['current_year'] = 2000
print(fernando.__dict__)
print(vars(fernando))

del fernando.__dict__['name']
print(vars(fernando))

daniel = {'name': 'Daniel San', 'birthday_year': 1990}

daniel_san = Person(**daniel)
print(daniel_san.__dict__)