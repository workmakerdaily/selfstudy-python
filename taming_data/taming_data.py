def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
# value="A", name="LATIN CAPITAL LETTER A", value2="A"

unicode_test('$')
# value="$", name="DOLLAR SIGN", value2="$"

unicode_test('\u00a2')
# value="¢", name="CENT SIGN", value2="¢"

unicode_test('\u20ac')
# value="€", name="EURO SIGN", value2="€"

unicode_test('\u2603')
# value="☃", name="SNOWMAN", value2="☃"

import html.entities
import unicodedata
print(unicodedata.name('\u00e9'))
# LATIN SMALL LETTER E WITH ACUTE

print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')) # é

place = 'caf\u00e9'
print(place) # café

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place) # café

u_umlaut = '\N{LATIN SMALL LETTER E WITH ACUTE}'
print(u_umlaut) # é

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)
# Now I can finally have my Gewérztraminer in a café

print(len('$')) # 1
print(len('\U0001f47b')) # 1

print(chr(233)) # é
print(chr(0xe9)) # é
print(chr(0x1fc6)) # ῆ

### 인코딩
snowman = '\u2603'

print(len(snowman)) # 1

ds = snowman.encode('utf-8')

print(len(ds)) # 3
print(ds) # b'\xe2\x98\x83'

# ds = snowman.encode('ascii')
# Traceback (most recent call last):
# ~~~
# UnicodeEncodeError: 'ascii' codec can't encode 
# character '\u2603' in position 0: ordinal not in range(128)

print(snowman.encode('ascii', 'ignore')) # b''

print(snowman.encode('ascii', 'replace')) # b'?'

print(snowman.encode('ascii', 'backslashreplace')) # b'\\u2603'

print(snowman.encode('ascii', 'xmlcharrefreplace')) # b'&#9731;'

### 디코딩
place = 'caf\u00e9'
print(place) # café
print(type(place)) # <class 'str'>

place_bytes = place.encode('utf-8')
print(place_bytes) # b'caf\xc3\xa9'
print(type(place_bytes)) # <class 'bytes'>

place2 = place_bytes.decode('utf-8')
print(place2) # café

# place3 = place_bytes.decode('ascii')
# Traceback (most recent call last):
# ~~~
# UnicodeDecodeError: 'ascii' codec 
# can't decode byte 0xc3 in position 3: ordinal not in range(128) 

place4 = place_bytes.decode('latin-1')
print(place4) # cafÃ©

place5 = place_bytes.decode('windows-1252')
print(place5) # cafÃ©

### HTML 엔티티
import html
print(html.unescape("&egrave;")) # è

import html
print(html.unescape("&#233;")) # é
print(html.unescape("&#xe9;")) # é

from html.entities import html5
print(html5["egrave"]) # è
print(html5["egrave;"]) # è

import html
char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])
# eacute

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value) # b'caf&#233;'
print(byte_value.decode()) # caf&#233;

### 정규화
eacute1 = 'é' # UTF-8
eacute2 = '\u00e9' # 유니코드 코드 포인트
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}' # 유니코드 이름
eacute4 = chr(233) # 10진수 바이트 값
eacute5 = chr(0xe9) # 16진수 바이트 값

print(eacute1, eacute2, eacute3, eacute4, eacute5)
# é é é é é
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)
# True

import unicodedata
print(unicodedata.name(eacute1))
# LATIN SMALL LETTER E WITH ACUTE
print(ord(eacute1)) # 233
print(0xe9) # 233

eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"

print(eacute_combined1, eacute_combined2, eacute_combined3)
# é é é
print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# True

print(eacute1 == eacute_combined1) # False

import unicodedata
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)

print(len(eacute_normalized)) # 1
print(eacute_normalized == eacute1) # True
print(unicodedata.name(eacute_normalized))
# LATIN SMALL LETTER E WITH ACUTE

# 정규 표현식
import re
result = re.match('You', 'Young Frankenstein')

youpattern = re.compile('You')

result = youpattern.match('Young Frankenstein')

### 시작부터 일치하는 패턴 찾기: match()
import re
source = 'Young Frankenstein'
m = re.match('You', source)

if m:
    print(m.group())
# You

m = re.match('^You', source) # 앵커 시작도 마찬가지이다.
if m:
    print(m.group())
# You

import re
source = 'Young Frankenstein'
m = re.match('Frank', source)
if m:
    print(m.group())
#

import re
source = 'Young Frankenstein'
if m:= re.match('Frank', source):
    print(m.group())
#

import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
    print(m.group())
# Frank

import re
source = 'Young Frankenstein'
m = re.match('.*Frank', source)
if m: # match는 객체를 반환한다.
    print(m.group())
# Young Frank

### 첫 번째 일치하는 패턴 찾기: search()
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m: # search는 객체를 반환한다.
    print(m.group())
# Frank

### 일치하는 모든 패턴 찾기: findall()
import re
source = 'Young Frankenstein'
m = re. findall('n', source)

print(m) # ['n', 'n', 'n', 'n']
print('Found', len(m), 'matches')
# Found 4 matches

import re
source = 'Young Frankenstein'
m = re.findall('n.', source)
print(m) # ['ng', 'nk', 'ns']

import re
source = 'Young Frankenstein'
m = re.findall('n.?', source)
print(m) # ['ng', 'nk', 'ns', 'n']

### 패턴으로 나누기: split()
import re
source = 'Young Frankenstein'
m = re.split('n', source)
# split는 리스트를 반환한다.
print(m) # ['You', 'g Fra', 'ke', 'stei', '']

### 일치하는 패턴 대체하기: sub()
import re
source = 'Young Frankenstein'
m = re.sub('n', '?', source)
# sub는 문자열을 반환한다.
print(m) # You?g Fra?ke?stei?

### 패턴: 특수 문자
import string
printable = string.printable

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

### 패턴: 지정자
source = '''I wish I may, I wish I might
    Have a dish of fish tonight.'''

print(re.findall('wish', source)) # ['wish', 'wish']
print(re.findall('wish|fish', source)) # ['wish', 'wish', 'fish']
print(re.findall('^wish', source)) # []
print(re.findall('^I wish', source)) # ['I wish']
print(re.findall('fish$', source)) # []
print(re.findall('fish tonight.$', source)) # ['fish tonight.']
print(re.findall('fish tonight\.$', source)) # ['fish tonight.']
print(re.findall('[wf]ish', source)) # ['wish', 'wish', 'fish']
print(re.findall('[wsh]+', source)) # ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']
print(re.findall('ght\W', source)) # ['ght\n', 'ght.']
print(re.findall('I (?=wish)', source)) # ['I ', 'I ']
print(re.findall('(?<=I) wish', source)) # [' wish', ' wish']

### 패턴: 매칭 결과 지정하기
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group()) # a dish of fish
print(m.groups()) # ('a dish', 'fish')

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group()) # a dish of fish
print(m.groups()) # ('a dish', 'fish')
print(m.group('DISH')) # a dish
print(m.group('FISH')) # fish

# 이진 데이터
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes) # b'\x01\x02\x03\xff'

the_bytes_array = bytearray(blist)
print(the_bytes_array) # bytearray(b'\x01\x02\x03\xff')

print(b'\x61') # b'a'
print(b'\x01abc\xff') # b'\x01abc\xff'

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
# the_bytes[1] = 127
# Traceback (most recent call last):
# ~~~
# TypeError: 'bytes' object does not support item assignment

blist = [1, 2, 3, 255]
the_bytes_array = bytearray(blist)
print(the_bytes_array) # bytearray(b'\x01\x02\x03\xff')

the_bytes_array[1] = 127
print(the_bytes_array) # bytearray(b'\x01\x7f\x03\xff')