"""
Class multiple inheritance

Always prefer to use composition
instead multiple inheritance, to
avoid a much comples code.

On Smartphone we are goint to use
multiple inheritance to illustrate
"""

from datetime import datetime
from log import LogPrintMixin

now = datetime.now()
current_time = now.strftime('%H:%M:%S')

class Electronic:
    def __init__(self, name) -> None:
        self._name = name
        self._turned_on = False
    
    def turn_on(self):
        if not self._turned_on:
            self._turned_on = True
    
    def turn_off(self):
        if self._turned_on:
            self._turned_on = False

class SmartPhone(Electronic, LogPrintMixin):
    def turn_on(self):
        super().turn_on()

        if self._turned_on:
            msg = f'{current_time} - {self._name} is turned on'
            self.log_success(msg)

    def turn_off(self):
        super().turn_off()

        if not self._turned_on:
            msg = f'{current_time} - {self._name} is turned off'
            self.log_success(msg)


if __name__ == '__main__':
    ...