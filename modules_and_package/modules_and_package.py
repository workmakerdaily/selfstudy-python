import sys
for place in sys.path:
    print(place)
# C:\python\modules_and_package
# C:\Users~~~
# C:\Users~~~

import math
print(math.pi)
# 3.141592653589793
math.pi = 3.0
print(math.pi)
# 3.0


### 누락된 키 처리하기: setdefault()와 defaultdict()
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2}

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon) # 12
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}

helium = periodic_table.setdefault('Helium', 947)
print(helium) # 2
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
print(periodic_table['Lead']) # 0
print(periodic_table)
# defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})

from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print(bestiary['A']) # Abominable Snowman
print(bestiary['B']) # Basilisk
print(bestiary['C']) # Huh?

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E']) # Huh?

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
# spam 3
# eggs 1

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
# Counter({'spam': 3, 'eggs': 1})

print(breakfast_counter.most_common())
# [('spam', 3), ('eggs', 1)]
print(breakfast_counter.most_common(1))
# [('spam', 3)]

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

print(lunch_counter & breakfast_counter)
# Counter({'eggs': 1})

print(lunch_counter | breakfast_counter)
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})

### 키 정렬하기: OrderedDict()
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

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar')) # True
print(another_palindrome('halibut')) # False

### 코드 구조 순회하기: itertools
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
# 1
# 2
# a
# b

# import itertools
# for item in itertools.cycle([1, 2]):
    # print(item)
# 1
# 2
# 1
# 2
# 1
# 2
# 1
# ...

import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
# 1
# 3
# 6
# 10

import itertools
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
# 1
# 2
# 6
# 24

### 깔끔하게 출력하기: pprint()
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

print(quotes)
# OrderedDict({'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'})

pprint(quotes)
# OrderedDict({'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!'})

### 임의값 얻기
from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))
# bacon
print(choice(['a', 'one', 'and-a', 'two']))
# one
print(choice(range(100)))
# 60
print(choice('alphabet'))
# t

from random import sample
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
# [9, 'bacon', 23]
print(sample(['a', 'one', 'and-a', 'two'], 2))
# ['one', 'two']
print(sample(range(100), 4))
# [78, 96, 4, 51]
print(sample('alphabet', 7))
# ['a', 'p', 'a', 'b', 'h', 't', 'e']

from random import randint
print(randint(38, 74)) # 57
print(randint(38, 74)) # 48
print(randint(38, 74)) # 52

from random import randrange
print(randrange(38, 74)) # 45
print(randrange(38, 74, 10)) # 68
print(randrange(38, 74, 10)) # 38

from random import random
print(random()) # 0.02930071684611002
print(random()) # 0.16549406290876278
print(random()) # 0.06019680478611067