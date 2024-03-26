"""
Banking System

Putuguese description to be fast.

Criar classes para banco, contas, pessoa e clientes.
- Cliente tem conta (corrente ou poupança);
- Contas tem método para saquee depósito;
- Conta corrente possui limite extra, poupança não;
"""
from abc import ABC

class Account(ABC):
    def __init__(self, agency, acc_number, amount, limit = 0) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._amount = amount
        self._limit = limit

    @property
    def account(self):
        return f'{self._acc_number}-{self._agency}'

    def show_balance(self):
        print(f'Your balance is: R$ {self._amount}.')

    def deposit(self, amount):
        if amount > 0:
            self._amount += amount
            self.show_balance()
            return True
        print('Amount need to be greater than 0.')
        return False

    def withdraw(self, amount):
        raise NotImplementedError('You should implement this method!')

    def __str__(self) -> str:
        return self.account

class SavingsAccount(Account):
    def __init__(self, agency, acc_number, amount = 0, limit = 0) -> None:
        super().__init__(agency, acc_number, amount, limit)

    def withdraw(self, amount):
        if self._amount >= amount:
            self._amount -= amount
            self.show_balance()
            return True
        print('Not enought money.')
        return False

class CurrentAccount(Account):
    def __init__(self, agency, acc_number, amount = 0, limit = 100) -> None:
        super().__init__(agency, acc_number, amount, limit)
        self._limit = limit

    def withdraw(self, amount):
        if self._amount + self._limit >= amount:
            self._amount -= amount
            self.show_balance()
            return True
        print('Not enought money.')
        return False

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._account = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    def __str__(self) -> str:
        return f'({self.name} - {self._account if self._account else "Not defined"})'

class Bank:
    def __init__(self, name, account, client) -> None:
        self._name = name
        self._account = account
        self._client = client

    def withdraw(self, amount):
        if self._account == self._client.account:
            self._client.account.withdraw(amount)
            return True
        print('This client isn\'t the account owner.')
        return False

    def deposit(self, amount):
        if self._account == self._client.account:
            self._client.account.deposit(amount)
            return True
        print('This client isn\'t the account owner.')
        return False

    def __str__(self):
        return self._name


###################
# CREATING ACCOUNTS
###################

acc1 = SavingsAccount(500, 14111)
# acc1.deposit(1000)
# acc1.withdraw(200)

acc2 = CurrentAccount(100, 14111)
# acc2.deposit(1000)
# acc2.withdraw(1200)

#################
# CREATING CLIENT
#################

fabio = Client('Fábio', 25)
fabio.account = acc2

###############
# CREATING BANK
###############

bank1 = Bank('Star Bank', acc2, fabio)
bank1.deposit(100)
bank1.withdraw(205)
