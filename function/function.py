# 함수 정의하기: def
def do_nothing():
    pass

# 함수 호출하기: ()
def make_a_sound():
    print('quack')

make_a_sound() # quack

def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
# Splendid!

# 인수와 매개변수
def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))
# Rumplestiltskin Rumplestiltskin

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

print(do_nothing()) # None

### 유용한 None
thing = None

if thing:
    print("It's some thing")
else:
    print("It's no thing")
# It's no thing

thing = None

if thing is None:
    print("It's nothing")
else:
    print("It's something")
# It's nothing

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

### 위치 인수
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}

print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
# {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}

print(menu('frontenac', dessert='flan', entree='fish'))
# {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}

### 기본 매개변수 값 지정하기
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}

print(menu('dunkelfelder', 'duck', 'doughnut'))
# {'wine': 'dunkelfelder', 'entree': 'duck', 'dessert': 'doughnut'}

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

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a') # ['a']
nonbuggy('b') # ['b']

### 위치 인수 분해하기/모으기: *
def print_args(*args):
    print('Positional tuple:', args)

print_args() # Positional tuple: ()
print_args(3, 2, 1, 'wait!', 'uh...')
# Positional tuple: (3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one, too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
# Need this one: cap
# Need this one, too: gloves
# All the rest: ('scarf', 'monocle', 'mustache wax')

print_args(2, 5, 7, 'x')
# Positional tuple: (2, 5, 7, 'x')

args = (2, 5, 7, 'x')
print_args(args)
# Positional tuple: ((2, 5, 7, 'x'),)

print_args(*args)
# Positional tuple: (2, 5, 7, 'x')

### 키워드 인수 분해하기/모으기: *
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()
# Keyword arguments: {}

print_kwargs(wine='melot', entree='mutton', dessert='macaroon')
# Keyword arguments: {'wine': 'melot', 'entree': 'mutton', 'dessert': 'macaroon'}

### 키워드 전용 인수
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

### 가변/불변 인수
outside = ['one', 'fine', 'day']

def mangle(arg):
    arg[1] = 'terrible!'

mangle(outside)

print(outside)

# 독스트링
def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

help(echo)
# Help on function echo in module __main__:

# echo(anything)
#     echo returns its input argument

print(echo.__doc__)
# echo returns its input argument

### 일등 시민: 함수
def answer():
    print(42)

answer() # 42

def run_something(func):
    func()

run_something(answer) # 42

print(type(run_something)) # <class 'function'>

def add_args(arg1, arg2):
    print(arg1 + arg2)

print(type(add_args)) # <class 'function'>

# func: 실행할 함수
# arg1: func 함수의 첫 번째 인수
# arg2: func 함수의 두 번째 인수
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9) # 14

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4)) # 10

# 내부 함수
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7)) # 11

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))

### 클로저
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

print(a)
# <function knights2.<locals>.inner2 at 0x0000025D7268F240>
print(b)
# <function knights2.<locals>.inner2 at 0x0000025D7268F2E0>

print(a()) # We are the knights who say: 'Duck'
print(b()) # We are the knights who say: 'Hasenpfeffer'

# 익명 함수: lambda
# words: 리스트
# func: 리스트의 각 word 문자열에 적용되는 함수
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)
# Thud!
# Meow!
# Thud!
# Hiss!

edit_story(stairs, lambda word: word.capitalize() + '!')
# Thud!
# Meow!
# Thud!
# Hiss!

print(sum(range(1, 101))) # 5050

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)
# <function my_range at 0x00000112E477F4C0>

ranger = my_range(1, 5)

print(ranger)
# <generator object my_range at 0x000001CF71924110>

for x in ranger:
    print(x)
# 1
# 2
# 3
# 4

for try_again in ranger:
    print(try_again)
#

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
# <generator object <genexpr> at 0x0000024481FD37C0>

for thing in genobj:
    print(thing)
# ('a', '1')
# ('b', '2')

# 데커레이터
# 함수 이름과 인수를 출력한다.
# 인수로 함수를 실행한다.
# 결과를 출력한다.
# 수정된 함수를 사용하도록 반환한다.
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5)) # 8

cooler_add_ints = document_it(add_ints) # 데커레이터 수동 할당
cooler_add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: new_function
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64

@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

# 네임스페이스와 스코프
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
# at the top level: fruitbat
print_global()
# inside print_global: fruitbat

# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)

# change_and_print_global()
# UnboundLocalError: cannot access local variable 'animal'
# where it is not associated with a value

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local() # inside change_local: wombat 2039293714736
print(animal) # fruitbat
print(id(animal)) # 2615608827888

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('after the change:', animal)

print(animal) # fruitbat
change_and_print_global()
# after the change: wombat
print(animal) # wombat

animal = 'fruitbat' # 전역 변수

def change_local(): 
    animal = 'wombat' # 지역 변수
    print('locals:', locals())

print(animal) # fruitbat
change_local() # locals: {'animal': 'wombat'}
print(animal) # fruitbat

# 이름에 _와 __ 사용하기
def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()
# This function is named: amazing
# And its docstring is: This is the amazing function.
#     Want to see it again?

# 재귀 함수
# def dive():
#     return dive()

# dive()
# Traceback (most recent call last):

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

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]

print(list(flatten(lol)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 예외
# short_list = [1, 2, 3]
# position = 5
# short_list[position]
# Traceback (most recent call last):
# ~~~
# IndexError: list index out of range

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, ' but got', position)
# Need a position between 0 and 2  but got 5

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

### 에외 만들기
class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
# Traceback (most recent call last):
# ~~~
# UppercaseException: MO

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)