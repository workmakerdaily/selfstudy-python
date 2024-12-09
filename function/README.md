# 함수 정의하기: def
함수를 정의하기 위해서는 def와 함수 이름, 괄호를 입력한다.
괄호 안에는 옵션으로 매개변수를 입력할 수 있다.
그리고 마지막으로 콜론을 붙인다.
이름의 첫 글자는 반드시 영문이나 언더바를 사용해야 한다.
(영문자, 숫자, 언더바만 사용할 수 있다.)
```python
def do_nothing():
    pass
```
매개변수가 없더라도 콜론을 입력해야 한다.
함수 다음 줄은 들여쓰기를 해야한다.

<br/>

---

# 함수 호출하기: ()
매개변수가 없는 함수를 정의하고 호출할 수 있다.
```python
def make_a_sound():
    print('quack')

make_a_sound() # quack
```
```python
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
# Splendid!
```

<br/>

---

# 인수와 매개변수
함수로 전달한 값을 인수라고 부른다.
인수와 함수를 호출하면 인수의 값은 함수 내에서 해당하는 매개변수에 복사된다.
함수 외부에서는 **인수**라고 하지만 내부에서는 **매개변수**라고 한다.
```python
def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))
# Rumplestiltskin Rumplestiltskin
```

if 문을 사용하고 인수를 취하는 함수를 작성할 수 있다.
```python
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)
# I've never heard of the color blue.
```
함수의 인수는 개수에 상관없이 모든 유형의 인수를 취할 수 있다.
반환값도 마찬가지로 개수에 상관없이 모든 유형을 반환할수 있다.
함수가 명시적으로 return을 호출하지 않으면, 호출자는 반환값으로 None을 얻는다.
```python
print(do_nothing()) # None
```

### 유용한 None
불리언의 False처럼 보이지만 다른 값을 의미한다.
```python
thing = None

if thing:
    print("It's some thing")
else:
    print("It's no thing")
# It's no thing
```
불리언 값 False와 None을 구분하기 위해 is 연산자를 사용한다.
```python
thing = None

if thing is None:
    print("It's nothing")
else:
    print("It's something")
# It's nothing
```
빠뜨린 빈 값을 구분하기 위해 None을 사용한다.
```python
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None) # None is None
whatis(True) # True is True
whatis(False) # False is False

whatis(0) # 0 is False
whatis(0.0) # 0.0 is False
whatis('') #  is False
whatis("") #  is False
whatis('''''') #  is False
whatis(()) # () is False
whatis([]) # [] is False
whatis({}) # {} is False
whatis(set()) # set() is False
whatis(0.00001) # 1e-05 is True
whatis([0]) # [0] is True
whatis(['']) # [''] is True
whatis(' ') #   is True
```

<br/>

### 위치 인수
파이썬은 다른 언어에 비해 함수의 인수를 유연하고 독특하게 처리한다.
인수의 가장 익숙한 유형은 값을 순서대로 상응하는 매개변수에 복사하는 위치 인수이다.

다음 함수는 위치 인수로 딕셔너리를 만들어서 반환한다.
```python
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}
```
위치 함수의 단점은 각 위치의 의미를 알아야 한다.

<br/>

### 키워드 인수
위치 인수의 혼란을 피하기 위해 매개변수에 상응하는 이름을 인수에 지정할 수 있다.
인수를 함수 정의와 다른 순서로 지정할 수 있다.
```python
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
# {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}
```
위치 인수와 키워드 인수를 섞어서 쓸 수 있다.
```python
print(menu('frontenac', dessert='flan', entree='fish'))
# {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}
```

<br/>

### 기본 매개변수 값 지정하기
호출자가 대응하는 인수를 제공하지 않으면 기본값을 사용한다.
```python
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}

print(menu('dunkelfelder', 'duck', 'doughnut'))
# {'wine': 'dunkelfelder', 'entree': 'duck', 'dessert': 'doughnut'}
```

buggy() 함수는 일반 매개변수 arg와 기본 매개변수로 빈 리스트를 취하는 result가 있다. 함수는 arg를 result 리스트에 추가한다.
이전에 호출했던 result가 그대로 리스트에 남아 있는 상태로 출력된다.
```python
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a') # ['a']
buggy('b') # ['a', 'b']

def works(arg):
    result = []
    result.append(arg)
    return result

print(works('a')) # ['a']
print(works('b')) # ['b']
```

첫 번째 인수 호출을 가리키기 위해 매개변수에 다른 값을 넣어서 수정할 수 있다.
```python
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a') # ['a']
nonbuggy('b') # ['b']
```

<br/>

### 위치 인수 분해하기/모으기: *
함수의 매개변수에 애스터리스크를 사용할 때, 애스터리스크는 매개변수에서 위치 인수 변수를 튜플로 묶는다.
```python
def print_args(*args):
    print('Positional tuple:', args)

print_args() # Positional tuple: ()
print_args(3, 2, 1, 'wait!', 'uh...')
# Positional tuple: (3, 2, 1, 'wait!', 'uh...')
```
가변 인수를 사용하는 print()와 같은 함수는 매우 유용하다.
함수에 위치 인수를 지정할 때 맨 끝에 *args를 써서 나머지 인수를 모두 취하게 할 수 있다.
```python
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one, too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
# Need this one: cap
# Need this one, too: gloves
# All the rest: ('scarf', 'monocle', 'mustache wax')
```
- 위치 인수를 함수에 전달하면, 함수 내 위치 매개변수와 일치한다.
- 튜플 인수를 함수에 전달하면, 함수 내 튜플 매개변수가 있다.
- 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 이수로 해석할 수 있다.
- args라는 튜플 인수를 함수에 전달하여, 위치 매개변수 *args로 분해할 수 있다.
이것은 튜플 매개변수 args 안에 다시 수집된다.
```python
print_args(2, 5, 7, 'x')
# Positional tuple: (2, 5, 7, 'x')

args = (2, 5, 7, 'x')
print_args(args)
# Positional tuple: ((2, 5, 7, 'x'),)

print_args(*args)
# Positional tuple: (2, 5, 7, 'x')
```
함수 호출 또는 정의에서만 *구문을 사용할 수 있다.

- 함수 외부에서 *args는 튜플 인수를 쉼표로 구분된 위치 매개변수로 분해한다.
- 함수 내부에서 *args는 모든 위치의 인수를 단일 인수 튜플로 수집한다.
- 외부 인수와 내부 인수 모두에 이름을 *args로 사용하는 것이 일반적이다.

*args는 함수 외부에서 분해된 값을 함수 내부에 모은다.

<br/>

### 키워드 인수 분해하기/모으기: *
키워드 인수를 딕셔너리로 묶기 위해 두개의 애스터리스크(**)를 사용할 수 있다.
인수의 이름은 키고, 값은 이 키에 대응하는 딕셔너리 값이다.
```python
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()
# Keyword arguments: {}

print_kwargs(wine='melot', entree='mutton', dessert='macaroon')
# Keyword arguments: {'wine': 'melot', 'entree': 'mutton', 'dessert': 'macaroon'}
```
함수 내에서 kwargs는 딕셔너리 매개변수다.
인수의 순서는
- 위치 인수
- 위치 인수(*args) - 옵션
- 키워드 인수 (**kwargs) - 옵션

이다.

args와 마찬가지로 키워드 인수 이름을 kwargs로 사용하지만 필수는 아니다.

**구문은 함수 호출 또는 정의에서만 유효하다.

- 키워드 인수를 함수에 전달하면, 함수 내 키워드 매개변수와 일치한다.
- 딕셔너리 인수를 함수에 전달하면, 함수 내 딕셔너리 매개변수가 있다.
- 하나 이상의 키워드 인수(이름=값)를 함수에 전달하고, 이를 **kwargs에 수잡하여, kwargs 딕셔너리 매개변수로 해석할 수 있다.
- 함수 외부에서 **kwargs는 딕셔너리 kwargs를 '이름=값' 인수로 분해한다.
- 함수 내부에서 **kwargs는 '이름=값' 인수를 단일 딕셔너리 매개변수 kwargs에 모은다.

**kwargs는 함수 외부에서 분해된 '이름=값'을 함수 내부에 모은다.

<br/>

### 키워드 전용 인수
위치 매개변수와 이름이 같은 키워드 인수를 전달하면 원하는 결과를 얻지 못할 수 있다.
파이썬 3에서는 키워드 전용 인수를 지정할 수 있다.
값을 위치적으로 제공하지 않고, '이름=값'으로 제공해야 한다.
아래 함수의 단일 애스터리스크(*)는 start 및 end 매개변수의 기본값을 사용하고 싶지 않은 경우 명명된 인수로 제공해야 함을 의미한다.
```python
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']

print_data(data)
# a
# b
# c
# d
# e
# f

print_data(data, start=4)
# e
# f

print_data(data, end=2)
# a
# b
```

<br/>

### 가변/불변 인수
인수가 가변 객체인 경우 해당 매개변수를 통해 함수 내부에서 값을 변경할 수 있다.
```python
outside = ['one', 'fine', 'day']

def mangle(arg):
    arg[1] = 'terrible!'

mangle(outside)

print(outside)
```
위의 코드는 안 좋은 예다.
함수 내에서 인수가 변경될 수 있다고 문서화하거나 새 값을 반환한다.

<br/>

---

# 독스트링
함수 바디 시작 부분에 문자열을 포함시켜 함수 정의에 문서를 붙일 수 있다.
이것이 함수의 독스트링이다.
```python
def echo(anything):
    'echo returns its input argument'
    return anything
```

길게 작성할 수 있고, 포매팅을 추가할 수도 있다.
```python
def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)
```

독스트링을 출력하려면 help() 함수를 호출한다.
```python
help(echo)
# Help on function echo in module __main__:

# echo(anything)
#     echo returns its input argument
```

서식 없는 독스트링을 그대로 보고 싶다면 다음과 같이 작성한다.
```python
print(echo.__doc__)
# echo returns its input argument
```

<br/>

### 일등 시민: 함수
함수를 변수에 할당하고, 다른 함수에서 이를 인수로 사용하고, 함수에서 이를 반환할 수 있다는 것이다.
```python
def answer():
    print(42)

answer() # 42
```
run_something() 함수에 answer 인수를 넣으면 이 함수를 데이터처럼 사용한다.
```python
def run_something(func):
    func()

run_something(answer) # 42

print(type(run_something)) # <class 'function'>
```
인수를 넣어서 함수를 실행할 수 있다.
```python
def add_args(arg1, arg2):
    print(arg1 + arg2)

print(type(add_args)) # <class 'function'>
```

세 인수를 취하는 함수를 만들 수 있다.
```python
# func: 실행할 함수
# arg1: func 함수의 첫 번째 인수
# arg2: func 함수의 두 번째 인수
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
```
```python
run_something_with_args(add_args, 5, 9) # 14
```

*args, **kwargs 인수와 결합해서 사용할 수 있다.
```python
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)
    
print(run_with_positional_args(sum_args, 1, 2, 3, 4)) # 10
```
함수를 리스트, 튜플, 셋, 딕셔너리의 요소로 사용할 수 있다.
함수는 불변하기 때문에 딕셔너리의 키로도 사용할 수 있다.


<br/>

---

# 내부 함수
하무 안에 다른 함수를 정의할 수 있다.
```python
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7)) # 11
```
반복문이나 코드 중복을 피하고자 또 다른 함수 내에 어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 사용된다.
```python
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))
```

<br/>

### 클로저
내부 함수는 클로저처럼 동작할 수 있다.
클로저는 다른 함수에 의해동적으로 생성된다.
외부 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수다.
```python
# inner2()는 인수를 취하지 않고, 외부 함수의 변수를 직접적으로 사용한다.
# knights2()는 inner2 함수 이름을 호출하지 않고, 이를 반환한다.
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
    
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a)) # <class 'function'>
print(type(b)) # <class 'function'>

# 이들은 함수지만, 클로저이기도 하다.
print(a)
# <function knights2.<locals>.inner2 at 0x0000025D7268F240>
print(b)
# <function knights2.<locals>.inner2 at 0x0000025D7268F2E0>

print(a()) # We are the knights who say: 'Duck'
print(b()) # We are the knights who say: 'Hasenpfeffer'
```

<br/>

---

# 익명 함수: lambda
람다 함수는 단일 문장으로 표현되는 익명 함수다.
```python
# words: 리스트
# func: 리스트의 각 word 문자열에 적용되는 함수
def edit_story(words, func):
    for word in words:
        print(func(word))
```
words 리스트와 각 word에 적용할 함수가 필요하다.
```python
stairs = ['thud', 'meow', 'thud', 'hiss']
```
각 word의 첫 글자를 대문자로 만들고 느낌표를 붙여준다.
```python
def enliven(word):
    return word.capitalize() + '!'
```
```python
edit_story(stairs, enliven)
# Thud!
# Meow!
# Thud!
# Hiss!
```
enliven() 함수를 람다로 간단하게 바꿀 수 있다.
```python
edit_story(stairs, lambda word: word.capitalize() + '!')
# Thud!
# Meow!
# Thud!
# Hiss!
```
람다는 인수를 취하지 않거나 콤바로 구분된 인수를 취하고, 콜론 이후에 함수를 정의한다.
내부 함수에서 def로 작성한 함수를 호출할 때처럼 람다를 호출할 때, 괄호를 사용하지 않는다.
람다는 많은 작은 함수를 정의하고, 이들을 호출해서 얻은 모든 결과값으 저장해야할 때 유용하다.
특히 콜백 함수를 정의하는 그래픽 유저 인터페이스(GUI)에서 람다를 사용할 수 있다.

<br/>

---

# 제너레이터
제너레이터는 시퀀스를 생성하는 객체다.
제너레이터로 전체 시퀀스를 한 번에 메모리에 생성하고 정렬할 필요 없이, 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
제너레이터는 이터레이터에 대한 데이터 소스로 자주 새용된다.
```python
print(sum(range(1, 101))) # 5050
```
제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환한다.

<br/>

### 제너레이터 함수
잠재적으로 큰 시퀀스를 생성하고, 제너레이터 컴프리헨션에 대한 코드가 아주 길다면 제너레이터 함수를 사용하면 된다.
```python
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
        
print(my_range)
# <function my_range at 0x00000112E477F4C0>
```
이것은 일반 함수다.

다음과 같이 제너레이터 객체를 반환한다.
```python
ranger = my_range(1, 5)

print(ranger)
# <generator object my_range at 0x000001CF71924110>
```

이 제너레이터 객체를 순회할 수 있다.
```python
for x in ranger:
    print(x)
# 1
# 2
# 3
# 4
```
순회를 마친 제너레이터를 다시 순회한다면 아무것도 반환하지 않는다.
```python
for try_again in ranger:
    print(try_again)
#
```

<br/>

### 제너레이터 컴프리헨션
제너레이터 컴프리헨션은 대괄호, 중괄호 대신 괄호로 묶어서 사용한다.
제너레이터 컴프리헨션은 제너레이터 함수의 축약 버전이며, 안보이게 yield 문을 실행하고, 제너레이터 객체를 반환한다.
```python
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
# <generator object <genexpr> at 0x0000024481FD37C0>

for thing in genobj:
    print(thing)
# ('a', '1')
# ('b', '2')
```

<br/>

---

# 데커레이터
데커레이터는 하나의 함수를 취해서 또 다른 함수를 반환하는 함수다.
이 파이썬 트릭을 사용하기 위해서 다음 기술을 사용한다.
- *args와 **kwargs
- 내부 함수
- 함수 인수

```python
# 함수 이름과 인수를 출력한다.
# 인수로 함수를 실행한다.
# 결과를 출력한다.
# 수정된 함수를 사용하도록 반환한다.
def document_it(func):
    def new_function(*arg, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*arg, **kwargs)
        print('Result:', result)
        return result
    return new_function
```
document_it() 함수에 어떤 func 함수 이름을 전달하든지 document_it() 함수에 추가 선언문이 포함된 새 함수를 얻는다.
데커레이터는 실제로 func 함수로부터 코드를 실행하지 않는다.
하지만 document_it() 함수로부터 func를 호출하여 결과뿐만 아니라 새로운 함수를 얻는다.

데커레이터를 수동으로 할당할 수 있다.
```python
def add_ints(a, b):
    return a + b

print(add_ints(3, 5)) # 8

cooler_add_ints = document_it(add_ints) # 데커레이터 수동 할당
cooler_add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
```
수동 할당 대신 데커레이터를 사용하고 싶은 함수에 @데커레이터_이름을 추가하여 사용할 수 있다.
```python
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
```
함수는 여러 데커레이터를 가질 수 있다.
```python
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
```
함수에서 가장 가까운 데커레이터를 먼저 실행한 후, 그 위의 데커레이터가 실행된다.
```python
@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: new_function
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64
# 64

@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 64
```

<br/>

---

# 네임스페이스와 스코프
네임스페이스는 특정 이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계가 없는 것을 말한다.
각 함수는 자신의 네임스페이스를 정의한다.
메인 프로그램에서 x라는 변수를 정의하고, 함수에서 x라는 변수를 정의했을 때 이들은 서로 다른 것을 참조한다.
하지만 이 경계를 넘을 수 있다. 다양한 방법으로 다른 네임스페이스의 이름을 접근할 수 있다.

메인 프로그램은 전역 네임스페이스를 정의한다.
메인 프로그램의 네임스페이스에서 선언된 변수는 전역 변수다.
```python
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
# at the top level: fruitbat
print_global()
# inside print_global: fruitbat
```
함수에서 전역 변수의 값을 얻어서 바꾸려 하면 에러가 발생한다.
```python
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()
# UnboundLocalError: cannot access local variable 'animal'
# where it is not associated with a value
```
함수 내에서 전역 변수와 이름이 같은 변수 animal을 변경할 때, 함수 내 animal 변수를 변경한다.
```python
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local() # inside change_local: wombat 2039293714736
print(animal) # fruitbat
print(id(animal)) # 2615608827888
```
change_local() 함수에 이름이 animal인 변수를 갖지만, 그것은 로컬 네임스페이 안에 있다.

함수 내의 지역 변수가 아닌 전역 변수를 접근하기 위해 global 키워드를 사용해서 전역 변수의 접근을 명시해야 한다.
```python
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('after the change:', animal)

print(animal) # fruitbat
change_and_print_global()
# after the change: wombat
print(animal) # wombat
```
함수 안에 global 키워드를 사용하지 않으면 파이썬은 로컬 네임스페이스를 사용하고 변수는 지역 변수가 된다.
지역 변수는 함수를 수행한 뒤 사라진다.

네임스페이스의 내용을 접근하기 위해 두 가지 함수를 제공한다.
- locals() 함수는 로컬(지역) 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
- globals() 함수는 글로벌(전역) 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
```python
animal = 'fruitbat' # 전역 변수

def change_local(): 
    animal = 'wombat' # 지역 변수
    print('locals:', locals())

print(animal) # fruitbat
change_local() # locals: {'animal': 'wombat'}
print(animal) # fruitbat
```
change_local() 함수 내 로컬 네임스페이스에는 animal 로컬 변수만 있다.
메인 프로그램의 글로벌 네임스페이스에는 animal 전역 변수와 다른 여러 가지가 포함되어 있다.

<br/>

---

# 이름에 _와 __ 사용하기
언더바 두 개로 시작하고 끝나는 이름은 파이썬 내부 사용을 위해 예약되어 있다.
```python
def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()
# This function is named: amazing
# And its docstring is: This is the amazing function.
#     Want to see it again?
```

<br/>

---

# 재귀 함수
함수가 자기 자신을 호출하는 것을 재귀 함수 라고 한다.
파이썬에서 재귀가 깊다면(자기 자신을 너무 많이 호출하면) 예외가 발생한다.
```python
def dive():
    return dive()

dive()
# Traceback (most recent call last):
```
재귀 함수는 리스트의 리스트의 리스트와 같이 고르지 않은 데이터를 처리할 때 유용한다.
```python
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

print(flatten(lol))
# <generator object flatten at 0x0000020DD1B1A5E0>

print(list(flatten(lol)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
yield from 표현식을 추가하여 제너레이터의 일부를 전달할 수 있다.
```python
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

print(list(flatten(lol)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br/>

---

# 비동기 함수
비동기 함수를 정의하고 실행하기 위해서 async와 await 키워드가 파이썬 3.5에 추가되었다.

- 비교적 새로운 기능이다.
- 이해하기 조금 어렵다.
- 시간이 갈수록 더 중요해지고 더 잘 알려질 것이다.

지금은 함수를 정의하는 def 앞에 async 키워드가 붙으면 비동기 함수라는 것을 알면 된다.
함수를 호출하기 전에 await 키워드가 있으면 해당 함수는 비동기적이다.

<br/>

---

# 예외
코드 관련 에러가 발생할 때 실행되는 예외를 사용한다.
어떤 상황에서 실패할 수 있는 코드를 실행할 때, 잠재적인 모든 에러를 방지하기 위해 적절한 예외 처리가 필요하다.
어떤 함수에서 예외가 발생하여 그곳에서 잡히지 않았다면, 이 함수를 호출한 핸들러에 의해서 그 예외를 잡을 때까지 버블링한다.
파이썬은 에러 메시지와 오류가 발생한 위치에 대한 정보를 출력하고 프로그램을 종료한다.
```python
short_list = [1, 2, 3]
position = 5
short_list[position]
# Traceback (most recent call last):
# ~~~
# IndexError: list index out of range
```

<br/>

### 에러 처리하기: try, except
에러가 예상되는 코드에 try 문을 사용하고, 그 에러를 처리하기 위해 except 문을 사용한다.
```python
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, ' but got', position)
# Need a position between 0 and 2  but got 5
```
위와 같이 인수가 없는 except 문은 모든 예외 타입을 잡는다는 것을 말한다.
이것은 포괄절인 예외처리 방식이다.
두 개 이상의 예외 타입이 발생하면 별도의 예외 핸들러를 제공하는 것이 가장 좋은 방법이다.

예외 사항에 대한 세부정보를 얻고 싶다면 다음과 같이 변수 이름에서 예외 객체 전체를 얻을 수 있다.
```python
except 예외 타입 as 이름
```
다음 예제는 IndexError를 찾는다.
```python
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
# Position [q to quit]?1
# 2
# Position [q to quit]?0
# 1
# Position [q to quit]?2
# 3
# Position [q to quit]?3
# Bad index: 3
# Position [q to quit]?2
# 3
# Position [q to quit]?two
# Something else broke: invalid literal for int() with base 10: 'two'
# Position [q to quit]?q
```

<br/>

### 에외 만들기
모든 예외는 파이썬 표준 라이브러리에 미리 정의되어 있는 것이다.
우리가 만든 프로그램에서 특별한 상황에 발생할 수 있는 예외를 처리하기 위해 예외 유형을 정의할 수 있다.

예외는 클래스고, Exception 클래스의 자식이다.
```python
class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
# Traceback (most recent call last):
# ~~~
# UppercaseException: MO
```
부모 클래스 Exception은 예외가 발생했을 때 출력할 내용을 알아내고 있다.

예외 객체에 접근해서 그 내용을 출력한다.
```python
try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
```