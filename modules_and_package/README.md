# 모듈과 import 문
**모듈**은 파이썬 코드 파일이다.
개발자는 특별한 작업 없이 코드를 모듈로 사용할 수 있다.
**import** 문을 사용하여 다른 모듈의 코드를 참조한다.
이것은 임포트한 모듈의 코드와 변수를 사용할 수 있게 만들어준다.

### 모듈 임포트하기
import 문을 사용하여 간단하게 모듈을 임포트할 수 있다.
확장자 .py를 제외한 파이썬 파일의 이름을 입력한다.
```python
from random import choice

places = ["McDonalds", "KFC", "Burger King", 
            "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    return choice(places)
```
```python
import fast

place = fast.pick()
print("Let's go to", place)
# Let's go to McDonalds
```
두 파일을 같은 디렉터리에 저장하고 실행하면 메인 프로그램 fast 모듈에 접근해서 fast() 함수를 실행한다.

```python
places = ["McDonalds", "KFC", "Burger King", 
            "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    import random
    return random.choice(places)
```

프로그래밍의 다양한 측면에서 어떤 코드 스타일을 선택할 때는 자신에게 맞는 가장 분명한 것을 선택한다.
모듈의 이름을 붙이는 것이 좀 더 안전하지만, 약간의 입력을 필요로 한다.

임포트한 코드가 여러 곳에서 사용되는 경우, import 문을 함수 밖으로 빼내는 것을 고려해야 한다.
함수 내부에서 import 문을 사용하는 경우, 코드 사용이 그 함수 내부에서만 제한된다.

<br/>

### 다른 이름으로 모듈 임포트하기
import fast를 사용했다.
하지만 다음과 같은 경우가 있다고 가정한다면
- 다른 곳에 fast 모듈이 존재하는가?
- 모듈과 관련된 연상 단어를 사용하고 싶은가?
- 짧은 모듈 이름을 사용하고 싶은가?
에일리어스를 사용해 가져올 수 있다.
```python
import fast as f
place = f.pick()
print("Let's go to", place)
```

<br/>

### 필요한 모듈만 임포트하기
모듈 전체나 필요한 부분만 임포트할 수있다.
모듈에서 에일리어스를 사용한 것처럼 모듈의 각 항목에 별명을 사용할 수 있다.
```python
from fast import pick
place = pick()
print("Let's go to", place)
```
이제 이 함수를 who_cares()함수로 임포트해본다.
```python
from fast import pick as who_cares
place = who_cares
print("Let's go to", place)
```

<br/>

---

# 패키지
파이썬 애플리케이션을 좀 더 확장하기 위해 모듈을 패키지라는 파일과 모듈 계층 구조에 구성할 수 있다.
패키지는 .py 파일을 포함한 하위 디렉터리다.
또한 디렉터리 안에 디렉터리를 여러 깊이로 사용할 수 있다.
```python
from choice import fast, advice

print("Let's go to", fast.pick())
print("Should. we take out?", advice.give())
```
파이썬은 현재 디렉터리에서 choice라는 디렉터리를 찾는다.
그리고 그 안에 있는 fast.py와 advice.py 파일을 찾는다.

chice안의 fast.py
```python
from random import choice

places = ["McDonalds", "KFC", "Burger King", 
            "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick():
    """Return random fast food place"""
    return choice(places)
```
choice 안의 advice.py
```python
from random import choice

answers = ["Yes!", "No!", "Reply hazy", "Sorry, what?"]

def give():
    """Return random advice"""
    return choice(answers)
```
메인 프로그램의 questions.py를 실행하면 아래와 같다.
```python
from choice import fast, advice

print("Let's go to", fast.pick())
print("Should. we take out?", advice.give())
# Let's go to McDonalds
# Should. we take out? Yes!
```

<br/>

### 모듈 탐색 경로
현재 디렉터리와 하위 디렉터리를 선택하여 해당 모듈에 접근했다.
다른 위치에서도 접근하여 제어할 수 있다.
파이썬 인터프리터가 보는 모든 위치를 보려면 표준 sys 모듈을 임포트해서 path 리스트를 살펴본다.
```python
import sys
for place in sys.path:
    print(place)
# C:\python\modules_and_package
# C:\Users~~~
# C:\Users~~~
```

코드 내에서 탐색 경로를 수정할 수 있다.

<br/>

### 네임스페이스 패키지
네임스페이스 패키지가 있는 디렉터리에서 패키지를 분할할 수 있다.
아래의 파일 레이아웃이 있다고 친다.
```
critters
	rougarou.py
    wendigo.py
```
이 모듈의 일반적인 import 문은 다음과 같다.
```python
from critters import wendigo, rougarou
```
이제 미국의 남과 북위치를 추가했을 때의 파일과 디렉터리의 내용은 다음과 같다.
```
north
	critters
    wendigo.py
south
	critters
    rougarou.py
```
north와 south가 모두 모듈 탐색 경로에 있다면, 단일 디렉터리 패키지를 공동으로 사용하는 것처럼 모듈을 가져올 수 있다.
```python
from critters import wendigo, rougarou
```

<br/>

### 모듈 vs 객체
모듈과 객체는 여러 면에서 비슷하게 보인다.
stuff라는 내부 데이터 값이 있는 thing이라는 객체 또는 모듈을 사용하면 thing.stuff로 값에 접근할 수 있다.
모듈이나 클래스를 만들 때 stuff가 정의되었거나 나중에 할당될 수 있다.
객체는 프로퍼티나 던더(__) 이름을 사용하여 데이터 속성에 대한 접근을 숨기거나 제어할 수 있다.
```python
import math
print(math.pi)
# 3.141592653589793
math.pi = 3.0
print(math.pi)
# 3.0
```
이것은 파이썬 math 모듈에 영향을 미치지 않았다.
호출 프로그램에서 가져온 math 모듈 코드의 사본에 대해서만 pi 값을 변경했으며, 위 코드 수행이 완료되면 이 값은 사라진다.

<br/>

---

# 파이썬 표준 라이브러리
파이썬의 두드러진 점 중 하나는 배터리 포함이라는 모토로 유용한 작업을 처리하는 많은 표준 라이브러리 모듈이다.
그리고 이 모듈은 핵심 언어가 늘어나는 것을 피하기 위해 분리되어 있다.

### 누락된 키 처리하기: setdefault()와 defaultdict()
setdefault() 함수는 get() 함수와 같지만, 키가 누락된 경우 딕셔너리에 항목을 할당할 수 있다.
```python
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2}
```
딕셔너리에 키가 없는 경우 새 값이 사용된다.
```python
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon) # 12
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}
```

존재하는 키에 다른 기본값을 할당하려 하면 키에 대한 원래 값이 반환되고 아무것도 바뀌지 않는다.
```python
helium = periodic_table.setdefault('Helium', 947)
print(helium) # 2
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}
```

defaultdict() 함수도 비슷하다.
다른 점은 딕셔너리를 생성할 때 모든 새 키에 대한 기본값을 먼저 지정한다는 것이다.
이함수의 인수는 함수다.
```python
from collections import defaultdict
periodic_table = defaultdict(int)
```
```python
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead']) # 0
print(periodic_table)
# defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})
```
defaultdict()의 인순ㄴ 값을 누락된 키에 할당하여 반환하는 함수다.
```python
from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print(bestiary['A']) # Abominable Snowman
print(bestiary['B']) # Basilisk
print(bestiary['C']) # Huh?
```
인수를 입력하지 않으면 새로운 키의 기본값이 None으로 설정된다.

lambda를 사용하여 호출 안에 기본값을 만드는 함수를 정의할 수 있다.
```python
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E']) # Huh?
```
카운터를 위해 아래와 값이 int 타입을 사용할 수 있다.
```python
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
# spam 3
# eggs 1
```

<br/>

### 항목 세기: Counter()
표준 라이브러리에는 항목을 셀 수 있는 여러 함수가 있다.
```python
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
# Counter({'spam': 3, 'eggs': 1})
```

most_common() 함수는 모든 요소를 내림차순으로 반환한다.
숫자를 입력하는 경우, 그 숫자만큼 상위 요소를 반환한다.
```python
print(breakfast_counter.most_common())
# [('spam', 3), ('eggs', 1)]
print(breakfast_counter.most_common(1))
# [('spam', 3)]
```
카운터를 결합할 수도 있고 뺄 수도 있다.
```python
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
# Counter({'eggs': 2, 'bacon': 1})

print(breakfast_counter + lunch_counter)
# Counter({'spam': 3, 'eggs': 3, 'bacon': 1})
print(breakfast_counter - lunch_counter)
# Counter({'spam': 3})
print(lunch_counter - breakfast_counter)
# Counter({'eggs': 1, 'bacon': 1})
```
교집합 연산자 &를 통해 고통된 항목을 얻을 수 있다.
```python
print(lunch_counter & breakfast_counter)
# Counter({'eggs': 1})
```
합집합 연산자 |를 사용하면 모든 항목을 얻을 수 있다.
```python
print(lunch_counter | breakfast_counter)
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})
```

<br/>

### 키 정렬하기: OrderedDict()
파이썬 2 인터프리터에서 아래 코드를 실행하면 결과는 다음과 같다.
```python
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
}

for stooge in quotes:
    print(stooge)
# Moe
# Larry
# Curly
```
OrderedDict()는 키 순서를 기억한다.
반복문과 같은 순서대로 반환한다.
```python
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

for stooge in quotes:
    print(stooge)
# Moe
# Larry
# Curly
```

<br/>

### 스택 + 큐 == 데크
데크느 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐다.
데크는 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때 유용하게 쓰인다.
popleft() 함수는 데크로부터 왼쪽 끝의 항목을 제거한 후, 그 항목을 반환한다.
pop() 함수는 오른쪽 끝의 항목을 제거한 후, 그 항목을 반환한다.
양쪽 끝에서부터 이 두 함수가 중간 지점을 향해 동작한다.
서로 일치한다면 단어 중간에 도달할 때까지 데크를 팝한다.
```python
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a')) # True
print(palindrome('racecar')) # True
print(palindrome('')) # True
print(palindrome('radar')) # True
print(palindrome('halibut')) # False
```
회문(앞에서 읽으나 뒤에서부터 읽으나 같은 구문) 코드를 더 간단하게 작성하고 싶다면 한 문자열을 반전해서 비교하면 된다.
파이썬은 문자열에 대한 reverse() 메서드가 없지만, 다음과 같이 스라이스로 문자열을 반전할 수 있다.
```python
def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar')) # True
print(another_palindrome('halibut')) # False
```

<br/>

### 코드 구조 순회하기: itertools
itertools는 특수 목적의 이터레이터 함수를 포함하고 있다.
for...in 반복문에서 이터레이터 함수를 호출할 때 함수는 한 번에 한 항목을 반환하고 호출 상태를 기억한다.

chain() 함수는 순회가능한 인수들을 차례로 반복한다.
```python
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
# 1
# 2
# a
# b
```

cycle() 함수는 인수를 순환하는 무한 이터레이터다.
```python
import itertools
for item in itertools.cycle([1, 2]):
    print(item)
# 1
# 2
# 1
# 2
# 1
# 2
# 1
# ...
```

accumulate() 함수는 축적된 값을 계산한다. 기본으로 합계를 계산한다.
```python
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
# 1
# 3
# 6
# 10
```
accumulate() 함수의 두 번째 인수로 함수를 전달하여, 합계를 구하는 대신 이 함수를 사용할 수있다.
```python
import itertools
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
# 1
# 2
# 6
# 24
```

itertools 모듈은 많은 함수를 제공하며, 조합 및 순열을 위한 함수도 있다.

<br/>

### 깔끔하게 출력하기: pprint()
출력된 결과를 읽기 힘든 경우 pprint() 함수가 필요하다.
```python
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

print(quotes)
# OrderedDict({'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'})
# 같게 나왔다. 책에서는 서로 다르게 나왔지만...
pprint(quotes)
# OrderedDict({'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'})
```

<br/>

### 임의값 얻기
```python
from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))
# bacon
print(choice(['a', 'one', 'and-a', 'two']))
# one
print(choice(range(100)))
# 60
print(choice('alphabet'))
# t
```
한 번에 둘 이상의 값을 얻으려면 sample() 함수를 사용한다.
```python
from random import sample
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
# [9, 'bacon', 23]
print(sample(['a', 'one', 'and-a', 'two'], 2))
# ['one', 'two']
print(sample(range(100), 4))
# [78, 96, 4, 51]
print(sample('alphabet', 7))
# ['a', 'p', 'a', 'b', 'h', 't', 'e']
```
어떤 범위에서 임의의 정수를 얻으려면 choice()와 sample()을 rage()와 같이 사용하거나 radint()와 randrange()를 사용한다.
```python
from random import randint
print(randint(38, 74)) # 57
print(randint(38, 74)) # 48
print(randint(38, 74)) # 52
```
randrange()는 range()와 같은 인수를 가진다. 시작(포함), 끝(제외), 스탭(옵션값)
```python
from random import randrange
print(randrange(38, 74)) # 45
print(randrange(38, 74, 10)) # 68
print(randrange(38, 74, 10)) # 38
```
0.0과 0.1사이의 임의의 실수를 얻는다.
```python
from random import random
print(random()) # 0.02930071684611002
print(random()) # 0.16549406290876278
print(random()) # 0.06019680478611067
```




