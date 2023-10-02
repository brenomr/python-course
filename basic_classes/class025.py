# DICT with some methods
# Classes 075, 076 (pt-01), 077, 078
# Like LIST, DICTIONARY is mutable

person = {
    'name': 'Lorenzo',
    'surname': 'Santos',
    'age': 45,
    'height': 1.76,
    'weight': 78,
    'addresses': [
        {
            'address_type': 'Home',
            'street': 'Avenida Paulista',
            'number': 455,
            'City': 'São Paulo',
            'UF': 'São Paulo'
        }, {
            'address_type': 'Work',
            'street': 'Avenida Conceição',
            'number': 780,
            'City': 'Indaiatuba',
            'UF': 'São Paulo'
        }
    ]
}

# print(person, type(person))

# Getiting a property with .get(), if nothing found return 'Nothing' (empty == None)
# get() is a better way to work with DICT instead [ ]
# print(person.get('addresses', 'Nothing...'))
# print(person['name'])

person_adresses = person.get('addresses')

# if person_adresses:
#     for address in person_adresses:
        # print(address)

# for key in person:
#     print(key)

# add new attribute
person['car'] = 'Ford Focus'
key_name = 'CPF'
person[key_name] = '221.222.123-09'

# delete attribute
del person['car']

# print(person)
