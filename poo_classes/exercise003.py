"""
Banking System

Putuguese description to be fast.

Criar classes para banco, contas, pessoa e clientes.
- Cliente tem conta (corrente ou poupança);
- Contas tem método para saquee depósito;
- Conta corrente possui limite extra, poupança não;
"""
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, acc_number: int, amount: float) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._amount = amount

    @property
    def account(self) -> str:
        return f'{self._acc_number}-{self._agency}'

    def show_balance(self) -> None:
        print(f'Your balance is: R$ {self._amount:.2f}.')

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._amount += amount
            self.show_balance()
            return True
        print('Amount need to be greater than 0.')
        return False

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        ...

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._agency!r}, {self._acc_number!r}, {self._amount!r})'
        return f'{class_name}{attrs}'


class SavingsAccount(Account):
    def withdraw(self, amount: float) -> bool:
        if self._amount >= amount:
            self._amount -= amount
            self.show_balance()
            return True
        print('Not enought money.')
        return False


class CurrentAccount(Account):
    def __init__(self, agency: int, acc_number: int, amount: float, limit: int = 100) -> None:
        super().__init__(agency, acc_number, amount)
        self._limit = limit

    def withdraw(self, amount: float) -> bool:
        if self._amount + self._limit >= amount:
            self._amount -= amount
            self.show_balance()
            return True
        print('Not enought money.')
        return False

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._agency!r}, {self._acc_number!r}, {self._amount!r}, '\
            f'{self._limit!r})'
        return f'{class_name}{attrs}'


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: Account | None = None

    @property
    def account(self) -> Account | None:
        return self._account

    @account.setter
    def account(self, account: Account) -> None:
        self._account = account

    def __str__(self) -> str:
        return f'({self.name} - {self.account if self.account else "Not defined"})'


class Bank:
    def __init__(self, name: str, account: Account, client: Client) -> None:
        self._name = name
        self._account = account
        self._client = client

    def withdraw(self, amount: float) -> bool:
        if self._account == self._client.account:
            self._client.account.withdraw(amount)
            return True
        print('This client isn\'t the account owner.')
        return False

    def deposit(self, amount: float) -> bool:
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

acc1 = SavingsAccount(500, 14111, 100)
# acc1.deposit(1000)
# acc1.withdraw(200)

acc2 = CurrentAccount(100, 14111, 200)
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
