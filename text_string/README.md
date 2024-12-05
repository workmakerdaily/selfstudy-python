# 따옴표로 문자열 생성
작은따옴표( ' )와 큰 따옴표( " )로 문자열을 만들 수 있다.
파이썬은 작은따옴표와 큰따옴표를 똑같이 처리한다.
```python
'Snap'
"Crackle"
```
작은따옴표의 문자열을 큰따옴표에 넣거나, 큰따옴표의 문자열을 작은따옴표에 넣을 수 있다.
```python
print("'Nay!' said the naysayer. 'Neigh?' said the horse.")
# 'Nay!' said the naysayer. 'Neigh?' said the horse.
```
세 개의 작은따옴표나 큰따옴표를 사용할 수 있다.
```python
print('''Boom!''') # Boom!
print("""Eek!""") # Eek!
```
세 개의 작은따옴표는 짧은 문자열에서 유용하지 안핟.
여러 줄의 문자열에서 유용하게 쓰인다.
```python
poem = '''There was a Young Lady of Norway,
    Who casually sat in a doorway;
    When the door squeezed her flat,
    She exclaimed, "What of that?"
    This courageous Young Lady of Norway.'''
print(poem)
# There was a Young Lady of Norway,
#     Who casually sat in a doorway;
#     When the door squeezed her flat,
#     She exclaimed, "What of that?"
#     This courageous Young Lady of Norway.
```
세 개의 작은따옴표가 아닌 그냥 작은 따옴표를 사용하면 에러가 발생한다
```python
poem = 'There was a young lady of Norway,
# SyntaxError: unterminated string literal (detected at line 19)
```
세 개의 작은 따옴표 안에 여러 줄이 있다면, 문자열 끝에 들어 있는 라인 끝 문자가 보존된다. 또한 양쪽 끝의 공백 또한 보존된다.

print()는 문자열에서 따옴표를 제거한 뒤 내용을 출력한다.
```python
print('Give', "us", '''some''', """space""") # Give us some space
```

<br/>

---

# 문자열 타입으로 변환: str()
str() 함수를 사용하여 다른 데이터 타입을 문자열로 변환할 수 있다.
```python
print(type(str(98.6))) # <class 'str'>
```

<br/>

---

# 이스케이프 문자: \
문자 앞에 백슬래시(\\) 기호를 붙임으로써 특별한 의미를 줄 수 있다.
가장 일반적으로준 줄바꿈을 의미하는 \n이다.
```python
palindrome = 'A man, \nA plan, \nA canal:\nPanama'
print(palindrome)
# A man,
# A plan,
# A canal:
# Panama
```
\t는 tap을 의미하며 텍스트의 공백에 사용된다.
```python
print('\tabc') #         abc
print('a\tbc') # a       bc
print('ab\tc') # ab      c
```

문자열에서 \' 혹은 \"을 사용하여 작은따옴표나 큰따옴표를 표현할 수 있다.
```python
testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony) # "I did nothing!" he said. "Or that other thing."
```
백슬래시를 입력하고 싶으면 백슬래시를 두 번 입력하면 된다.
```python
speech = 'The backslash (\\) bends over backwards to please you.'
print(speech) # The backslash (\) bends over backwards to please you.
```

원시 문자열은 이스케이프 문자를 무효화 한다.
```python
info = r'Type a \n to get a new line in a normal string'
print(info) # Type a \n to get a new line in a normal string

poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
print(poem)
# Boys and girls, come out to play.
# The moon doth shine as bright as day.
```

<br/>

---

# 결합하기: +
+ 연산자를 사용하여 리터럴 문자열 또는 문자열 변수를 결합할 수 있다.
```python
print('Release the kraken! ' + 'No, wait!')
# Release the kraken! No, wait!
```
괄호로 묶어 여러 줄에 걸쳐 문자열을 출력할 수 있다.
```python
vowels = ('a'
        "e" '''i'''
        'o' """u""")
print(vowels) # aeiou
```
파이썬은 문자열을 결합할 때 공백을 자동으로 붙이지 않는다.
print()는 각 인수 사이에 공백을 붙인다.

<br/>

---

# 복제하기: *
* 연산자를 사용하여 문자열을 복제할 수 있다.
```python
start = 'Na ' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
# Na Na Na Na
# Na Na Na Na
# HeyHeyHey
# Goodbye.
```

<br/>

---

# 문자 추출: []
문자열에서 한 문자를 얻기 위해서는 문자열 이름 뒤에 대괄호([])와 오프셋을 지정한다.
가장 왼쪽의 오프셋은 0이고 가장 오른쪽의 오프셋은 -1이다.
```python
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0]) # a
print(letters[1]) # b
print(letters[-1]) # z
print(letters[-2]) # y
```
오프셋을 문자열의 길이 그 이상으로 지정하면 예외를 얻는다.
```python
print(letters[100])
# IndexError: string index out of range
```

문자열은 불변하기 때문에 특정 인덱스에 문자를 삽입하거나 변경할 수 없다.
```python
name = 'Henny'
name[0] = 'P'
# TypeError: 'str' object does not support item assignment
```

replace()나 슬라이스와 같은 문자열 함수를 사용할 수 있다.
```python
name = 'Henny'
print(name.replace('H', 'P')) # Penny
print('P' + name[1:]) # Penny
print(name) # Henny
```
name에 저장된 값은 바뀌지 않는다.

<br/>

---

# 슬라이스로 부분 문자열 추출
슬라이스를 사용하여 한 문자열에서 문자열의 일부를 추출할 수 있다.
대골호를 사용하여 시작(start) 오프셋, 끝(end) 오프셋, 옵션으로 스텝(step)을 명시하여 슬라이스를 정의한다.
- [:] : 처음부터 끝까지 전체 시퀀스를 추출
- [start :] : start 오프셋부터 끝까지 시퀀스를 추출한다.
- [: end] : 처음부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
- [start : end] : start 오프셋부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
- [start : end : step] step 만큼 문자를 건너뛰면서, start 오프셋부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
```python
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:]) # abcdefghijklmnopqrstuvwxyz
print(letters[20:]) # uvwxyz
print(letters[10:]) # klmnopqrstuvwxyz
print(letters[12:15]) # mno
print(letters[-3:]) # xyz
print(letters[18:-3]) # stuvw
print(letters[-6:-2]) # uvwx
print(letters[::7]) # ahov
print(letters[4:20:3]) # ehknqt
print(letters[19::4]) # tx
print(letters[:21:5]) # afkpu
print(letters[-1::-1]) # zyxwvutsrqponmlkjihgfedcba
print(letters[::-1]) # zyxwvutsrqponmlkjihgfedcba
print(letters[-50:]) # abcdefghijklmnopqrstuvwxyz
print(letters[-51:-50]) # ''
print(letters[:70]) # abcdefghijklmnopqrstuvwxyz
print(letters[70:71]) # ''
```

<br/>

---

# 문자열 길이: len()
len() 함수는 문자열의 길이를 센다.
```python
print(len(letters)) # 26

empty = ''
print(len(empty)) # 0
```

<br/>

---

# 문자열 나누기: split()
어떤 구분자를 기준으로 하나의 문자열을 작은 문자열들의 리스트로 나누기 위해서는 문자열 내장 함수 split()을 사용한다.
```python
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
# ['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']
```
구분자를 지정하지 않으면 split()는 문자열에 등장하는 공백 문자(줄바꿈, 스페이스, 탭)를 사용한다.
```python
print(tasks.split())
# ['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']
```

<br/>

---

# 문자열 결합하기: join()
join() 메서드는 split() 메서드와 반대로 문자열 리스트를 하나의 문자열로 결합한다.
```python
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
# Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster
```

<br/>

---

# 문자열 대체하기: replace()
문자열 일부룰 대체하기 위해서는 replace() 메서드를 사용한다.
인수로 바꿀 문자열, 대체할 새 문자열, 바꿀 문자열에 대한 횟수를 입력한다.
원본 문자열은 수정하지 않고 변경된 문자열을 반환한다.
마지막 인수를 생략하면 모든 인스턴스를 바꾼다.
```python
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
# a marmoset goes into a bar...

print(setup.replace('a ', 'a famous ', 100))
# a famous duck goes into a famous bar...
```
대체하고 싶은 정확한 문자열을 안다면 replace() 메서드가 적합하다.


<br/>

---
# 문자열 스트립: strip()
strip() 메서드에 인수가 없다면 양쪽 끝의 공백 문자('', '\t', '\n')를 제거한다.
lstrip()는 왼쪽 끝을, rstrip() 메서드는 오른쪽 끝만 제거한다.
```python
world = " earth "
print(world.strip()) # 'earth'
print(world.strip(' ')) # 'earth'
print(world.lstrip()) # 'earth '
print(world.rstrip()) # ' earth'
```

strip() 메서드에 해당하는 인수가 없다면 아무 일도 일어나지 않는다.
```python
print(world.strip('!')) # ' earth '
```

strip() 메서드에 아무 인수가 없거나, 단일 문자 또는 여러 문자의 인수를 ㅟ해서 해당 문자열을 제거할 수 있다.
```python
blurt = "What the...!!?"
print(blurt.strip('.?!')) # What the
```

<br/>

---

# 검색과 선택
```python
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13]) # All that doth
print(len(poem)) # 250
print(poem.startswith('All')) # True
print(poem.endswith('That\'s all, folks!')) # False
```
### find(), index()
문자열에서 부분 문자열 오프셋을 찾기 위한 두 개의 메서드 find(), index()가 있다.
두 메서드 모두 부분 문자열을 찾았을 때 같은 결과를 반환한다.
그러나 찾기 못한다면 find() 메서드는 -1을, index() 메서드는 예외가 발생한다.
문자열의 끝에서 부분 문자열을 찾을때는 r을 붙인다.
```python
word = 'the'
print(poem.find(word)) # 73
print(poem.index(word)) # 73

print(poem.rfind(word)) # 214
print(poem.rindex(word)) # 214

# 부분 문자열이 없을 경우
word = "duck"
print(poem.find(word)) # -1
print(poem.index(word)) # ValueError: substring not found
```

### count()
부분 문자열이 몇개가 있는지 찾고 싶을 떄 사용한다.
```python
word = 'the'
print(poem.count(word)) # 3
```

### isalnum()
시의 모든 문자는 알파벳 또는 숫자로 이루어져 있는지 궁금할 경우에 사용한다.
```python
print(poem.isalnum()) # False
```

<br/>

---
# 대소 문자
```python
setup = 'a duck goes into a bar...'
```
### capitalize()
첫 번째 단어를 대문자로 만든다.
```python
print(setup.capitalize()) # A duck goes into a bar...
```

### title()
모든 단어의 첫 글자를 대문자로 만든다.
```python
print(setup.title()) # A Duck Goes Into A Bar...
```

### upper()
글자를 모두 대문자로 만든다.
```python
print(setup.upper()) # A DUCK GOES INTO A BAR...
```

### lower()
글자를 모두 소문자로 만든다.
```python
print(setup.lower()) # a duck goes into a bar...
```

### swapcase()
소문자는 대문자로, 대문자는 소문자로 만든다.
```python
print(setup.swapcase()) # A DUCK GOES INTO A BAR...
```

<br/>

---

# 정렬
### center()
지정한 공간에서 문자열을 중앙 정렬을 한다.
```python
print(setup.center(30)) # '  a duck goes into a bar...   '
```

### ljust()
지정한 공간에서 왼쪽 정렬을 한다.
```python
print(setup.ljust(30))  # 'a duck goes into a bar...     '
```

### rjust()
지정한 공간에서 오른쪽 정렬을 한다.
```python
print(setup.rjust(30))  # '     a duck goes into a bar...'
```

<br/>

---

# 포매팅
포매팅을 사용해서 보고서나 특정 양식 등의 출력을 생성할 수 있다.

> ### 문자열 포매팅
- 옛 스타일 (파이썬 2, 3에서 지원)
- 새 스타일 (파이썬 2.6 이상에서만 지원)
- f-문자열 (파이썬 3.6 이상에서만 지원)

### 옛 스타일: %
format_string % data 형식이다.
포맷 문자열 안에 끼워 넣을 데이터를 표시하는 형식은 보간 시퀀스다.

|||
|---|---|
|%s|문자열|
|%d|10진수|
|%x|16진수|
|%o|8진수|
|%f|10진 부동소수점|
|%e|지수로 나타낸 부동소수점|
|%g|10진 부동소수점 혹은 지수로 나타낸 부동소수점|
|%%|리터럴 %|

모든 데이터 타입에 %s를 사용할 수 있고 추가 공백 없이 문자열로 지정한다.
```python
print('%s' % 42) # 42
print('%d' % 42) # 42
print('%x' % 42) # 2a
print('%o' % 42) # 52

print(type('%s' % 42)) # <class 'str'>
print(type('%d' % 42)) # <class 'str'>
print(type('%x' % 42)) # <class 'str'>
print(type('%o' % 42)) # <class 'str'>
```
부동소수점에 관한 예제이다.
```python
print('%s' % 7.03) # 7.03
print('%f' % 7.03) # 7.030000
print('%e' % 7.03) # 7.030000e+00
print('%g' % 7.03) # 7.03
```

정수와 리터럴 %에 대한 예제이다.
```python
print('%d%%' % 100) # 100%
```

다음은 정수와 문자열 보간에 대한 예제이다.
문자열 내의 %s는 다른 문자열을 끼워 넣는 것을 의미한다.
문자열 안의 % 수는 % 뒤의 데이터 항목의 수와 일치해야 한다.
```python
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
# My wife's favorite actor is Richard Gere

print("Our cat %s weighs %s pounds" % (cat, weight))
# Our cat Chester weighs 28 pounds
# weight는 정수임에도 문자열 안의 %s는 문자열로 변환한다.
```

> ### 옛 스타일의 사용방법
- 초기 '%' 문자
- 정렬 문자(옵션) : '+' 또는 아무것도 없으면 오른쪽 정렬을 의미하고, '-'는 왼쪽 정렬을 의미한다.
- 최소 너비(옵션)
- '.' 문자(옵션) : 최소 너비 및 최대 문자를 구분한다.
- 최대 문자(옵션) : 변환 타입이 s인 경우 데이터 값에서 출력할 문자열 수를 나타낸다. 변환 타입이 f인 경우, 정밀도를 지정한다.

```python
thing = 'woodchuck'
print('%s' % thing) # 'woodchuck'
print('%12s' % thing)  # '   woodchuck'
print('%+12s' % thing) # '   woodchuck'
print('%-12s' % thing) # 'woodchuck   '
print('%12.3s' % thing)  # '         woo'
print('%-12.3s' % thing) # 'woo         '
```

부동소수점 수 포매팅 %f 예제이다.
```python
thing = 98.6
print('%f' % thing) # '98.600000'
print('%12f' % thing)  # '   98.600000'
print('%+12f' % thing) # '  +98.600000'
print('%-12f' % thing) # '98.600000   '
print('%.3f' % thing) # '98.600'
print('%12.3f' % thing)  # '      98.600'
print('%-12.3f' % thing) # '98.600      '
```

부동소수점 수 포매팅 %d 예제이다.
```python
thing = 9876
print('%d' % thing) # '9876'
print('%12d' % thing)  # '        9876'
print('%+12d' % thing) # '       +9876'
print('%-12d' % thing) # '9876        '
print('%.3d' % thing) # '9876'
print('%12.3d' % thing)  # '        9876'
print('%-12.3d' % thing) # '9876        '
```
정수의 경우 %+12d는 부호를 강제로 출력하며, .3이 있는 포맷 문자열은 부동소수점과 달리 아무 일도 하지 않는다.

### 새 스타일: {}, format()
새 스타일 포매팅은 format_string.format(data) 형식이다.
```python
thing = 'woodchuck'
print('{}'.format(thing)) # 'woodchuck'
```

format() 메서드의 인수는 포맷 문자열 내의 {} 순서대로 나타낸다.
위치별로 인수를 지정할 수 있다.
```python
thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))
# The woodchuck is in the lake.
print('The {1} is in the {0}.'.format(thing, place))
# The lake is in the woodchuck.
```
format()에서 인수를 명명하여 사용할 수 있다.
```python
print('The {thing} is in the {place}.'.format(thing='duck', place='bathtub'))
# The duck is in the bathtub.
```

딕셔너리로도 사용할 수 있다.
```python
d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))
# The duck is in the bathtub.
```

> ### 새 스타일의 사용방법
- 맨 처음 콜론(:)이 온다.
- 채우기 문자(옵션) : 문자열이 최소 너비보다 짧은 경우, 이 문자로 채운다(기본값 ' ').
- 선택적 정렬 문자(옵션) : 왼쪽 정렬이 기본값이다. '<'는 왼쪽 정렬, '>'는 오른쪽 정렬, '^'는 가운데 정렬이다.
- 숫자에 대한 부호 문자(옵션) : 기본값으로 음수에만 부호('-')가 붙는다. '-'는 음수에 부호가 붙고, 양수에 공백(' ')을 붙인다.
- 최소 너비(옵션) : 최소 너비 및 최대 문자를 구분한다.
- 최대 문자(옵션)
-변환 타입

```python
thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
# 'The wraith is at the window'
print('The {:10s} is at the {:10s}'.format(thing, place))
# 'The wraith     is at the window    '
print('The {:<10s} is at the {:<10s}'.format(thing, place))
# 'The wraith     is at the window    '
print('The {:^10s} is at the {:^10s}'.format(thing, place))
# 'The   wraith   is at the   window  '
print('The {:>10s} is at the {:>10s}'.format(thing, place))
# 'The     wraith is at the     window'
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))
# 'The !!wraith!! is at the !!window!!'
```

### 최신 스타일: f-문자열
- 첫 인용 부호 앞에 문자 f 또는 F를 입력한다.
- 변수 이름이나 식을 중괄호 안에 포함해 값을 문자열로 가져온다.

```python
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
# The wereduck is in the werepond
```
중괄호 안에 표현식 사용이 가능하다.
```python
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
# The Wereduck is in the             werepond
```

':' 다음에 새 스타일의 포매팅과 같은 언어(너비, 패딩, 정렬)를 사용할 수 있다.
```python
print(f'The {thing:>20} is in the {place:.^20}')
# The             wereduck is in the ......werepond......
```

이름과 값을 쉽게 출력할 수 있다.
이름 뒤에 = 문자를 붙여서 사용한다.
```python
print(f'{thing =}, {place =}')
# thing ='wereduck', place ='werepond'
```

이름은 표현식이 될 수 있다.
```python
print(f'{thing[-4:] =}, {place.title() =}')
# thing[-4:] ='duck', place.title() ='Werepond'
```

= 다음에 : 및 너비, 정렬과 같은 포매팅 인수를 사용할 수 있다.
```python
print(f'{thing = :>4.4}') # thing = were
```









