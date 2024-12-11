### 클래스 선언하기: class
class Cat():
    pass

class Cat:
    pass

a_cat = Cat()
another_cat = Cat()

### 속성
class Cat:
    pass

a_cat = Cat()
print(a_cat)
# <__main__.Cat object at 0x0000021F191A63F0>

another_cat = Cat()
print(another_cat)
# <__main__.Cat object at 0x0000021F191A64B0>

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat

print(a_cat.age) # 3
print(a_cat.name) # Mr. Fuzzybuttons
print(a_cat.nemesis)
# <__main__.Cat object at 0x0000019E59A66840>

# a_cat.nemesis.name
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Cat' object has no attribute 'name'

a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name) # Mr. Bigglesworth

class Cat:
    def __init__(self):
        pass

class Cat():
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')

print('Our latest addition: ', furball.name)
# Our latest addition:  Grumpy

### 부모 클래스 상속받기
class Car():
    pass

class Yugo(Car):
    pass

print(issubclass(Yugo, Car)) # True

give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
# I'm a Car!

give_me_a_yugo.exclaim()
# I'm a Car!

### 메서드 오버라이드
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm a Yugo! Much like a Car, but more Yugo-ish

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
# Fudd
print(doctor.name)
# Doctor Fudd
print(lawyer.name)
# Fudd, Esquire

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()
# A little help here?

# give_me_a_car.need_a_push()
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Car' object has no attribute 'need_a_push'

### 부모에게 도움받기: super()
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@rapples.com')

print(bob.name) # Bob Frapples
print(bob.email) # bob@rapples.com

### 다중 상속
class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'
    
class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

print(Mule.mro())
# [<class '__main__.Mule'>, <class '__main__.Donkey'>, 
# <class '__main__.Horse'>, <class '__main__.Animal'>, <class 'object'>]

print(Hinny.mro())
# [<class '__main__.Hinny'>, <class '__main__.Horse'>, 
# <class '__main__.Donkey'>, <class '__main__.Animal'>, <class 'object'>]

mule = Mule()
hinny = Hinny()

print(mule.says()) # Hee-haw!
print(hinny.says()) # Neigh!

### 믹스인
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"

t.dump()
# {'age': 'eldritch', 'feature': 'ichor', 'name': 'Nyarlathotep'}

# 자신: self

a_car = Car()
a_car.exclaim()
# I'm a Car!

# 속성 접근

### 직접 접근
class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck('Daffy')
print(fowl.name) # Daffy

fowl.name = 'Daphne'
print(fowl.name) # Daphne

### Getter/Setter 메서드
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

don = Duck('Donald')
print(don.get_name())
# inside the getter
# Donald
print(don.set_name('Donna'))
# inside the setter
# None
print(don.get_name())
# inside the getter
# Donna

### 속성 접근을 위한 프로퍼티
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

don = Duck('Donald')
print(don.get_name())
# inside the getter
# Donald
print(don.set_name('Donna'))
# inside the setter
# None
print(don.get_name())
# inside the getter
# Donna

don = Duck('Donald')
print(don.name)
# inside the getter
# Donald
don.name = 'Donna'
# inside the setter
print(don.name)
# inside the getter
# Donna

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)
# inside the getter
# Howard
fowl.name = 'Donald'
# inside the setter
print(fowl.name)
# inside the getter
# Donald

### 계산된 값의 프로퍼티
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    
c = Circle(5)
print(c.radius) # 5

print(c.diameter) # 10

c.radius = 7
print(c.diameter) # 14

# c.diameter = 20
# Traceback (most recent call last):
# ~~~
# AttributeError: property 'diameter' of 'Circle' object has no setter

### 프라이버시를 위한 네임 맹글링
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')

        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)
# inside the getter
# Howard
fowl.name = 'Donald'
# inside the setter
print(fowl.name)
# inside the getter
# Donald

# fowl.__name
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Duck' object has no attribute '__name'. Did you mean: 'name'?

print(fowl._Duck__name) # Donald

### 클래스와 객체 속성
class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color) # red
print(blueberry.color) # red

blueberry.color = 'blue'
print(blueberry.color) # blue
print(Fruit.color) # red

Fruit.color = 'orange'
print(Fruit.color) # orange
print(blueberry.color) # blue

new_fruit = Fruit()
print(new_fruit.color) # orange

### 클래스 메서드
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A haas", cls.count, "little objects.")

easy_a = A()
brezzy_a = A()
wheezy_a = A()
A.kids()
# A haas 3 little objects.

### 정적 메서드
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWepon has been brought th you by Acme')

CoyoteWeapon.commercial()
# This CoyoteWepon has been brought th you by Acme

# 덕 타이핑
# who() 메서드는 저장된 person 문자열의 값을 반환한다.
# says() 메서드는 특정 구두점과 함께 저장된 words 문자열을 반환한다.
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
    
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
    
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
# Elmer Fudd says: I'm hunting wabbits.

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
# Bugs Bunny says: What's up, doc?

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())
# Daffy Duck says: It's rabbit season!

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
# Elmer Fudd says I'm hunting wabbits.
who_says(hunted1)
# Bugs Bunny says What's up, doc?
who_says(hunted2)
# Daffy Duck says It's rabbit season!
who_says(brook)
# Brook says Babble

# 매직 메서드
class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
    
first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second)) # True

print(first.equals(third)) # False

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second) # True
print(first == third) # False

first = Word('ha')
print(first)
# <__main__.Word object at 0x000002038EAF42C0>

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'

first = Word('ha')

# __repr__() 호출
first # Word("ha")

# __str__() 호출
print(first) # ha

# 애그리게이션과 콤퍼지션
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 
                'bill and a', self.tail.length, 'tail')
        
a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)

duck.about()
# This duck has a wide orange bill and a long tail

# 네임드 튜플
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
# Duck(bill='wide orange', tail='long')
print(duck.bill) # wide orange
print(duck.tail) # long

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
# Duck(bill='wide orange', tail='long')

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
# Duck(bill='crushing', tail='magnificent')

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
# {'bill': 'wide orange', 'tail': 'long'}

duck_dict['color'] = 'green'
print(duck_dict)
# {'bill': 'wide orange', 'tail': 'long', 'color': 'green'}

# duck.color = 'green'
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Duck' object has no attribute 'color'

# 데이터 클래스
class TeenyClass():
    def __init__(self, name):
        self.name = name

teeny = TeenyClass('itsy')
print(teeny.name) # itsy

from dataclasses import dataclass
@dataclass
class TeenyDataClass:
    name: str

teeny = TeenyDataClass('bitsy')
print(teeny.name) # bitsy

from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')

print(snowman)
# AnimalClass(name='yeti', habitat='Himalayas', teeth=46)
print(duck)
# AnimalClass(name='duck', habitat='lake', teeth=0)

print(duck.habitat) # lake
print(snowman.teeth) # 46