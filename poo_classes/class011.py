"""
Composition is a type of association that represents a "whole" relationship.

One object depends on another, if one object is erase the other is also erased.
"""

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.addresses = list()
    
    def insert_address(self, street, number):
        self.addresses.append(Address(street, number))
    
    def show_address(self):
        return self.addresses
    
    # to show the object being removed when the program finishes
    def __del__(self):
        print('REMOVING:', self.name)

class Address:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number
    
    def __str__(self) -> str:
        return f'({self.street}, {self.number})'
    
    # to show the object being removed when user is removed
    def __del__(self):
        print('REMOVING:', self.street, self.number)


cintia = User('Cintia')
cintia.insert_address('Boulervar Street', 522)
cintia.insert_address('Boulervar Street', 222)
print(*cintia.show_address(), sep='\n')

# to test the objects being removed before the program finishes, if 
# enabled, the removing calls will be shown before the 'end of program'
# del cintia

print('End of program...')
