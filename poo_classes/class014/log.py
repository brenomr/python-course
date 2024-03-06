"""
Abstract: log module

Abstract method: log (will need to implement it)
Class inheritance: LogFileMixin is a Log
"""

class Log():

    def _log(self, msg):
        raise NotImplemented('You should implement this method!')

    def log_error(self, msg):
        return self._log(f'Error: {msg}.')

    def log_success(self, msg):
        return self._log(f'Success: {msg}.')

class LogFileMixin(Log):
    def _log(self, msg):
        print(f'{msg} (from {self.__class__.__name__})')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} (from {self.__class__.__name__})')

if __name__ == '__main__':
    l1 = LogPrintMixin()
    l1.log_error('Show me!')
    l1.log_success('Show me!')
