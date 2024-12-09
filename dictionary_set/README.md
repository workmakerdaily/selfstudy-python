# 딕셔너리
**딕셔너리**는 리스트와 비슷하다.
차이는 항목의 순서를 따지지 않으며, 0 또는 1과 같은 오프셋으로 항목을 선택할 수 없다.
대신 값에 상응하는 고유한 **키**를 지정한다.
**키**는 불변하는 어떤 타입(불리언, 정수, 부동소수점, 튜플, 문자열 등)이 될 수 있다.
딕셔너리는 변경이 가능하다.

### 생성하기: {}
중괄호 안에 콤마로 구분한 키:값 쌍을 지정한다.
```python
empty_dict = {}
print(empty_dict) # {}

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The king of fortune that never misses",
}
print(bierce)
# {'day': 'A period of twenty-four hours, mostly misspent', 
# 'positive': "Mistaken at the top of one's voice", 
# 'misfortune': 'The king of fortune that never misses'}
```

<br/>

### 생성하기: dict()
명명된 인수와 값을 dict() 함수에 전달하여 딕셔너리를 생성할 수 있다.
```python
# 일반적인 방법
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
# {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}

# dict() 함수 사용 방법
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)
# {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
```
두 번째 방법의 제약 사항은 인수 이름이 유효한 변수(공백과 예약어가 없는) 이름이어야 한다.
```python
x = dict(name="Elmer", def="hunter")
print(x) # SyntaxError: invalid syntax
```

<br/>

### 변환하기: dict()
dict() 함수를 사용하여 두 값으로 이루어진 시퀀스를 딕셔너리로 변환할 수 있다.
각 시퀀스의 첫 번째 항목은 키로, 두 번째 항목은 값으로 사용된다.

두 항목의 리스트로 구성된 리스트를 딕셔너리로 변환하는 예제이다.
```python
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))
# {'a': 'b', 'c': 'd', 'e': 'f'}
```
두 항목으로 구성된 시퀀스를 딕셔너리로 변환할 수 있다.
```python
lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))
# {'a': 'b', 'c': 'd', 'e': 'f'}
```

두 항목의 리스트로 구성된 튜플이다.
```python
tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(tol))
# {'a': 'b', 'c': 'd', 'e': 'f'}
```
두 문자열로 구성된 리스트다.
```python
los = [ 'ab', 'cd', 'ef' ]
print(dict(los))
# {'a': 'b', 'c': 'd', 'e': 'f'}
```
두 문자열로 구성된 튜플이다.
```python
tos = ('ab', 'cd', 'ef')
print(dict(tos))
# {'a': 'b', 'c': 'd', 'e': 'f'}
```

<br/>

### 항목 추가/변경: [key]
딕셔너리에 항목을 추가하는 방법은 키에 참조되는 항목에 값을 할당하면 된다.
딕셔너리에 존재하는 키라면 그 값은 새 값으로 대체된다.
키가 존재하지 않는다면 새 값과 키가 추가된다.
```python
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}

pythons['Gilliam'] = 'Gerry'
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 
# 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Gerry'}

pythons['Gilliam'] = 'Terry'
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 
# 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}
```

딕셔너리의 키들은 반드시 고유해야 한다.
같은 키를 두 번 이상 사용하면 마지막 값으로 저장된다.
```python
some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}

print(some_pythons)
# {'Graham': 'Chapman', 'John': 'Cleese', 
# 'Eric': 'Idle', 'Terry': 'Jones', 'Michael': 'Palin'}
```

<br/>


### 항목 얻기: [key]와 get()
딕셔너리의 가장 일반적인 용도로 키를 지정하여 상응하는 값을 얻는다.
```python
### 항목 얻기: [key]와 get()
print(some_pythons['John']) # Cleese
```
키가 없으면 예외가 발생한다.
```python
print(some_pythons['Groucho'])
# KeyError: 'Groucho'
```
이 문제를 피하는 첫 번째 방법은 in으로 키에 대한 멤버십 테스트를 실행하는 것이다.
```python
print('Groucho' in some_pythons) # False
```
두 번째 방법은 get() 함수를 사용하는 것이다.
이 함수는 딕셔너리, 키, 옵션값을 사용한다.
```python
print(some_pythons.get('John')) # Cleese
```

키가 존재하지 않으면, 옵션값을 지정해서 이를 출력할 수 있다.
```python
print(some_pythons.get('Groucho', 'Not a Python'))
# Not a Python
```
옵션값을 지정하지 않으면 None을 얻는다.

<br/>

### 모든 키 얻기: keys()
```python
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
# dict_keys(['green', 'yellow', 'red'])
```
파이썬 3에서는 list()를 호출해서 dict_keys 객체를 리스트로 변환할 수 있다.
```python
print(list( signals.keys() ))
# ['green', 'yellow', 'red']
```

<br/>

### 모든 값 얻기: values()
```python
print(list( signals.values() ))
# ['go', 'go faster', 'smile for the camera']
```

<br/>

### 모든 키-값 얻기: items()
```python
print(list( signals.items() ))
# [('green', 'go'), ('yellow', 'go faster'), ('red', 'smile for the camera')]
```

<br/>

### 길이 얻기: len()
```python
print(len(signals)) # 3
```

<br/>

### 결합하기: {**a, **b}
파이썬 3.5부터는 **를 사용하여 딕셔너리를 결합할 수 있다.
```python
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})
# {'a': 'agony', 'b': 'bagels', 'c': 'candy'}

third = {'d': 'donuts'}
print({**first, **second, **third})
# {'a': 'agony', 'b': 'bagels', 'c': 'candy', 'd': 'donuts'}
```
이것은 얕은 복사를 수행한다.

<br/>

### 결합하기: update()
```python
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }

pythons.update(others)

print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 
# 'Marx': 'Groucho', 'Howard': 'Moe'}
```
두 번째 딕셔너리를 첫 번째 딕셔너리에 병합하려고 할 때 두 딕셔너리에 같은 키:값이 있다면 두 번째 딕셔너리 값으로 병합된다.
```python
first = { 'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)

print(first)
# {'a': 1, 'b': 'platypus'}
```

<br/>

### 키와 del로 항목 삭제하기
```python
del pythons['Marx']
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Howard': 'Moe'}

del pythons['Howard']
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
```

<br/>

### 키로 항목을 가져온 뒤 삭제하기: pop()
pop()은 get()과 del을 함께 사용한다.
딕셔너리에 있는 키와 pop()의 인수가 일치하면 해당 값을 반환한 뒤, 
딕셔너리에 해당 키-값을 삭제한다.
일치하지 않는다면 예외가 발생한다.
```python
print(len(pythons)) # 6
print(pythons.pop('Palin')) # Michael
print(len(pythons)) # 5
print(pythons.pop('Palin')) # KeyError: 'Palin'
```
pop()에 두 번째 인수를 지정하면, get()과 같이 잘 작동한다.
키가 존재하지 않을 시 두 번째 인수가 출력된다.
```python
print(pythons.pop('First', 'Hugo')) # Hugo
print(len(pythons)) # 5
```

<br/>

### 모든 항목 삭제하기: clear()
```python
pythons.clear()
print(pythons) # {}
```

<br/>

### 키 멤버십 테스트: in
```python
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 
        'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
        
print('Chapman' in pythons) # True
print('Palin' in pythons) # True
print('Gilliam' in pythons) # False
```

<br/>

### 할당하기: =
딕셔너리를 할당한 후 변경할 때 딕셔너리를 참조하는 모든 이름에 변경된 딕셔너리를 반영한다.
```python
signals = {'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'}

save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
# {'green': 'go', 'yellow': 'go faster', 
# 'red': 'smile for the camera', 'blue': 'confuse everyone'} 
```

<br/>

### 얕은 복사: copy()
딕셔너리 키/값을 또 다른 딕셔너리로 복사하기 위해서는 위와 같이 할당하지 않고 copy()를 사용한다.
```python
signals = {'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'}

original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
# {'green': 'go', 'yellow': 'go faster', 
# 'red': 'smile for the camera', 'blue': 'confuse everyone'}   
print(original_signals)
# {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
```
딕셔너리 값이 불변이면 동작하지만, 가변이라면 deepcopy()를 사용해야 한다.

<br/>

### 깊은 복사: deepcopy()
```python
# 얕은 복사
signals = {'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']}

signals_copy = signals.copy()
print(signals)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
print(signals_copy)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}

signals['red'][1] = 'sweat'
print(signals)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}
print(signals_copy)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}

# 깊은 복사
import copy
signals = {'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']}

signals_copy = copy.deepcopy(signals)
print(signals)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
print(signals_copy)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}

signals['red'][1] = 'sweat'
print(signals)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'sweat']}
print(signals_copy)
# {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
```

<br/>

### 딕셔너리 비교
==, != 외의 비교연산자는 사용할 수 없다.
```python
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b) # True
print(a <= b)
# TypeError: '<=' not supported between instances of 'dict' and 'dict'
```
파이썬은 원래 생성된 키/ 값의 순서에 상관없이 딕셔너리의 키/값을 하나씩 비교한다.
```python
a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a == b) # False
```

<br/>

### 순회하기: for와 in
```python
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col.Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)
# room
# weapon
# person
```
값을 순회하려면 values() 메서드를 사용한다.
```python
for value in accusation.values():
    print(value)
# ballroom
# lead pipe
# Col.Mustard
```
모두 튜플로 반환하려면 items() 메서드를 사용한다.
```python
for item in accusation.items():
    print(item)
# ('room', 'ballroom')
# ('weapon', 'lead pipe')
# ('person', 'Col.Mustard')
```
한 번에 모두 튜플에 할당할 수 있다.
```python
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
# Card room has the contents ballroom
# Card weapon has the contents lead pipe
# Card person has the contents Col.Mustard
```

<br/>

### 딕셔너리 컴프리헨션
```python
{키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체}
```
```python
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in word}
print(letter_counts)
# {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter:word.count(letter) for letter in set(word)}
print(letter_counts)
```
set(word)를 순회하는 것은 문자열 word를 순회하는 것과 다르게 문자를 반환하기 때문에 위와 아래의 정렬은 다르게 되어있다.

if문과 다중 for문을 사용할 수 있다.
```python
{키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체 if 테스트}
```
```python
vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) 
                if letter in vowels}
print(vowel_counts)
# {'e': 1, 'a': 2, 'i': 1, 'o': 4}
```

<br/>

---
# 셋
셋은 값은 버리고 키만 남은 딕셔너리와 같다.
어떤 것이 존재하는지만 판단할 때 셋을 사용한다.
키에 어떤 정보를 첨부해서 그 결과를 얻고 싶을 때 딕셔너리를 사용한다.

### 생성하기: set()
set() 함수나 중괄호 안에 콤마로 구분된 값을 넣으면 된다.
```python
empty_set = set()
print(empty_set) # set()

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers) # {0, 2, 4, 6, 8}

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers) # {1, 3, 5, 7, 9}
```
셋은 순서와 상관없이 저장된다.

<br/>

### 변환하기: set()
리스트, 문자열, 튜플, 딕셔너리에서 중복된 값을 삭제하여 셋을 생성할 수 있다.
```python
print(set( 'letters'))
# {'t', 'l', 'r', 'e', 's'}
```
'e'와 't'가 두 개씩 있어도, 셋에는 이 문자들이 하나씩 포함되어 있다.

리스트를 셋으로 만들 수 있다.
```python
print(set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ))
# {'Prancer', 'Mason-Dixon', 'Dancer', 'Dasher'}
```
튜플을 셋으로 만들 수 있다.
```python
print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ))
# {'Ummagumma', 'Atom Heart Mother', 'Echoes'}
```

딕셔너리에 set()을 사용하면 키만 사용한다.
```python
print (set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))
# {'cherry', 'orange', 'apple'}
```

<br/>

### 길이 얻기: len()
```python
reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
print(len(reindeer)) # 4
```

<br/>

### 항목 추가하기: add()
```python
s = set((1, 2, 3))
print(s) # {1, 2, 3}

s.add(4)
print(s) # {1, 2, 3, 4}
```

<br/>

### 항목 삭제하기: remove()
```python
s = set((1, 2, 3))
s.remove(3)
print(s) # {1, 2}
```

<br/>

### 순회하기: for와 in
```python
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)
# ottoman
# table
# sofa
```

<br/>

### 멤버십 테스트: in
일반적으로 사용하는 셋의 용도다.
```python
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermount', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
# martini
# black russian
# white russian
# screwdriver

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
        'cream' in contents):
        print(name)
# black russian
# screwdriver
```

<br/>

### 콤비네이션과 연산자
& 연산자의 결과는 비교하고자 했던 재료의 모든 항목이 포함된 셋이다.
```python
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
# martini
# manhattan
# screwdriver

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
# black russian
# screwdriver
```

두 음료의 재료 셋을 변수에 저장할 수 있다.
그 다음 이 변수를 사용한다.
```python
bruss = drinks['black russian']
wruss = drinks['white russian']
```

다음 예제에서 셋 연산자의 기호와 함수 둘 다 사용해본다.
```python
a = {1, 2}
b = {2, 3}
```
& 연산자와 intersection() 메서드를 사용해서 교집합을 구할 수 있다.
```python
print(a & b) # {2}
print(a.intersection(b)) # {2}
```
조금 전 저장한 음료의 재료 변수를 사용한다.
```python
print(bruss & wruss)
# {'kahlua', 'vodka'}
```
 | 연산자와 union() 메서드를 사용해서 합집합을 구할 수 있다.
```python
 print(bruss | wruss)
# {'cream', 'vodka', 'kahlua'}
```

- 연산자와 difference() 메서드를 사용해서 차집합을 구할 수 있다.
```python
print(a - b) # {1}
print(a.difference(b)) # {1}
print(bruss - wruss) # set()
print(wruss - bruss) # {'cream'}
```

^ 연산자나 symmetric_difference() 메서드를 사용해서 대칭 차집합을 구할 수 있다.
```python
print(a ^ b) # {1, 3}
print(a.symmetric_difference(b)) # {1, 3}
print(bruss ^ wruss) # {'cream'}
```

<= 연산자나 issubset() 메서드를 사용해서 첫 번째 셋이 두 번째 셋의 부분집합인지 알 수 있다.
```python
print(a <= b) # False
print(a.issubset(b)) # False
# wruss는 bruss의 상위집합이다.
print(bruss <= wruss) # True
```
모든 셋은 자신의 부분집합이다.

첫 번째 셋이 두 번째 셋의 진부분집합이 되려면, 두 번째 셋에는 첫 번째 셋의 모든 멤버를 포함한 그 이상의 멤버가 있어야 한다.
```python
print(a < b) # False
print(a < a) # False
print(bruss < wruss) # True
```

연산자 >=나 issuperset() 메서드를 사용해서 첫 번째 셋이 두 번째 셋의 상위집합인지 알 수 있다.
```python
print(a >= b) # False
print(a.issuperset(b)) # False
print(wruss >= bruss) # True
```
모든 셋은 자신의 상위집합이다.

첫 번째 셋이 두 번째 셋의 진상위집합이 되려면, 첫 번째 셋에는 두 번째 셋의 모든 항목을 포함한 그 이상의 항목이 있어야 한다.
```python
print(a > b) # False
print(wruss > bruss) # True
```
모든 셋은 자신의 진상위집합이 될 수 없다.

<br/>

### 셋 컴프리헨션
```python
{표현식 for 표현식 in 순회 가능한 객체}
{표현식 for 표현식 in 순회 가능한 객체 if 테스트}
```
```python
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set) # {1, 4}
```

<br/>

### 불변 셋 생성하기: frozenset()
frozenset() 함수와 인수로 순회 가능한 객체를 사용한다.
```python
print(frozenset([3, 2, 1]))
# frozenset({1, 2, 3})
print(frozenset(set([2, 1, 3])))
# frozenset({1, 2, 3})
print(frozenset({3, 1, 2}))
# frozenset({1, 2, 3})
print(frozenset((2, 3, 1)))
# frozenset({1, 2, 3})

fs = frozenset([3, 2, 1])
print(fs)
# frozenset({1, 2, 3})
print(fs.add(4))
# AttributeError: 'frozenset' object has no attribute 'add'
```

<br/>

---

# 지금까지 배운 자료구조
- 대괄호를 사용한 리스트
- 콤마와 괄호를 사용한 튜플(괄호는 옵션)
- 중괄호를 사용한 딕셔너리와 셋

셋을 제외하고 모두 대괄호로 항목에 접근한다.
리스트와 튜플의 경우 대괄호에 들어가는 값이 정수 오프셋이고 딕셔너리는 키다.
이 세가지의 결과는 값이다.
셋은 인덱스와 키가 없다.
```python
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}

print(marx_list[2]) # Harpo
print(marx_tuple[2]) # Harpo
print(marx_dict['Harpo']) # harp

print('Harpo' in marx_list) # True
print('Harpo' in marx_tuple) # True
print('Harpo' in marx_dict) # True
print('Harpo' in marx_set) # True
```

<br/>

---

# 자료구조 결합하기
내장된 자료구조를 결합해서 자료구조를 확장할 수 있다.
```python
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
```

튜플의 각 요소는 리스트다.
```python
tuble_of_lists = marxes, pythons, stooges
print(tuble_of_lists)
# (['Groucho', 'Chico', 'Harpo'], 
# ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# ['Moe', 'Curly', 'Larry'])
```

세 리스트를 포함한 리스트를 만들 수 있다.
```python
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
# [['Groucho', 'Chico', 'Harpo'], 
# ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# ['Moe', 'Curly', 'Larry']]
```

리스트 딕셔너리를 만들 수 있다.
```python
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
# {'Marxes': ['Groucho', 'Chico', 'Harpo'], 
# 'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# 'Stooges': ['Moe', 'Curly', 'Larry']}
```

이런 자료구조의 제한 사항은 데이터 타입 자체에 있따.
딕셔너리의 키는 불변하기 때문에 리스트, 딕셔너리, 셋은 딕셔너리의 키가 될 수 없다.
그러나 튜플은 딕셔너리의 키가 될 수 있다.
