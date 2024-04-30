"""
Using locale

Inside locale we have:
LC_ALL: All locale settings.
LC_MONETARY: Monetary formatting.
LC_NUMERIC: Number formatting.
LC_TIME: Time formatting.

etc...

Usefull command in terminal to show
available locales on your system:
locale -a
"""

import calendar
import locale

# Original en-US calendar
# print(calendar.calendar(2024))

# Setting locale from OS
# locale.setlocale(locale.LC_ALL, '')

# Setting locale to pt-BR
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Changed to pt-BR calendar
print(calendar.calendar(2024))

# Getting the configured locale
print(locale.getlocale())
