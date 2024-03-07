"""
Abstract: main module to make tests
"""

from log import LogFileMixin, LogPrintMixin

l3 = LogPrintMixin()
l3.log_error('Params not defined on L3')
l3.log_success('L3 completed all tasks')

l2 = LogFileMixin()
l2.log_success('Params not defined on L1')
l2.log_error('L1 completed all tasks')
