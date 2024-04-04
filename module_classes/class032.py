"""
Comparing and formatting date

More options than timedelta with relativedelta:
pip install python-dateutil types-python-dateutil
from dateutil.relativedelta import relativedelta
"""
from datetime import datetime, timedelta

#################
# COMPARING DATES
#################

fmt = "%d/%m/%Y %H:%M:%S"

start_date = datetime.strptime("14/3/2001 14:55:03", fmt)
end_date = datetime.strptime("20/12/2002 10:35:49", fmt)
time_delta = end_date - start_date

print(time_delta)  # time_delta.days, seconds, microseconds

ten_days = timedelta(days=10)  # hours, minuts, etc
end_date = (end_date + ten_days)
print(end_date)

##################
# FORMATTING DATES
##################

# STRing Parsed to dateTIME object (strptime)
date = datetime.strptime('2022-11-20 10:30:05', '%Y-%m-%d %H:%M:%S')
print(f'DATE: {date} - TYPE: {type(date)}')
print(date.day, date.month, date.year)  # date.hour, minute, second

string_date = date.strftime('%d/%m/%y')
string_date = date.strftime('%d/%m/%y %H:%M')
print(f'DATE: {string_date} - TYPE: {type(string_date)}')
