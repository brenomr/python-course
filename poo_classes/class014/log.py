"""
Abstract: log module

Abstract method: log (will need to implement it)
Class inheritance: LogFileMixin is a Log
"""

from pathlib import Path

FILE_PATH = Path(__file__).parent / 'logfile.log'

class Log():

    def _log(self, msg: str, status: str):
        raise NotImplemented('You should implement this method!')

    def log_error(self, msg: str):
        return self._log(f'Error: {msg}.', 'Error')

    def log_success(self, msg: str):
        return self._log(f'Success: {msg}.', 'Success')

class LogFileMixin(Log):
    def _log(self, msg: str, status: str):
        edt_msg = f'{msg} (from {self.__class__.__name__})'
        
        with open(FILE_PATH, 'a', encoding='utf8') as file:
            print(f'Adding new {status.lower()} entry at log...')
            file.write(f'{edt_msg}')
            file.write('\n')
        print(f'File saved at: {FILE_PATH}')


class LogPrintMixin(Log):
    def _log(self, msg:str, status: str):
        print(f'{msg} (from {self.__class__.__name__})')

if __name__ == '__main__':
    l1 = LogPrintMixin()
    l1.log_error('Params not defined on L1')
    l1.log_success('L1 completed all tasks')

    l2 = LogFileMixin()
    l2.log_success('None type detected as argument')
    l2.log_error('L2 completed all tasks')
