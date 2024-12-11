import calendar
print(calendar.isleap(1900)) # False
print(calendar.isleap(1996)) # True
print(calendar.isleap(1999)) # False
print(calendar.isleap(2000)) # True
print(calendar.isleap(2002)) # False
print(calendar.isleap(2004)) # True

### datetime 모듈
from datetime import date
halloween = date(2019, 10, 31)
print(halloween) # 2019-10-31
print(halloween.day) # 31
print(halloween.month) # 10
print(halloween.year) # 2019

print(halloween.isoformat())
# 2019-10-31

from datetime import date
now = date.today()
print(now) # 2024-12-12

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow) # 2024-12-13
print(now + 17*one_day) # 2024-12-29

yesterday = now - one_day
print(yesterday) # 2024-12-11

from datetime import time
noon = time(12, 0, 0)
print(noon) # 12:00:00
print(noon.hour) # 12
print(noon.minute) # 0
print(noon.second) # 0
print(noon.microsecond) # 0

from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day) # 2019-01-02 03:04:05.000006

print(some_day.isoformat()) # 2019-01-02T03:04:05.000006

from datetime import datetime
now = datetime.now()
print(now) # 2024-12-12 01:22:24.677962
print(now.year) # 2024
print(now.month) # 12
print(now.day) # 12
print(now.hour) # 1
print(now.minute) # 23
print(now.second) # 8
print(now.microsecond) # 335907

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today) # 2024-12-12 12:00:00

print(noon_today.date()) # 2024-12-12
print(noon_today.time()) # 12:00:00

# time 모듈
import time
now = time.time()
print(now) # 1733934515.0891626

print(time.ctime(now)) # Thu Dec 12 01:29:23 2024

print(time.localtime(now))
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12, 
# tm_hour=1, tm_min=30, tm_sec=34, tm_wday=3, tm_yday=347, tm_isdst=0)
print(time.gmtime(now))
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=11, 
# tm_hour=16, tm_min=30, tm_sec=34, tm_wday=2, tm_yday=346, tm_isdst=0)

import time
now = time.localtime()
print(now)
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12, 
# tm_hour=1, tm_min=35, tm_sec=26, tm_wday=3, tm_yday=347, tm_isdst=0)
print(now[0]) # 2024
print(list(now[x] for x in range(9))) # [2024, 12, 12, 1, 36, 19, 3, 347, 0]

now = time.time()

tm = time.localtime(now)
print(time.mktime(tm)) # 1733935117.0

# 날짜와 시간 읽고 쓰기
import time
now = time.time()
print(time.ctime(now)) # Thu Dec 12 01:41:18 2024

import time
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12,
# tm_hour=1, tm_min=48, tm_sec=3, tm_wday=3, tm_yday=347, tm_isdst=0)

print(time.strftime(fmt, t))
# It's Thursday, December, 12, 2024, local time 01:48:30AM

from datetime import date
some_day = date(2019, 7, 4)
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
print(some_day.strftime(fmt))
# It's Thursday, July, 04, 2019, local time 12:00:00AM

from datetime import time
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
some_time = time(10, 35)
print(some_time.strftime(fmt))
# It's Monday, January, 01, 1900, local time 10:35:00AM

import time
fmt = "%Y-%m-%d"
# time.strptime("2019 01 29", fmt)
# Traceback (most recent call last):
# ~~~
# ValueError: time data '2019 01 29' does not match format '%Y-%m-%d'

import time
fmt = "%Y-%m-%d"
print(time.strptime("2019-01-29", fmt))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, 
# tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)

import time
fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, 
# tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)

# time.strptime("2019-13-29", fmt)
# Traceback (most recent call last):
# ~~~
# ValueError: time data '2019-13-29' does not match format '%Y %m %d'

import locale
from datetime import date
halloween = date(2019, 10, 31)
for lang_contry in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_contry)
    print(halloween.strftime('%A, %B %d'))
# Thursday, October 31
# jeudi, octobre 31
# Donnerstag, Oktober 31
# jueves, octubre 31
# fimmtudagur, okt�ber 31

import locale
names = locale.locale_alias.keys()

good_names = [name for name in names if \
            len(name) == 5 and name[2] == '_']

print(good_names[:5]) 
# ['a3_az', 'aa_dj', 'aa_er', 'aa_et', 'af_za']

# 모든 독일어 로케일
de = [name for name in good_names if name.startswith('de')]
print(de) # ['de_at', 'de_be', 'de_ch', 'de_de', 'de_it', 'de_lu']