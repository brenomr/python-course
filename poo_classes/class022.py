"""
Methods decorator 
"""

def is_my_home(method_show_name):
    def show_phrase(self):
        planet_name = method_show_name(self)
        planet_name = planet_name.capitalize()
        if planet_name.lower() in ['earh', 'terra']:
            return f'The planet {planet_name} is my home.'
        return f'The planet {planet_name} is not my home.'
    return show_phrase


class Planet:
    def __init__(self, name) -> None:
        self.name = name

    @is_my_home
    def show_name(self) -> str:
        return self.name


jupter = Planet('Jupter')
terra = Planet('TERRA')

print(jupter.show_name())
print(terra.show_name())
