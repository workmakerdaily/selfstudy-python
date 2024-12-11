# 데이터 길들이기
기본 데이터 형식부터 데이터 과학을 위한 가장 유용한 도구까지 살펴볼 것이다.
데이터 형식을 크게 텍스트와 2진수로 나눌 수 있다.
텍스트 데이터에서 파이썬 문자열을 사용한다.

<br/>

# 텍스트 문자열: 유니코드
파이썬 3의 문자열은 바이트 배열이 아닌 유니코드 문자 시퀀스다.
국가별로 독자적인 무낮열 인코딩을 사용하는 것을 해결하기 위해 국제 표준화 기구에서 유니코드를 만들었다.
유니코드는 수학 및 기타 분야의 기호들도 포함한다.(이모티콘 까지)

### 파이썬 3 유니코드 문자열
- 4자리 16진수와 그 앞에 \u는 유니코드의 기본 평면 256개 중 하나의 문자를 지정한다.
첫 번째 두 숫자는 평면 번호다(00에서 ff까지).
다음 두 숫자는 평면에 있는 문자의 인덱스다.
평면 00은 아스키 코드고, 평면 안의 문자 위치는 아스키 코드의 번호와 같다.
- 높은 평면의 문자일수록 비트 수가 더 필요하다. 이에 대한 파이썬의 이스케이프 시퀀스는 \U고, 8자리의 16진수를 사용한다. 숫자에 남는 공간이 있다면 왼쪽에 0을 채운다.
- 모든 문자는 표준 이름 \N{name}으로 지정할 수 있다. 유니코드 문자 이름 인덱스 페이지에서 표준 이름 리스트를 참조한다.

파이썬의 unicodedata 모듈은 유니코드 식별자와 이름으로 검색할 수 있는 함수를 제공한다.
- lookup() : 인수로 대소 문자를 구분하지 않는 이름을 취하고, 유니코드 문자를 반환한다.
- name() : 인수로 유니코드 문자를 취하고, 대문자 이름을 반환한다.
```python
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
    
# 아스키 문자
unicode_test('A')
# value="A", name="LATIN CAPITAL LETTER A", value2="A"

# 아스키 문자 부호
unicode_test('$')
# value="$", name="DOLLAR SIGN", value2="$"

# 유니코드 통화 문자
unicode_test('\u00a2')
# value="¢", name="CENT SIGN", value2="¢"

# 유니코드 통화 문자
unicode_test('\u20ac')
# value="€", name="EURO SIGN", value2="€"
```
잠재적으로 발생할 수 있는 유일한 문제는 텍스트를 표시하는 데 사용하는 글꼴의 제한이다.
모든 유니코드에 대한 이미지가 있는 글꼴은 거의 없으며, 누락된 글꼴에 대하여 플레이스홀더 문자가 표시될 수 있다.
```python
# 딩벳 글꼴의 SNOWMAN에 대한 유니코드 기호
unicode_test('\u2603')
# value="☃", name="SNOWMAN", value2="☃"
```
<br/>

é문자를 얻는 방법은 E에 대한 문자 인덱스를 찾아(http://bit.ly/e-index)
name()과 lookup() 함수로 문자 인덱스를 확인할 수 있다.
```python
import unicodedata
print(unicodedata.name('\u00e9'))
# LATIN SMALL LETTER E WITH ACUTE

print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')) # é
```
이제 코드와 이름으로 문자열 café를 저장할 수 있다.
```python
place = 'caf\u00e9'
print(place) # café

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place) # café
```
다음과 같이 문자열에 추가하는 것도 가능하다.
```python
u_umlaut = '\N{LATIN SMALL LETTER E WITH ACUTE}'
print(u_umlaut) # é

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)
# Now I can finally have my Gewérztraminer in a café
```
문자열 len() 함수는 유니코드의 바이트가 아닌 문자수를 센다.
```python
print(len('$')) # 1
print(len('\U0001f47b')) # 1
```
유니코드 숫자 ID를 알고 있다면, ord()와 chr() 함수를 사용하여 정수 ID로 단일 문자의 유니코드 문자열을 빠르게 변환할 수 있다.
```python
print(chr(233)) # é
print(chr(0xe9)) # é
print(chr(0x1fc6)) # ῆ
```

<br/>

### UTF-8
파이썬에서 일반 문자열을 처리할 때는 각 유니코드 문자를 저장하는 방법에 걱정하지 않아도 된다.
그러나 외부 데이터를 교환할 때는 다음 과정이 필요하다.
- 문자열을 바이트로 인코딩
- 바이트를 문자열로 디코딩

유니코드는 한 문자당 1~4바이트를 사용한다.
- 1바이트 : 아스키 코드
- 2바이트 : 키릴 문자를 제외한 대부분 파생된 라틴어
- 3바이트 : 기본 다국어 평면의 나머지
- 4바이트 : 아시아 언어 및 기호를 포함한 나머지

코드에 UTF-8 인코딩 방식을 사용하면 다양한 인코딩 방식을 시도하는 것보다 편해진다.

<br/>

### 인코딩
문자열을 바이트로 인코딩할 수 있다.
문자열 encode() 함수의 첫 번째 인수는 인코딩 이름이다.

|인코딩 이름|설명|
|---|---|
|'ascii'|7비트 아스키 코드|
|'utf-8'|8비트 가변 길이 인코딩 형식. 거의 대부분의 문자 지원|
|'latin-1'|ISO 8859-1로도 알려짐|
|'cp-1252'|윈도우 인코딩 형식|

모두 UTF-8로 인코딩할 수 있다.
```python
snowman = '\u2603'

print(len(snowman)) # 1
```
snowman은 한 문자의 파이썬 유니코드 문자열이다.
유니코드 문자를 바이트 시퀀스로 인코딩할 수 있다.
```python
ds = snowman.encode('utf-8')
```
UTF-8은 가변 길이 인코딩이다.
이 경우 유니코드 문자를 인코딩 하기 위해 3바이트를 사용한다.
```python
print(len(ds)) # 3
print(ds) # b'\xe2\x98\x83'
```

UTF-8 아외의 다른 인코딩도 사용할 수 있다. 하지만 유니코드 문자열을 인코딩 할 수 없다면 에러를 얻게 된다.
```python
ds = snowman.encode('ascii')
# Traceback (most recent call last):
# ~~~
# UnicodeEncodeError: 'ascii' codec can't encode 
# character '\u2603' in position 0: ordinal not in range(128)
```
인코딩 예외를 피하기 위해 encode() 함수에 두 번째 인수를 취한다.
아스키 코드가 아닌 문자가 나타났을 때 UnicodeEncodeError를 발생시킨다.
'ignore'를 사용하여 알 수 없는 문자를 인코딩하지 않도록 할 수 있다.
```python
print(snowman.encode('ascii', 'ignore')) # b''
```
'replace'는 알 수 없는 문자를 ?로 대체한다.
```python
print(snowman.encode('ascii', 'replace')) # b'?'
```
'backslashreplace'는 유니코드 이스케이프처럼 파이썬 유니코드 문자의 문자열을 만든다.
```python
print(snowman.encode('ascii', 'backslashreplace')) # b'\\u2603'
```
HTML-safe 문자열 생성을 위해서 'xmlcharrefreplace'를 사용한다.
유니코드 이스케이프 시퀀스를 출력할 수 있는 문자열로 만든다.
```python
print(snowman.encode('ascii', 'xmlcharrefreplace')) # b'&#9731;'
```

<br/>

### 디코딩
바이트 문자열을 유니코드 문자열로 디코딩할 수 있다.
외부 소스에서 텍스트를 얻을 때마다 그것은 바이트 문자열로 인코딩되어 있다.
실제로 어떤 인코딩이 사용되었는지 분서가여 유니코드 문자열을 얻을 수 있다.
문제는 바이트 문자열이 어떻게 인코딩 되었는지 말해주지 않는다.

유니코드 문자열을 생성해본다.
```python
place = 'caf\u00e9'
print(place) # café
print(type(place)) # <class 'str'>
```
place 변수를 UTF-8 형식으로 인코딩하여 place_bytes 변수에 할당한다.
```python
place_bytes = place.encode('utf-8')
print(place_bytes) # b'caf\xc3\xa9'
print(type(place_bytes)) # <class 'bytes'>
```
place_bytes는 5바이트다.
첫 3바이트는 UTF-8과 똑같이 표현되는 아스키 문자다.
마지막 2바이트는 é를 인코딩했다.
바이트 문자열을 유니코드 문자열로 디코딩해본다.
```python
place2 = place_bytes.decode('utf-8')
print(place2) # café
```
다른 인코딩 방식으로 디코딩하면 에러가 발생한다.
```python
place3 = place_bytes.decode('ascii')
# Traceback (most recent call last):
# ~~~
# UnicodeDecodeError: 'ascii' codec 
# can't decode byte 0xc3 in position 3: ordinal not in range(128) 
```
아스키 디코더는 예외를 던진다.
0xc3 바이트 값이 유효하지 않기 때문이다.
```python
place4 = place_bytes.decode('latin-1')
print(place4) # cafÃ©

place5 = place_bytes.decode('windows-1252')
print(place5) # cafÃ©
```
가능하면 UTF-8을 사용하는 것이 좋다.
UTF-8은 모든 유니코드 문자를 표현할 수 있고, 어디에서나 지원한다.
그리고 빠르게 디코딩과 인코딩을 수행한다.

<br/>

### HTML 엔티티
파이썬 3.4에서 유니코드로 변환하거나 HTML 문자 엔티티를 사용하는 또 다른 방법을 추가했다. 웹 작업의 경우 유니코드 이름을 찾기가 쉬워졌다.
```python
import html
print(html.unescape("&egrave;")) # è
```
엔티티 10진수나 16진수에도 적용된다.
```python
import html
print(html.unescape("&#233;")) # é
print(html.unescape("&#xe9;")) # é
```
명명된 문자 엔티티 번역을 딕셔너리로 가져와서 직접 변환할 수 있다.
딕셔너리 키에서 처음 '&'문자를 삭제한다.(마지막 ';'를 삭제할 수도 있다.)
```python
from html.entities import html5
print(html5["egrave"]) # è
print(html5["egrave;"]) # è
```
단일 파이썬 유니코드 문자에서 HTML 엔티티 이름으로 변환할 수 있다.
ord()를 사용하여 문자의 10진수 값을 얻는다.
```python
import html
char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])
# eacute
```
문자가 2개 이상인 유니코드 문자열도 2단계로 변환가능하다.
```python
place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value) # b'caf&#233;'
print(byte_value.decode()) # caf&#233;
```
place.encode('ascii', 'xmlcharrefreplace') 표현식은 인코딩된 아스키 문자의 바이트 타입을 반환한다.
byte_value를 HTML 호환 문자열로 변환하려면 byte_value.decode()로 디코딩한다.

<br/>

### 정규화
일부 유니코드 문자는 둘 이상의 유니코드 인코딩으로 표현된다.
모양은 같지만 내부 시퀀스가 다르기 때문에 동일하게 보지 않는다.
```python
eacute1 = 'é' # UTF-8
eacute2 = '\u00e9' # 유니코드 코드 포인트
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}' # 유니코드 이름
eacute4 = chr(233) # 10진수 바이트 값
eacute5 = chr(0xe9) # 16진수 바이트 값

print(eacute1, eacute2, eacute3, eacute4, eacute5)
# é é é é é
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)
# True
```
```python
import unicodedata
print(unicodedata.name(eacute1))
# LATIN SMALL LETTER E WITH ACUTE
print(ord(eacute1)) # 233
print(0xe9) # 233
```
그냥 e와 양음 악센트를 결합하여 é를 만든다.
```python
eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"

print(eacute_combined1, eacute_combined2, eacute_combined3)
# é é é
print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# True
```
위 두가지는 동일하게 보이지만 다르다.
```python
print(eacute1 == eacute_combined1) # False
```
unicodedata 모듈에서 normalize() 함수를 사용하여 이러한 문제를 해결할 수 있다.
```python
print(len(eacute_normalized)) # 1
print(eacute_normalized == eacute1) # True
print(unicodedata.name(eacute_normalized))
# LATIN SMALL LETTER E WITH ACUTE
```
'NFC'는 구성된 일반 형식을 의미한다.

<br/>

---

# 정규 표현식
정규 표현식으로 복자반 문자열 패턴 매칭이 가능하다.
정규 표현식은 임포트 할 수 있는 표준 모듈 re로 제공한다.
```python
import re
result = re.match('You', 'Young Frankenstein')
```
'You'는 패턴이고, 'Young Frankenstein'은 확니하고자 하는 문자열 소스다.
match()는 소스와 패턴의 일치 여부를 확인한다.

나중에 패턴 확인을 빠르게 하기 위해 패턴을 먼저 컴파일할 수 있다.
```python
youpattern = re.compile('You')
```
긜고 컴파일된 패턴으로 패턴 일치 여부를 확인할 수 있다.
```python
result = youpattern.match('Young Frankenstein')
```
match()는 소스 처음부터 시작하는 패턴만 매칭한다.
search()는 소스 어디에서나 패턴을 찾아 매칭한다.
- search()는 첫 번째 일치하는 항목을 반환한다.
- findall()은 중첩에 상관없이 패턴에 일치하는 모든 문자열 리스트를 반환한다.
- split()은 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트를 반환한다.
- sub()는 대체 인수를 하나 더 받아서, 패턴에 일치하는 모든 소스 부분을 대체 인수로 변경한다.

<br/>

### 시작부터 일치하는 패턴 찾기: match()
```python
import re
source = 'Young Frankenstein'
m = re.match('You', source)

if m:
    print(m.group())
# You

m = re.match('^You', source)  # 앵커 시작도 마찬가지이다.
if m:
    print(m.group())
# You
```

'Frank'로 찾아본다.
```python
import re
source = 'Young Frankenstein'
m = re.match('Frank', source)
if m:
    print(m.group())
#
```
match()가 아무것도 반환하지 않는다.
match()는 패턴이 소스의 처음에 있는 경우에만 작동한다.
:= 연산자를 사용하여 위 예제 코드를 줄일 수 있다.
```python
import re
source = 'Young Frankenstein'
if m:= re.match('Frank', source):
    print(m.group())
#
```

search()는 패턴이 어떤 위치에 있더라도 동작한다.
```python
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
    print(m.group())
# Frank
```
패턴을 바꿔 match()를 다시 적용해본다.
```python
import re
source = 'Young Frankenstein'
m = re.match('.*Frank', source)
if m: # match는 객체를 반환한다.
    print(m.group())
# Young Frank
```

> ### .*Frnak
- .은 한 문자를 의미한다.
- *은 어떤 패턴이 0회 이상 올 수 있다는 것을 의미한다.
- .*은 0회 이상의 문자가 올 수 있다는 것을 의미한다.
- Frank는 포함되어야 할 문구를 의미한다.

<br/>

### 첫 번째 일치하는 패턴 찾기: search()
.* 와일드카드 없이 소스 문자열에서 패턴을 찾기 위해 search()를 사용할 수 있다.
```python
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m: # search는 객체를 반환한다.
    print(m.group())
# Frank
```

<br/>

### 일치하는 모든 패턴 찾기: findall()
```python
import re
source = 'Young Frankenstein'
m = re. findall('n', source)

print(m) # ['n', 'n', 'n', 'n']
print('Found', len(m), 'matches')
# Found 4 matches
```
'n' 다음에 어떤 문자가 오는지 알 수 있다.
```python
import re
source = 'Young Frankenstein'
m = re.findall('n.', source)
print(m) # ['ng', 'nk', 'ns']
```
마지막 'n'은 위 패턴에 포함되지 않는다.
(.은 한 문자를 의미하고, ?는 0 또는 1회를 의미한다. 그러므로 ?는 하나의 문자가 0 또는 1회 올 수 있다는 뜻이다.)
```python
import re
source = 'Young Frankenstein'
m = re.findall('n.?', source)
print(m) # ['ng', 'nk', 'ns', 'n']
```

<br/>

### 패턴으로 나누기: split()
```python
import re
source = 'Young Frankenstein'
m = re.split('n', source)
# split는 리스트를 반환한다.
print(m) # ['You', 'g Fra', 'ke', 'stei', '']
```

<br/>

### 일치하는 패턴 대체하기: sub()
sub() 메서드는 리터럴 문자열이 아닌 패턴을 사용한다.
```python
### 일치하는 패턴 대체하기: sub()
import re
source = 'Young Frankenstein'
m = re.sub('n', '?', source)
# sub는 문자열을 반환한다.
print(m) # You?g Fra?ke?stei?
```

<br/>

### 패턴: 특수 문자
정규 표현식은 아주 많은 문장 부호를 사용한다.
match(), search(), findall(), sub() 메서드에서는 아래의 패턴을 적용할 수 있다.
- 리터럴은 모든 비특수 문자와 일치한다.
- \n을 제외한 하나의 문자: .
- 이전 문자 0회 이상: *
- 이전 문자 0 또는 1회: ?

> ### 특수 문자
|패턴일치|
|---|---|
|\d|숫자|
|\D|비숫자|
|\w|알파벳 문자|
|\W|비알파벳 문자|
|\s|공백 문자|
|\S|비공백 문자|
|\b|단어 경계(/w와 /W 또는 \W와 \w 사이의 경계|

string 모듈은 테스트에 사용할 수 있는 문자열 상수가 미리 정의되어 있다.
printable은 대소 문자, 숫자, 공백 문자. 구두점을 포함한 아스키 문자 100가지가 포함되어 있다.
```python
print(len(printable)) # 100
print(printable[0:50])
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
print(printable[50:])
# OPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# 숫자
print(re.findall('\d', printable))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 숫자와 문자, 언더바
print(re.findall('\w', printable))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
# 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
# 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
# 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
# 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']

# 공백 문자
print(re.findall('\s', printable))
# [' ', '\t', '\n', '\r', '\x0b', '\x0c']
```
정규 표현식은 아스키 코드에만 국한되지 않는다.

<br/>

### 패턴: 지정자
expr은 표현식, prev는 이전 토큰, next는 다음 토큰을 의미한다.

|패턴|일치|
|---|---|
|Abc|리터럴 abc|
|( expr )|expr|
|expr1 \| expr2|expr1 또는 expr2|
|.|\n을 제외한 모든 문자|
|^|소스 문자열 시작|
|$|소스 문자열 끝|
|prev ?|0 또는 1회 prev|
|prev \*|0회 이상의 최대 prev|
|prev \*? |0회 이상의 최소 prev|
|prev +|1회 이상의 최대 prev|
|prev \_?|1회 이상의 최소 prev m회 prev|
|prev {m}|m회 prev|
|prev {m, n}|m에서 n회 최대 prev|
|prev {m, n}?|m에서 n회 최소 prev|
|[abc]|a 또는 b 또는 c(a\|b\|c와 같음)|
|[^abc]|(a 또는 b 또는 c)가 아님|
|prev (?=next)|뒤에 next가 오면 prev|
|prev (?!next)|뒤에 next가 오지 않으면 prev|
|(?<=prev) next|앞에 prev가 오면 next|
|(?<!prev) next|앞에 prev가 오지 않으면 next|

소스 문자열을 정의한다.
```python
source = '''I wish I may, I wish I might
    Have a dish of fish tonight.'''
```
wish를 모두 찾는다.
```python
print(re.findall('wish', source)) # ['wish', 'wish']
```

wish 또는 fish를 모두 찾는다.
```python
print(re.findall('wish|fish', source)) # ['wish', 'wish', 'fish']
```
wish로 시작하는 것을 찾는다.
```python
print(re.findall('^wish', source)) # []
```
I wish로 시작하는 것을 찾는다.
```python
print(re.findall('^I wish', source)) # ['I wish']
```
fish로 끝나는 것을 찾는다.
```python
print(re.findall('fish$', source)) # []
```
fish tonight.으로 끝나는 것을 찾는다.
```python
print(re.findall('fish tonight.$', source)) # ['fish tonight.']
```
문자 ^와 $는 앵커라고 부른다.
^는 문자열의 시작 위치에, $는 마지막 위치에 고정한다.
정확하게 문자 그대로를 매칭하기 위해 .에 이스케이프 문자를 붙여야 한다.
```python
print(re.findall('fish tonight\.$', source)) # ['fish tonight.']
```
w 또는 f 다음에 ish가 오는 것을 찾는다.
```python
print(re.findall('[wf]ish', source)) # ['wish', 'wish', 'fish']
```
w, s, h가 하나 이상인 것을 찾는다.
```python
print(re.findall('[wsh]+', source)) # ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']
```
ght 다음에 알파벳 문자가 아닌 것을 찾는다.
```python
print(re.findall('ght\W', source)) # ['ght\n', 'ght.']
```
wish 이전에 I를 찾는다.
```python
print(re.findall('I (?=wish)', source)) # ['I ', 'I ']
```
I 다음에 나오는 wish를 찾는다.
```python
print(re.findall('(?<=I) wish', source)) # [' wish', ' wish']
```

<br/>

### 패턴: 매칭 결과 지정하기
match() 또는 search()를 사용할 때 모든 매칭은 m.group()과 같이 객체 m으로부터 결과를 반환한다. 패턴을 괄호로 둘러싸면 매칭은 그 괄호만의 그룹으로 저장된다.
m.groups()를 사용하면 그룹의 튜플을 출력할 수 있다.
```python
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group()) # a dish of fish
print(m.groups()) # ('a dish', 'fish')
```
(?P<name\> expr) 패턴을 사용한다면, 표현식이 매칭되고, 그룹 이름의 매칭이 저장된다.
```python
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group()) # a dish of fish
print(m.groups()) # ('a dish', 'fish')
print(m.group('DISH')) # a dish
print(m.group('FISH')) # fish
```

<br/>

---

# 이진 데이터
이진 데이터를 다루기 위해서는 엔디언(컴퓨터 프로세서가 데이터를 바이트로 나누는 방법)과 정수에 대한 사인 비트가틍ㄴ 개념을 알아야 한다.

### 바이트와 바이트 배열
- 바이트는 바이트의 튜플처럼 불변하다.
- 바이트 배열은 바이트의 리스트처럼 가변이다.
```python
# 리스트의 변수 blist
# 바이트 변수 the_bytes
# 바이트 배열 변수 the_byte_array
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes) # b'\x01\x02\x03\xff'

the_bytes_array = bytearray(blist)
print(the_bytes_array) # bytearray(b'\x01\x02\x03\xff')

print(b'\x61') # b'a'
print(b'\x01abc\xff') # b'\x01abc\xff'
```
다음 예제는 바이트 변수가 불변하다는 것을 보여준다.
```python
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes[1] = 127
# Traceback (most recent call last):
# ~~~
# TypeError: 'bytes' object does not support item assignment
```

바이트 배열 변수는 변경 가능하다.
```python
blist = [1, 2, 3, 255]
the_bytes_array = bytearray(blist)
print(the_bytes_array) # bytearray(b'\x01\x02\x03\xff')

the_bytes_array[1] = 127
print(the_bytes_array) # bytearray(b'\x01\x7f\x03\xff')
```
바이트 혹은 바이트 배열 데이터를 출력할 때, 파이썬은 출력할 수 없는 바이트에 대해서는 \xxx를 사용하고, 출력할 수 있는 바이트에 대해서는 아스키 코드 값을 사용한다.

<br/>

### 이진 데이터 변환하기: struct
파이썬 표준 라이브러리는 C와 C++의 구조체와 유사한, 데이터를 처리하는 struct 모듈이 있다.
struct를 사용하면 이진 데이터를 파이썬 데이터 구조로 바꾸거나 파이썬 데이터 구조를 이진 데이터로 바꿀 수 있다.

<br/>

### 바이트/문자열 변환하기: binascii()
표준 binascii 모듈은 이진 데이터와 다양한 문자열 표현을 서로 변환할 수 있는 함수를 제공한다.

<br/>

### 비트 연산자
파이썬은 C언어와 유사한 비트단위 정수 연산을 제공한다.
> ### 비트단위 정수 연산
|연산자|설명|예제|10진수 결과|2진수 결과|
|---|---|---|---|---|
|&|And|x & y|1|0b0001|
|\||Or|x \| y|5|0b0101|
|^|XOR|x ^ y|4|0b0100|
|~|NOT|~x|-6|정수 크기에 따라 이진 표현이 다름|
|<<|왼쪽 시프트|x << 1|10|0b1010|
|>>|오른쪽 시프트|x >> 1|2|0b0010|

