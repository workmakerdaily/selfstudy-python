# 날짜와 시간
### 윤년
윤년은 특정한 시간 주기다. 4년에 한 번씩 온다.
```python
import calendar
print(calendar.isleap(1900)) # False
print(calendar.isleap(1996)) # True
print(calendar.isleap(1999)) # False
print(calendar.isleap(2000)) # True
print(calendar.isleap(2002)) # False
print(calendar.isleap(2004)) # True
```

<br/>

### datetime 모듈
표준 datetime 모듈은 날짜와 시간을 처리한다.
이 모듈은 여러 메서드를 가진 4개의 주요 객체 클래스르 정의한다.
- date: 년, 월, 일
- time: 시, 분, 초, 마이크로초
- datetime: 날짜, 시간
- timedelta: 날짜 및 시간 간격

년, 월 일을 지정하여 date 객체를 만들 수 있다.
```python
from datetime import date
halloween = date(2019, 10, 31)
print(halloween) # 2019-10-31
print(halloween.day) # 31
print(halloween.month) # 10
print(halloween.year) # 2019
```
isoformat() 메서드로 날짜를 출력할 수 있다.
```python
print(halloween.isoformat())
# 2019-10-31
```
iso는 날짜와 시간의 표기에 관한 국제 표준 규격인 ISO 8601을 참고한다.
년, 월, 일 순으로 표현한다.

today() 메서드를 사용하여 오늘 날짜를 출력한다.
```python
from datetime import date
now = date.today()
print(now) # 2024-12-12
```
timedelta 객체를 사용하여 날짜에 시간 간격을 더할 수 있다.
```python
from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow) # 2024-12-13
print(now + 17*one_day) # 2024-12-29

yesterday = now - one_day
print(yesterday) # 2024-12-11
```
datetime 모듈의 time 객체는 하루의 시간을 나타내는 데 사용된다.
```python
from datetime import time
noon = time(12, 0, 0)
print(noon) # 12:00:00
print(noon.hour) # 12
print(noon.minute) # 0
print(noon.second) # 0
print(noon.microsecond) # 0
```
인수는 가장 큰 시간 단위부터 가장 작은 시간 단위 순으로 입력한다.
인수를 입력하지 않으면 time 객체의 초기 인수는 0으로 간주된다.
컴퓨터는 마이크로초를 정확하게 계산할 수 없다.

datetime 객체는 날짜와 시간 모두를 포함한다.
```python
from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day) # 2019-01-02 03:04:05.000006
```
datetime 객체도 isoformat() 메서드가 있다.
```python
print(some_day.isoformat()) # 2019-01-02T03:04:05.000006
```
중간의 T는 날짜와 시간을 구분한다.

datetime 객체에서 now() 메서드로 현재 날짜와 시간을 얻을 수 있다.
```python
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
```
combine()으로 date 객체와 time 객체를 datetime 객체로 병합할 수 있다.
```python
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today) # 2024-12-12 12:00:00
```
datetime 객체에서 date()와 time() 메서드를 사용하여 날짜와 시간을 얻을 수 있다.
```python
print(noon_today.date()) # 2024-12-12
print(noon_today.time()) # 12:00:00
```

<br/>

---

# time 모듈
datetime 모듈의 time 객체와 별도의 time 모듈이 헷갈릴 수 있다.

유닉스 시간은 1970년 1월 1일 자정 이후 시간의 초를 사용한다. 이 값을 에폭이라고 부르며, 에폭은 시스템간에 날짜와 시간을 교환하는 아주 간단한 방식이다.

time 모듈의 time() 함수는 현재 시간을 에폭 값으로 반환한다.
```python
import time
now = time.time()
print(now) # 1733934515.0891626
```
ctime() 함수를 사용하여 에폭 값을 문자열로 변환할 수 있다.
```python
print(time.ctime(now)) # Thu Dec 12 01:29:23 2024
```

localtime() 메서드는 시간을 시스템의 표준 시간대로, gmtime() 메서드는 시간을 UTC로 제공한다.
```python
print(time.localtime(now))
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12, 
# tm_hour=1, tm_min=30, tm_sec=34, tm_wday=3, tm_yday=347, tm_isdst=0)
print(time.gmtime(now))
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=11, 
# tm_hour=16, tm_min=30, tm_sec=34, tm_wday=2, tm_yday=346, tm_isdst=0)
```

> ### struct_time 값
|인덱스|이름|설명|값|
|---|---|---|---|
|0|tm_year|년|0000 ~ 9999|
|1|tm_mon|월|1 ~ 12|
|2|tm_mday|일|1 ~ 31|
|3|tm_hour|시|0 ~ 23|
|4|tm_min|분|0 ~ 59|
|5|tm_sec|초|0 ~ 59|
|6|tm_wday|요일|0(월요일) ~ 6(일요일)|
|7|tm_yday|년일자|1 ~ 366|
|8|tm_isdst|일광 시간 절약제|0 = 아니오, 1 = 예, -1 = 모름|

struct_time에서 tm_... 대신, 네임드 튜플처럼 인덱스를 사용할 수 있다.
```python
import time
now = time.localtime()
print(now)
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12, 
# tm_hour=1, tm_min=35, tm_sec=26, tm_wday=3, tm_yday=347, tm_isdst=0)
print(now[0]) # 2024
print(list(now[x] for x in range(9))) # [2024, 12, 12, 1, 36, 19, 3, 347, 0]
```

mktime() 메서드는 struct_time 객체를 에폭 초로 변환한다.
```python
now = time.time()

tm = time.localtime(now)
print(time.mktime(tm)) # 1733935117.0
```
이 값은 조금 전 now()의 에폭 값과 정확하게 일치하지 않는다.
struct_time 객체는 시간을 초까지만 유지하기 때문이다.

<br/>

---

# 날짜와 시간 읽고 쓰기
isoformat()이 날짜와 시간을 쓰기 위한 유일한 방법은 아니다.
time 모듈의 ctime() 함수로 쓸 수도 있다.(이 함수는 에폭 시간을 문자열로 변환한다.)
```python
import time
now = time.time()
print(time.ctime(now)) # Thu Dec 12 01:41:18 2024
```
strftime()을 사용하여 날짜와 시간을 문자열로 변환할 수 있다.

> ### strftime() 출력 지정자
|문자열 포맷|날짜/시간 단위|범위|
|---|---|---|
|%Y|년|1900 -...|
|%m|월|01 - 12|
|%B|월 이름|January, ...|
|%b|월 축약 이름|Jan, ...|
|%d|월의 일자|01 - 31|
|%A|요일 이름|Sunday, ...|
|%a|요일 축약 이름|Sun, ...|
|%H|24시간|00 - 23|
|%I|12시간|01 - 12|
|%p|오전/오후|AM, PM|
|%M|분|00 - 59|
|%S|초|00 - 59|
- 숫자는 자릿수에 맞춰 왼쪽에 0이 채워진다.

time 모듈의 strftime() 함수다.
이것은 struct_time 객체를 문자열로 변환한다.
```python
import time
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
# time.struct_time(tm_year=2024, tm_mon=12, tm_mday=12,
# tm_hour=1, tm_min=48, tm_sec=3, tm_wday=3, tm_yday=347, tm_isdst=0)

print(time.strftime(fmt, t))
# It's Thursday, December, 12, 2024, local time 01:48:30AM
```
이것을 date 객체에 사용하면 날짜 부분만 작동한다. 그리고 시간은 기본값으로 자정으로 지정된다.
```python
from datetime import date
some_day = date(2019, 7, 4)
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
print(some_day.strftime(fmt))
# It's Thursday, July, 04, 2019, local time 12:00:00AM
```
time 객체는 시간 부분만 변환한다.
```python
from datetime import time
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
some_time = time(10, 35)
print(some_time.strftime(fmt))
# It's Monday, January, 01, 1900, local time 10:35:00AM
```
time 객체에서 날짜를 사용할 수 없다.

문자열을 날짜나 시간으로 변환하기 위해 같은 포맷 문자열로 strptime()을 사용한다.
정규 표현식 패턴 매칭은 없다.
문자열 비형식 부분(% 제외)이 정확히 일치해야 한다.
날짜 문자열에서 대시 대신 공백을 사용하면 에러가 발생한다.
```python
import time
fmt = "%Y-%m-%d"
time.strptime("2019 01 29", fmt)
# Traceback (most recent call last):
# ~~~
# ValueError: time data '2019 01 29' does not match format '%Y-%m-%d'
```
대시를 붙이면 정삭 작동된다.
```python
import time
fmt = "%Y-%m-%d"
print(time.strptime("2019-01-29", fmt))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, 
# tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)
```

날짜 문자열과 일치하도록 문자열 fmt를 수정할 수 있다.
```python
import time
fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, 
# tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=29, tm_isdst=-1)
```
문자열 포맷은 맞는데 값 범위를 벗어나면 예외가 발생한다.
```python
time.strptime("2019-13-29", fmt)
# Traceback (most recent call last):
# ~~~
# ValueError: time data '2019-13-29' does not match format '%Y %m %d'
```
이름은 운영체제의 국제화 설정인 로케일에 따라 다르다.
다른 월, 일의 이름을 출력하려면 setlocale()을 사용하여 로케일을 바꿔야 한다.
setlocale()의 첫 번째 인수는 날짜와 시간을 위한 locale.LC_TIME이고, 두 번쨰는 언어와 국가 약어가 결합된 문자열이다.
```python
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
```
lang_country에 대한 값은 다음 예제를 실행하여 몇 백 개의 값을 모두 찾을 수 있다.
```python
import locale
names = locale.locale_alias.keys()
```

setlocale()을 실행하기 위해 names로부터 로케일 이름을 얻어온다.
```python
good_names = [name for name in names if \
            len(name) == 5 and name[2] == '_']
            
# 처음 5개
print(good_names[:5]) 
# ['a3_az', 'aa_dj', 'aa_er', 'aa_et', 'af_za']

# 모든 독일어 로케일
de = [name for name in good_names if name.startswith('de')]
print(de) # ['de_at', 'de_be', 'de_ch', 'de_de', 'de_it', 'de_lu']
```



