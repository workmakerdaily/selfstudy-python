# 딕셔너리

### 생성하기: {}
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

### 생성하기: dict()

# 일반적인 방법
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
# {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}

# dict() 함수 사용 방법
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)
# {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}

# x = dict(name="Elmer", def="hunter")
# print(x) # SyntaxError: invalid syntax

### 변환하기: dict()
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))
# {'a': 'b', 'c': 'd', 'e': 'f'}

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))
# {'a': 'b', 'c': 'd', 'e': 'f'}

tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(tol))
# {'a': 'b', 'c': 'd', 'e': 'f'}

los = [ 'ab', 'cd', 'ef' ]
print(dict(los))
# {'a': 'b', 'c': 'd', 'e': 'f'}

tos = ('ab', 'cd', 'ef')
print(dict(tos))
# {'a': 'b', 'c': 'd', 'e': 'f'}

### 항목 추가/변경: [key]
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

### 항목 얻기: [key]와 get()
print(some_pythons['John']) # Cleese

# print(some_pythons['Groucho'])
# KeyError: 'Groucho'

print('Groucho' in some_pythons) # False

print(some_pythons.get('John')) # Cleese

print(some_pythons.get('Groucho', 'Not a Python'))
# Not a Python

### 모든 키 얻기: keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
# dict_keys(['green', 'yellow', 'red'])

print(list( signals.keys() ))
# ['green', 'yellow', 'red']


### 모든 값 얻기: values()
print(list( signals.values() ))
# ['go', 'go faster', 'smile for the camera']

### 모든 키-값 얻기: items()
print(list( signals.items() ))
# [('green', 'go'), ('yellow', 'go faster'), ('red', 'smile for the camera')]

### 길이 얻기: len()
print(len(signals)) # 3

### 결합하기: {**a, **b}
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})
# {'a': 'agony', 'b': 'bagels', 'c': 'candy'}

third = {'d': 'donuts'}
print({**first, **second, **third})
# {'a': 'agony', 'b': 'bagels', 'c': 'candy', 'd': 'donuts'}

### 결합하기: update()
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

first = { 'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)

print(first)
# {'a': 1, 'b': 'platypus'}

### 키와 del로 항목 삭제하기
del pythons['Marx']
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Howard': 'Moe'}

del pythons['Howard']
print(pythons)
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}

### 키로 항목을 가져온 뒤 삭제하기: pop()
print(len(pythons)) # 6
print(pythons.pop('Palin')) # Michael
print(len(pythons)) # 5
# print(pythons.pop('Palin')) # KeyError: 'Palin'


print(pythons.pop('First', 'Hugo')) # Hugo
print(len(pythons)) # 5

### 모든 항목 삭제하기: clear()
pythons.clear()
print(pythons) # {}

### 키 멤버십 테스트: in
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 
        'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}

print('Chapman' in pythons) # True
print('Palin' in pythons) # True
print('Gilliam' in pythons) # False

### 할당하기: =
signals = {'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'}

save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
# {'green': 'go', 'yellow': 'go faster', 
# 'red': 'smile for the camera', 'blue': 'confuse everyone'} 

### 얕은 복사: copy()
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

### 깊은 복사: deepcopy()

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

### 딕셔너리 비교
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b) # True
# print(a <= b)
# TypeError: '<=' not supported between instances of 'dict' and 'dict'

a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
print(a == b) # False

### 순회하기: for와 in
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col.Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)
# room
# weapon
# person

for value in accusation.values():
    print(value)
# ballroom
# lead pipe
# Col.Mustard

for item in accusation.items():
    print(item)
# ('room', 'ballroom')
# ('weapon', 'lead pipe')
# ('person', 'Col.Mustard')

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
# Card room has the contents ballroom
# Card weapon has the contents lead pipe
# Card person has the contents Col.Mustard

### 딕셔너리 컴프리헨션
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in word}
print(letter_counts)
# {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter:word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) 
                if letter in vowels}
print(vowel_counts)
# {'e': 1, 'a': 2, 'i': 1, 'o': 4}

# 셋

### 생성하기: set()
empty_set = set()
print(empty_set) # set()

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers) # {0, 2, 4, 6, 8}

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers) # {1, 3, 5, 7, 9}

### 변환하기: set()
print(set( 'letters'))
# {'t', 'l', 'r', 'e', 's'}

print(set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ))
# {'Prancer', 'Mason-Dixon', 'Dancer', 'Dasher'}

print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ))
# {'Ummagumma', 'Atom Heart Mother', 'Echoes'}

print (set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))
# {'cherry', 'orange', 'apple'}

### 길이 얻기: len()
reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
print(len(reindeer)) # 4

### 항목 추가하기: add()
s = set((1, 2, 3))
print(s) # {1, 2, 3}

s.add(4)
print(s) # {1, 2, 3, 4}

### 항목 삭제하기: remove()
s = set((1, 2, 3))
s.remove(3)
print(s) # {1, 2}

### 순회하기: for와 in
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)
# ottoman
# table
# sofa

### 멤버십 테스트: in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
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

### 콤비네이션과 연산자
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

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b) # {2}
print(a.intersection(b)) # {2}

print(bruss & wruss)
# {'kahlua', 'vodka'}

print(bruss | wruss)
# {'cream', 'vodka', 'kahlua'}

print(a - b) # {1}
print(a.difference(b)) # {1}
print(bruss - wruss) # set()
print(wruss - bruss) # {'cream'}

print(a ^ b) # {1, 3}
print(a.symmetric_difference(b)) # {1, 3}
print(bruss ^ wruss) # {'cream'}

print(a <= b) # False
print(a.issubset(b)) # False
print(bruss <= wruss) # True

print(a < b) # False
print(a < a) # False
print(bruss < wruss) # True

print(a >= b) # False
print(a.issuperset(b)) # False
print(wruss >= bruss) # True

print(a > b) # False
print(wruss > bruss) # True

### 셋 컴프리헨션
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set) # {1, 4}

### 불변 셋 생성하기: frozenset()
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
# print(fs.add(4))
# AttributeError: 'frozenset' object has no attribute 'add'

# 지금까지 배운 자료구조
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

# 자료구조 결합하기
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuble_of_lists = marxes, pythons, stooges
print(tuble_of_lists)
# (['Groucho', 'Chico', 'Harpo'], 
# ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# ['Moe', 'Curly', 'Larry'])

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
# [['Groucho', 'Chico', 'Harpo'], 
# ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# ['Moe', 'Curly', 'Larry']]

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
# {'Marxes': ['Groucho', 'Chico', 'Harpo'], 
# 'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 
# 'Stooges': ['Moe', 'Curly', 'Larry']}