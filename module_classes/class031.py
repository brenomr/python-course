"""
Using datetime and timezone from pytz modules

Some uses of datetime module:
datetime(year, month, day, hour, minute, second, microsecond)
datetime.strptime('date', 'format')
datetime.now()
"""
from datetime import datetime
from pytz import timezone

# Creating a datetime object
date = datetime(2021, 5, 15)

# Creating datetime object with hours, minutes, seconds and microseconds
date = datetime(2021, 5, 15, 12, 30, 45, 100000)

# print(date)

# date_str = '2021-05-15 15:30:45'
date_str = '15/05/2021 14:33:55'

# date_pattern = '%Y-%m-%d %H:%M:%S'
date_pattern = '%d/%m/%Y %H:%M:%S'

# Create datetime object from a string
date = datetime.strptime(date_str, date_pattern)

# print(date)

# Get current date and time with timezone
tz = timezone('America/Sao_Paulo')
tzt = timezone('Asia/Tokyo')
date_sao_paulo = datetime.now(tz)
date_tokyo = datetime.now(tzt)

# print(date_sao_paulo)
# print(date_tokyo)

# Adding timezone to a datetime object (it won't reflected in the time)
custom_date_tz_tokyo = datetime(2021, 5, 15, 12, 44, 50, tzinfo=tzt)
# print(custom_date_tz_tokyo)

# Get the timestamp, date in seconds since 1970
# timestamp won't consider the timezone
# print(custom_date_tz_tokyo.timestamp())

# Create a datetime object from a timestamp
timestamp = 1712109499.321232  # 2024-04-03 10:58:19
date_from_timestamp = datetime.fromtimestamp(timestamp, tz=tzt)

# print(date_from_timestamp)
