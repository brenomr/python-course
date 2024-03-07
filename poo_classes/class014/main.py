"""
Abstract: main module to make tests
"""

from log import LogFileMixin, LogPrintMixin
from electronic import SmartPhone

galaxy_1 = SmartPhone('Galaxy 1')
galaxy_n = SmartPhone('Galaxy N')

galaxy_1.turn_on()
galaxy_n.turn_off()


# For tests
# l3 = LogPrintMixin()
# l3.log_error('Params not defined on L3')
# l3.log_success('L3 completed all tasks')

# l2 = LogFileMixin()
# l2.log_success('Params not defined on L1')
# l2.log_error('L1 completed all tasks')
