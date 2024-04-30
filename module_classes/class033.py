"""
Using calendar
"""

import calendar

# print calendar of 2022
# print(calendar.calendar(2022))

# print calendar of march, 2022
# print(calendar.month(2022, 3))

# last day of the month (the return will be a tuple of:
# (weekday of the first day, last_day))
# print(calendar.monthrange(2024, 1))

# weekday: 0 = monday, 6 = sunday
# print(list(calendar.day_name))
# print(list(enumerate(calendar.day_name)))
# print(calendar.weekday(2024, 1, 1))

# Day of the week of the last day of the month
day_of_week, last_month_day = calendar.monthrange(2024, 1)
print(f'Week day of first day (name): {calendar.day_name[day_of_week]}.')
print(f'Week day of first day (number): {day_of_week}')
print(f'Week day of last day: {calendar.weekday(2024, 1, last_month_day)}')
