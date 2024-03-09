"""
Class Polymorphism

Multiple classes that inherit from a same parent class and
have the same method, but with different implementations

Method signature is method name, parameters, parameters
type and return type. (method return type isn't an academic
definition)

Log, LogPrintMixin and LogFileMixin from class014 have the
necessary base for the polymorphism.

SOLID:
S - Single Responsibility Principle
O - Open/Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send_notification(self) -> bool:
        pass


class EmailNotification(Notification):
    def send_notification(self) -> bool:
        print(f'Sending email: {self.msg}')
        return True

class SMSNotification(Notification):
    def send_notification(self) -> bool:
        print(f'Sending SMS: {self.msg}')
        return True

def notify(notification: Notification):
    result = notification.send_notification()

    if result:
        print('Notification sent successfully')
    else:
        print('Failed to send notification')

sms = SMSNotification('John you have been invite to the party!')
email = EmailNotification('meet at 5, dont be late.')

# Polymorphism occurring here, the objects are different, but
# have the same type (Notification), using the same method, but
# behaving differently.
notify(sms)
notify(email)
