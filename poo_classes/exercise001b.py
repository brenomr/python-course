import json
from exercise001 import current_path, Person

def convert_list_to_person_class(person):
    file_path = f'{current_path}/data/people_list.json'

    with open(file_path, 'r', encoding='utf8') as file:
        people_list = json.load(file)

        people_class_list = [Person(**person) for person in people_list]

        for person in people_class_list:
            print(person.__dict__)


if __name__ == '__main__':
    convert_list_to_person_class('test')
