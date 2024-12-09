# 튜플

empty_tuple = ()
print(empty_tuple) # ()

one_marx = 'Groucho',
print(one_marx) # ('Groucho',)

one_marx = ('Groucho',)
print(one_marx) # ('Groucho',)

one_marx = ('Groucho')
print(one_marx) # Groucho
print(type(one_marx)) # <class 'str'>

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple) # ('Groucho', 'Chico', 'Harpo')
print(type(marx_tuple)) # <class 'tuple'>

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple) # ('Groucho', 'Chico', 'Harpo')

one_marx = 'Groucho',
print(type(one_marx)) # <class 'tuple'>
print(type('Groucho',)) # <class 'str'>
print(type(('Groucho',))) # <class 'tuple'>

### 튜플 언패킹
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a) # Groucho
print(b) # Chico
print(c) # Harpo

### 튜플을 사용한 값 교환
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password) # tuttifrutti
print(icecream) # swordfish

### 생성하기: tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list)) # ('Groucho', 'Chico', 'Harpo')

### 결합하기: +
print(('Groucho',) + ('Chico', 'Harpo'))
# ('Groucho', 'Chico', 'Harpo')

### 항목 복제하기: *
print(('yada',) * 3) # ('yada', 'yada', 'yada')

### 비교하기
a = (7, 2)
b = (7, 2, 9)
print(a == b) # False
print(a <= b) # True
print(a < b) # True

### 순회하기: for와 in
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)
# fresh
# out
# of
# ideas

### 수정하기
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2) # ('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1) # ('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1)) # 1547252367040

t1 += t2
print(id(t1)) # 1547252246832

### 생성하기: []
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {'groundhog': 'Phil'}, 'Feb. 2']

### 생성 및 변환하기: list()
another_empty_list = list()
print(another_empty_list) # []

print(list('cat')) # ['c', 'a', 't']

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple)) # ['ready', 'fire', 'aim']

### 문자열 분할로 생성하기: split()
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))
# ['9', '19', '2019']

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
# ['a', 'b', '', 'c', 'd', '', '', 'e']

print(splitme.split('//'))
# ['a/b', 'c/d', '/e']

### [offset]으로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0]) # Groucho
print(marxes[1]) # Chico
print(marxes[2]) # Harpo

print(marxes[-1]) # Harpo
print(marxes[-2]) # Chico
print(marxes[-3]) # Groucho

### 슬라이스로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2]) # ['Groucho', 'Chico']
print(marxes[::2]) # ['Groucho', 'Harpo']
print(marxes[::-2]) # ['Harpo', 'Groucho']
print(marxes[::-1]) # ['Harpo', 'Chico', 'Groucho']

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes) # ['Harpo', 'Chico', 'Groucho']

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:]) # []
print(marxes[-6:]) # ['Groucho', 'Chico', 'Harpo']
print(marxes[-6:-2]) # ['Groucho']
print(marxes[-6:-4]) # []

### 리스트 끝에 항목 추가하기: append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo']

### 오프셋과 insert()로 항목 추가하기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes) # ['Groucho', 'Chico', 'Gummo', 'Harpo']

marxes.insert(10, 'Zeppo')
print(marxes) # ['Groucho', 'Chico', 'Gummo', 'Harpo', 'Zeppo']

### 모든 항목 복제하기: *
print(["blah"] * 3) # ['blah', 'blah', 'blah']

### 리스트 병합하기: extend()와 +
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]

### [offset]으로 항목 바꾸기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes) # ['Groucho', 'Chico', 'Wanda']

### 슬라이스로 항목 바꾸기
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers) # [1, 8, 9, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers) # [1, 7, 8, 9, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers) # [1, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers) # [1, 98, 99, 100, 4]

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers) # [1, 'w', 'a', 't', '?', 4]

### 오프셋으로 항목 삭제하기: del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Gummo']

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes) # ['Groucho', 'Harpo', 'Gummo']

### 값으로 항목 삭제하기: remove()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes) # ['Chico', 'Harpo']

### 오프셋으로 항목을 얻은 후 삭제하기: pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop()) # Zeppo
print(marxes) # ['Groucho', 'Chico', 'Harpo']
print(marxes.pop(1)) # Chico
print(marxes) # ['Groucho', 'Harpo']

### 모든 항목 삭제하기: clear()
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
work_quotes.clear()
print(work_quotes) # []

### 값으로 오프셋 찾기: index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico')) # 1

### 존재여부 확인하기: in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes) # True
print('Bob' in marxes) # False

### 값 세기: count()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo')) # 1
print(marxes.count('Bob')) # 0

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger')) # 3

### 문자열로 변환하기: join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes)) # Groucho, Chico, Harpo

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined) # Harry * Hermione * Ron

separated = joined.split(separator)
print(separated) # ['Harry', 'Hermione', 'Ron']

print(separated == friends) # True

### 정렬하기: sort()와 sorted()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes) # ['Chico', 'Groucho', 'Harpo']
print(marxes) # ['Groucho', 'Chico', 'Harpo']

marxes.sort()
print(marxes) # ['Chico', 'Groucho', 'Harpo']

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4.0]

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers) # [4.0, 3, 2, 1]

### 항목 개수 얻기: len()
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes)) # 3

### 할당하기: =
a = [1, 2, 3]
print(a) # [1, 2, 3]

b = a
print(b) # [1, 2, 3]

a[0] = 'surprise'
print(a) # ['surprise', 2, 3]
print(b) # ['surprise', 2, 3]

b[0] = 'I hate surprises'
print(b) # ['I hate surprises', 2, 3]
print(a) # ['I hate surprises', 2, 3]

### 복사하기: copy(), list(), 슬라이스
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
print(a) # ['integer lists are boring', 2, 3]
print(b) # [1, 2, 3]
print(c) # [1, 2, 3]
print(d) # [1, 2, 3]

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

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a) # [1, 2, [8, 9]]
print(b) # [1, 2, [8, 9]]

a[2][1] = 10
print(a) # [1, 2, [8, 10]]
print(b) # [1, 2, [8, 9]]

### 리스트 비교
a = [7, 2]
b = [7, 2, 9]
print(a == b) # False
print(a <= b) # True
print(a < b)  # True

a = [3, 2]
b = [1, 2, 3]
print(a > b) # True

### 순회하기: for와 in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
# brie
# gjetost
# havarti

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
# brie
# I won't eat anything that starts with 'g'

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

cheeses = []
for cheese in cheeses:
    print('This shop has some lobely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')
# This is not much of a cheese shop, is it?

### 여러 시퀀스 순회하기: zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
# Monday : drink coffee - eat banana - enjoy tiramisu
# Tuesday : drink tea - eat orange - enjoy ice cream
# Wednesday : drink beer - eat peach - enjoy pie

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list( zip(english,french) ))
# [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]

print(dict( zip(english, french) ))
# {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

### 리스트 컴프리헨션
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list) # [1, 2, 3, 4, 5]

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)
# [1, 2, 3, 4, 5]

number_list = list(range(1, 6))
print(number_list) # [1, 2, 3, 4, 5]

number_list = [number for number in range(1, 6)]
print(number_list) # [1, 2, 3, 4, 5]

number_list = [number-1 for number in range(1, 6)]
print(number_list) # [0, 1, 2, 3, 4]

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list) # [1, 3, 5]

a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list) # [1, 3, 5]

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

for row, col in cells:
    print(row, col)
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

### 리스트의 리스트
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds[0]) # ['hummingbird', 'finch']
print(all_birds[1]) # ['dodo', 'passenger pigeon', 'Norwegian Blue']
print(all_birds[1][0]) # dodo

# 튜플 컴프리헨션은 없다
number_thing = (number for number in range(1, 6))
print(type(number_thing)) # <class 'generator'>