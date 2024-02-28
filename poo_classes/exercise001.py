"""
Save the data from your class to JSON
Initiate new classes based on your JSON file
Save each class in a new JSON file
"""
import os
import json

current_path = os.path.dirname(os.path.realpath(__file__))

class Person:

    def __init__(self, name, last_name, age, address ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = str(age)
        self.address = address
    
    def save_person_file(self, dir_not_created=True):
        self.dir_not_created = dir_not_created

        data_to_save = self.__dict__
        dir_path = f'{current_path}/data'
        path = f'{dir_path}/{self.name}.json'

        try:
            with open(path, 'w', encoding='utf8') as file:
                json.dump(obj=data_to_save, fp=file, indent=2, ensure_ascii=False)
            print(f'The file was saved at: {path}')
        except Exception as e:
            if isinstance(e, FileNotFoundError) and self.dir_not_created:
                print('Creating directory for the new file...')
                os.mkdir(dir_path)
                self.save_person_file(dir_not_created=False)
    
    def open_person_file(self):
        path = f'{current_path}/data/{self.name}.json'
        try:
            with open(path, 'r', encoding='utf8') as file:
                opened_file = json.load(file)
                print(opened_file)
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                self.save_person_file()
            else:
                print(e)
    
    def __str__(self) -> str:
        return self.name

Fernando = Person(name='Fernando', last_name='Amaral', age=25, address='Boulevart Street, 25')
Adalberto = Person(name='Adalberto', last_name='Antunes', age=34, address='Boulevart Street, 475')
Adriana = Person(name='Adriana', last_name='Souza', age=29, address='Ammy Street, 1235')

# Fernando.save_person_file()
# fernando.open_person_file()

pl = [Fernando.__dict__, Adalberto.__dict__, vars(Adriana)]

def create_people_json(people_list, file_path):

    fp = f'{file_path}/data/people_list.json'

    with open(fp, 'w', encoding='utf8') as file:
        json.dump(obj=people_list, fp=file, ensure_ascii=False, indent=2)
    print(f'People list saved at: {fp}')

if __name__ == '__main__':
    create_people_json(people_list=pl, file_path=current_path)
