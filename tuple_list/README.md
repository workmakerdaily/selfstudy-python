**튜플**은 불변이다. 항목을 할당하고 나면 바꿀 수 없다.
**리스트**는 가변이다. 항목을 할당하고 나서 자유롭게 수정하거나 삭제할 수 있다.

# 튜플
### 튜플 생성하기:, 그리고()
튜플은 다양한 방법으로 생성할 수 있다.
```python
empty_tuple = ()
print(empty_tuple) # ()
```
한 요소 이상의 튜플을 만들기 위해서는 각 요소 뒤에 콤마( , )를 붙인다.
괄호를 추가하여 쓸 수도 있다.
```python
one_marx = 'Groucho',
print(one_marx) # ('Groucho',)

one_marx = ('Groucho',)
print(one_marx) # ('Groucho',)
```
괄호 안에 한 요소만 있고, 콤마를 생략하면 튜플이 아니라 문자열이 된다.
```python
one_marx = ('Groucho')
print(one_marx) # Groucho
print(type(one_marx)) # <class 'str'>
```
요소가 두 개 이상이면 마지막에는 콤마를 붙이지 않는다.
```python
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple) # ('Groucho', 'Chico', 'Harpo')
print(type(marx_tuple)) # <class 'tuple'>
```
튜플을 출력할 때 괄호를 포함한다.
튜플을 정의할 때는 괄호가 필요 없다.
그러나 값들을 괄호로 묶어서 튜플을 정의한다면, 이것이 튜플인지 구분하기가 더 쉽다.
```python
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple) # ('Groucho', 'Chico', 'Harpo')
```
콤마를 다른 용도(함수, 메서드의 인수 등)로 사용하려면 괄호가 필요하다.
다음 예제는 쉼표만 사용하여 단일 요소를 가진 튜플을 만들수 있지만, 함수에 인수로 전달은 안된다.
```python
one_marx = 'Groucho',
print(type(one_marx)) # <class 'tuple'>
print(type('Groucho',)) # <class 'str'>
print(type(('Groucho',))) # <class 'tuple'>
```

튜플로 한 번에 여러 변수를 할당할 수 있다.
이것을 **튜플 언패킹**이라고 한다.
```python
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a) # Groucho
print(b) # Chico
print(c) # Harpo
```

한 문장에서 값을 교환하기 위해 튜플을 사용할 수 있다.
```python
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password) # tuttifrutti
print(icecream) # swordfish
```

<br/>

### 생성하기: tuple()
tuple() 함수는 다른 객체를 튜플로 만들어준다.
```python
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list)) # ('Groucho', 'Chico', 'Harpo')
```

<br/>

### 결합하기: +
```python
print(('Groucho',) + ('Chico', 'Harpo'))
# ('Groucho', 'Chico', 'Harpo')
```

<br/>

### 항목 복제하기: *
```python
print(('yada',) * 3) # ('yada', 'yada', 'yada')
```

<br/>

### 비교하기
```python
a = (7, 2)
b = (7, 2, 9)
print(a == b) # False
print(a <= b) # True
print(a < b) # True
```

<br/>

### 순회하기: for와 in
```python
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)
# fresh
# out
# of
# ideas
```

<br/>

### 수정하기
튜플은 불변 객체이므로 기존 튜플을 변경할 수 없으며, 문자열과 같이 결합하여 새 튜플을 만들 수 있다.
```python
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2) # ('Fee', 'Fie', 'Foe', 'Flop')
```
튜플을 수정하는 것처럼 보인다.
```python
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1) # ('Fee', 'Fie', 'Foe', 'Flop')
```
그러나 이것은 이전의 t1이 아닌 t1가 t2가 가리키는 원래 튜플에 새로운 튜플을 만들고, 새로운 튜플을 t1에 할당한 것이다.
id() 함수로 확인할 수 있다.
```python
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1)) # 1547252367040

t1 += t2
print(id(t1)) # 1547252246832
```

<br/>

---

# 리스트
리스트는 데이터를 순차적으로 파악하는 데 유용하다. 특히 내용의 순서가 바뀔 수 있다. 또한 리스트의 현재 위치에서 새로운 요소를 추가, 삭제하거나 덮어쓸 수 있다.
또한 동일한 값이 여러 번 나올 수 있다.

### 생성하기: []
리스트는 0 혹은 그 이상의 요소로 만들어진다.
콤마로 구분하며 대괄호로 둘러싸여 있다.
```python
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
# 값이 고유하지 않아도 된다.
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {'groundhog': 'Phil'}, 'Feb. 2']
```

<br/>

### 생성 및 변환하기: list()
list() 함수로 빈 리스트를 만들 수 있다.
```python
another_empty_list = list()
print(another_empty_list) # []
```
list() 함수는 다른 데이터 타입을 리스트로 변환한다.
```python
# 문자열
print(list('cat')) # ['c', 'a', 't']

# 튜플
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple)) # ['ready', 'fire', 'aim']
```

<br/>

### 문자열 분할로 생성하기: split()
split() 메서드는 문자열을 구분자 단위로 분할하여 리스트를 생성한다.
```python
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))
# ['9', '19', '2019']
```

문자열 안에 구분자가 두 개 이상 있다면 리스트 항목으로 빈 문자열을 볼 수 있다.
```python
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
# ['a', 'b', '', 'c', 'd', '', '', 'e']

print(splitme.split('//'))
# ['a/b', 'c/d', '/e']
```

<br/>

### [offset]으로 항목 얻기
리스트는 오프셋으로 특정 값을 추출할 수 있다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0]) # Groucho
print(marxes[1]) # Chico
print(marxes[2]) # Harpo

print(marxes[-1]) # Harpo
print(marxes[-2]) # Chico
print(marxes[-3]) # Groucho
```

<br/>

### 슬라이스로 항목 얻기
슬라이스로 리스트의 서브시퀀스를 추출할 수 있다.
문자열과 마찬가지로 슬라이스에 스텝을 사용할 수 있다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2]) # ['Groucho', 'Chico']
print(marxes[::2]) # ['Groucho', 'Harpo']
print(marxes[::-2]) # ['Harpo', 'Groucho']
print(marxes[::-1]) # ['Harpo', 'Chico', 'Groucho']
```

marxes 리스트 자체를 반대로 뒤집은 상태로 바꾸기 위해 list.reverse() 메서드를 사용한다.
reverse() 메서드는 리스트를 변경하지만 값을 반환하지는 않는다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes) # ['Harpo', 'Chico', 'Groucho']
```
리스트 슬라이스는 문자열 슬라이스와 같이 잘못된 인덱스를 지정할 수 있지만 예외는 발생하지 않는다.
유효범위의 인덱스를 반환하거나 아무것도 반환하지 않는다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:]) # []
print(marxes[-6:]) # ['Groucho', 'Chico', 'Harpo']
print(marxes[-6:-2]) # ['Groucho']
print(marxes[-6:-4]) # []
```

<br/>

### 리스트 끝에 항목 추가하기: append()
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo']
```

<br/>

### 오프셋과 insert()로 항목 추가하기
append() 메서드는 리스트의 끝에 항목을 추가만 하지만
insert() 메서드는 원하는 위치에 항목을 추가할 수 있다.
0은 시작점이며 끝을 넘는 오프셋은 append()처럼 끝에 추가한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes) # ['Groucho', 'Chico', 'Gummo', 'Harpo']

marxes.insert(10, 'Zeppo')
print(marxes) # ['Groucho', 'Chico', 'Gummo', 'Harpo', 'Zeppo']
```

<br/>

### 모든 항목 복제하기: *
```python
print(["blah"] * 3) # ['blah', 'blah', 'blah']
```

<br/>

### 리스트 병합하기: extend()와 +
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
```

+나 +=로 병합할 수 있다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
```

append()를 사용하면 항목을 병합하지 않고 others가 하나의 리스트로 추가된다.
리스트는 다른 타입의 요소를 포함할 수 있다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]
```

<br/>

### [offset]으로 항목 바꾸기
리스트 오프셋은 리스트에서 유효한 위치여야 한다.
문자열은 불변 객체이지만 리스트는 가변 객체이다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes) # ['Groucho', 'Chico', 'Wanda']
```

<br/>

### 슬라이스로 항목 바꾸기
슬라이스는 하위 리스트에 값을 할당할 수 있다.
```python
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers) # [1, 8, 9, 4]
```

리스트에 할당되는 오른쪽 값의 수는 왼쪽 슬라이스 항목 수와 달라도 된다.
```python
numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers) # [1, 7, 8, 9, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers) # [1, 4]
```

오른쪽 값은 리스트가 아닌 순회 가능한 타입 값을 리스트 항목에 할당할 수 있다.
```python
numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers) # [1, 98, 99, 100, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers) # [1, 'w', 'a', 't', '?', 4]
```

<br/>

### 오프셋으로 항목 삭제하기: del
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Gummo']
```
오프셋으로 리스트의 특정 항목을 삭제하면, 제거된 항목 이후의 항목들이 한 칸씩 앞당겨지며 리스트의 길이가 1씩 감소한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes) # ['Groucho', 'Harpo', 'Gummo']
```

<br/>

### 값으로 항목 삭제하기: remove()
삭제할 항목의 위치를 모른다면 값과 remove()로 그 항목을 삭제할 수 있다.
만약 값이 중복된다면 첫 번째 항목만 삭제한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes) # ['Chico', 'Harpo']
```

<br/>

### 오프셋으로 항목을 얻은 후 삭제하기: pop()
pop()은 리스트에서 항목을 가져오는 동시에 그 항목을 삭제한다.
pop()과 그 인수로 오프셋을 호출했다면, 해당 오프셋의 항목이 반환된다.
인수가 없다면 기본값은 -1이다.
pop(0)은 리스트의 시작을, pop()이나 pop(-1)은 리스트의 끝을 반환한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop()) # Zeppo
print(marxes) # ['Groucho', 'Chico', 'Harpo']
print(marxes.pop(1)) # Chico
print(marxes) # ['Groucho', 'Harpo']
```

<br/>

### 모든 항목 삭제하기: clear()
모든 항목을 지우는 메서드이다.
```python
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
work_quotes.clear()
print(work_quotes) # []
```

<br/>

### 값으로 오프셋 찾기: index()
리스트 항목 값의 오프셋을 알고 싶을 떄 사용한다.
리스트에 같은 값이 2개 이상이면 첫 번째 오프셋만 반환한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico')) # 1
```

<br/>

### 존재여부 확인하기: in
같은 값이 여러 개 존재할 때 리스트에 적어도 값이 하나 존재하면 in은 True를 반환한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes) # True
print('Bob' in marxes) # False
```

<br/>

### 값 세기: count()
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo')) # 1
print(marxes.count('Bob')) # 0

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger')) # 3
```

<br/>

### 문자열로 변환하기: join()
join()은 문자열 메서드지, 리스트 메서드가 아니므로 marxes.join(', ')으로 사용할 수 없다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes)) # Groucho, Chico, Harpo
```
join()을 split()의 **반대**라고 생각하면 기억하기 쉬울 것이다.
```python
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined) # Harry * Hermione * Ron

separated = joined.split(separator)
print(separated) # ['Harry', 'Hermione', 'Ron']

print(separated == friends) # True
```

<br/>

### 정렬하기: sort()와 sorted()
- sort()는 리스트 자체를 내부적으로 정렬한다.
- sorted()는 리스트의 정렬된 복사본을 반환한다.
리스트의 항목이 숫자라면 오름차순으로, 문자열이면 알파벳순으로 정렬한다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)

# sorted_marxes는 복사본이므로 원본 리스트는 변하지 않는다.
print(sorted_marxes) # ['Chico', 'Groucho', 'Harpo']
print(marxes) # ['Groucho', 'Chico', 'Harpo']

# sort()는 marxes를 정렬된 marxes로 바꾼다.
marxes.sort()
print(marxes) # ['Chico', 'Groucho', 'Harpo']
```

리스트의 요소들이 모두 같은 타입이면 sort()는 제대로 동작한다.
정수와 부동소수점 숫자 같이 혼합된 타입도 정렬할 수 있다.
```python
numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4.0]
```

내림차순으로 정렬하고 싶다면 인수어 reverse=True를 추가하면 된다.
```python
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers) # [4.0, 3, 2, 1]
```

<br/>

### 항목 개수 얻기: len()
```python
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes)) # 3
```

<br/>

### 할당하기: =
한 리스트를 변수 두 곳에 할당했을 때, 한 리스트를 변경하면 다른 리스트도 같이 변경된다.
```python
a = [1, 2, 3]
print(a) # [1, 2, 3]

b = a
print(b) # [1, 2, 3]

a[0] = 'surprise'
print(a) # ['surprise', 2, 3]
print(b) # ['surprise', 2, 3]
```
a 또는 b 리스트 내용을 변경하면 두 변수 모두에 반영된다.
```python
b[0] = 'I hate surprises'
print(b) # ['I hate surprises', 2, 3]
print(a) # ['I hate surprises', 2, 3]
```

<br/>

### 복사하기: copy(), list(), 슬라이스
원본 리스트 a가 있다. copy()로 리스트 b를 만든다.
list() 변환 함수로 리스트 c를 만든다.
그리고 a를 슬라이스해서 리스트 d를 만든다.
```python
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
```
복사본 c, b, d를 바꾸더라도 원본 a에는 아무런 영향을 주지 않는다.
```python
a[0] = 'integer lists are boring'
print(a) # ['integer lists are boring', 2, 3]
print(b) # [1, 2, 3]
print(c) # [1, 2, 3]
print(d) # [1, 2, 3]
```

<br/>

### 깊은 복사: deepcopy()
리스트 값이 모둔 불변이면 copy() 메서드는 제대로 작동한다.
리스트, 튜플, 딕셔너리와 같은 가변 객체는 참조일 뿐이다.
원본과 사본의 변경 사항을 모두 반영한다.
```python
a = [1, 2, [8,9]]
b = a.copy()
c = list(a)
d = a[:]
print(a) # [1, 2, [8, 9]]
print(b) # [1, 2, [8, 9]]
print(c) # [1, 2, [8, 9]]
print(d) # [1, 2, [8, 9]]

a[2][1] = 10
print(a) # [1, 2, [8, 10]]
print(b) # [1, 2, [8, 10]]
print(c) # [1, 2, [8, 10]]
print(d) # [1, 2, [8, 10]]
```
a[2]의 값이 리스트이며, 해당 항목을 변경할 수 있다.
위에서는 **얕은 복사**를 사용했다.

이 문제를 해결하기 위해서 **깊은 복사**를 수행하는 deepcopy() 메서드를 사용한다.
```python
import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a) # [1, 2, [8, 9]]
print(b) # [1, 2, [8, 9]]

a[2][1] = 10
print(a) # [1, 2, [8, 10]]
print(b) # [1, 2, [8, 9]]
```
deepcopy()는 하위에 중첩된 리스트, 딕셔너리, 기타 다른 객체를 모두 복사한다.

<br/>

### 리스트 비교
비교연산자는 두 리스트의 같은 위치의 오프셋 항목을 비교한다.
리스트 a가 리스트 b보다 길이가 짧고, 모든 요소가 같으면 a는 b보다 작다.
```python
a = [7, 2]
b = [7, 2, 9]
print(a == b) # False
print(a <= b) # True
print(a < b)  # True

a = [3, 2]
b = [1, 2, 3]
print(a > b) # True
```

<br/>

### 순회하기: for와 in
```python
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
# brie
# gjetost
# havarti
```
break 문은 for문을 종료하고, continue 문은 다음 순회 단계로 넘어간다.
```python
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
# brie
# I won't eat anything that starts with 'g'
```
for문이 break 문 없이 완료됐다면 다음과 같이 else 문을 사용할 수 있다.
```python
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'") 
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")
# brie
# gjetost
# havarti
# Didn't find anything that started with 'x'
```
in 문의 리스트에 항목이 없어서 for 문이 실행되지 않을 때도 else 문이 실행된다.
```python
cheeses = []
for cheese in cheeses:
    print('This shop has some lobely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')
# This is not much of a cheese shop, is it?
```

<br/>

### 여러 시퀀스 순회하기: zip()
여러 시퀀스 중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다
```python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
# Monday : drink coffee - eat banana - enjoy tiramisu
# Tuesday : drink tea - eat orange - enjoy ice cream
# Wednesday : drink beer - eat peach - enjoy pie
```

두개의 튜블을 만들기 위해 zip()을 사용한다.
zip()에 의해 반환되는 값은 튜플이나 리스트 자신이 아니라 하나로 반환될 수 있는 순회 가능한 값이다.
```python
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list( zip(english,french) ))
# [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
```
zip()의 결과를 dict()에 넣으면 작은 영어-프랑스어 사전이 생성된다.
```python
print(dict( zip(english, french) ))
# {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}
```

<br/>

### 리스트 컴프리헨션
1부터 5까지 정수 리스트를 한 번에 하나씩 만들 수 있다.
```python
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list) # [1, 2, 3, 4, 5]
```
또한 이터레이터와 range() 함수를 사용하여 만들 수 있다.
```python
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)
# [1, 2, 3, 4, 5]
```
또 리스트에 직접 range()를 넣어서 결과를 반환할 수 있다.
```python
number_list = list(range(1, 6))
print(number_list) # [1, 2, 3, 4, 5]
```
위 모두 동일한 결과를 생성하지만
**리스트 컴프리헨션**을 사용해서 리스트를 만드는 것이 조금 더 파이써닉한 방법이다.
```python
[표현식 for 항목 in 순회 가능학 객체]
```

```python
number_list = [number for number in range(1, 6)]
print(number_list) # [1, 2, 3, 4, 5]
```
리스트 값을 생성하는 첫 번째 number 변수가 필요하다.
이것은 순회 결과를 number_list 변수에 넣어준다.
두 번쨰 number 변수는 for 문의 일부다.
```python
number_list = [number-1 for number in range(1, 6)]
print(number_list) # [0, 1, 2, 3, 4]
```
리스트 컴프리헨션은 조건 표현식을 포함할 수 있다.
```python
[표현식 for 항목 in 순회 가능한 객체 if 조건]
```
```python
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list) # [1, 3, 5]
```
컴프리헨션이 지금까지 사용했던 방식보다 좀 더 단순하면서 강력하다.
```python
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list) # [1, 3, 5]
```

일반적인 중첩 루프를 사용해서 결과를 출력해보았다.
```python
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
```
컴프리헨션을 사용해보았다.
```python
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
# (1, 1)
# (1, 2)
# (2, 1)
# (2, 2)
# (3, 1)
# (3, 2)
```
cells 리스트를 순회한 것처럼, 각 튜플로부터 row와 col의 값만 출력하기 위해
**튜플 언패킹**을 할 수 있다.
```python
for row, col in cells:
    print(row, col)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
```

<br/>

### 리스트의 리스트
리스트는 리스트뿐만 아니라 다른 타입의 요소도 포함할 수 있다. 
```python
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds[0]) # ['hummingbird', 'finch']
print(all_birds[1]) # ['dodo', 'passenger pigeon', 'Norwegian Blue']
print(all_birds[1][0]) # dodo
```

<br/>

---

# 튜플 vs 리스트
튜플은 리스트의 append(), insert() 등과 같은 함수가 없고, 생성한 후에는 수정할 수 없어서 함수의 수가 매우 적다.
그럼에도 튜플을 사용하는 이유는
- 더 적은 공간을 사용한다.
- 실수로 항목이 손상될 염려가 없다.
- 딕셔너리 키로 사용할 수 있다.
- 네임드튜플은 객체의 단순한 대안이 될 수 있다.

일반적으로는 리스트와 딕셔너리를 많이 사용한다.

<br/>

---
# 튜플 컴프리헨션은 없다
가변 타입(리스트, 딕셔너리 및 셋)에는 컴프리헨션이 있지만
문자열과 튜플과 같은 불변 타입은 다른 방법으로 만들어져야 한다.
```python
number_thing = (number for number in range(1, 6))
```
위 코드는 예외를 발생하지 않아 정상적으로 작동하는 것처럼 보인다.
그러나 () 안에 있는 것은 **제너레이터 컴프리헨션**으로 완전히 다른 것이다.
**제너레이터 객체**를 반환한다.
```python
print(type(number_thing)) # <class 'generator'>
```










