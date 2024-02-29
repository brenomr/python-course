"""
Class summary (revision)
- Method - Have access to the SELF instance, can execute instance functions (methods)
- Classmethod - Have access to the class, can return pre-defined instances
- Staticmethod - Can't access anything, it's just a regular function
"""

class Connection:

    def __init__(self, host: str ='localhost') -> None:
        self.host = host
        self.username = None
        self.password = None

    def set_username(self, username: str):
        self.username = username
    
    def set_password(self, password: str):
        self.password = password
    

    @classmethod
    def create_with_auth(cls, username, password):
        user = cls()
        user.set_username(username) # or user.set_username('Default username')
        user.set_password(password) # or user.set_password('Default password')
        return user
    
    @staticmethod
    def say_hello():
        print('Hello!')

user_base = Connection.create_with_auth('Paula', 'senhaforte123456') # or Connection.create_with_auth()
user_base.say_hello()
print(user_base.__dict__)