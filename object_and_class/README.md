# 객체란 무엇인가?
객체는 데이터(변수, 속성)와 코드(함수, 메서드)를 포함하는 커스텀 자료구조다.
객체는 어떤 구체적인 것의 유일한 인스턴스를 나타낸다.
객체를 명사로, 메서드를 동사로 생각하면 된다.
객체는 개별 사물을 나타내며 해당 메스드는 다른 사물과 상호작용하는 방법을 정의한다.

<br/>

---

# 간단한 객체
### 클래스 선언하기: class
아무도 만들어본 적이 없는 새 객체를 생성하기 위해서 객체에 포함된 내용을 나타내는 클래스를 정의한다.
객체를 플라스틱 박스에 비유하면 클래스는 상자를 만드는 틀에 비유할 수 있다.

다음의 둘 다 빈 클래스이다. 객체를 생성하기 위한 최소한의 정의다.
```python
class Cat():
    pass
    
class Cat:
    pass
```

함수처럼 클래스 이름을 호출하여 클래스로부터 객체를 생성할 수 있다.
```python
# Cat()은 Cat 클래스로부터 개별 객체를 생성한다.
# 이런 개체를 a_cat, another_cat 이름에 할당한다.
# 하지만 Cat클래스는 빈 클래스이기 때문에 생성한 객체만 존재할 뿐 아무것도 할 수 없다.
a_cat = Cat()
another_cat = Cat()
```

<br/>

### 속성
속성은 클래스나 객체 내부의 변수다.
객체나 클래스가 생성되는 동안이나 이후에 속성을 할당할 수 있다.
속성은 다른 객체일 수 있다.
```python
class Cat:
    pass

a_cat = Cat()
print(a_cat)
# <__main__.Cat object at 0x0000021F191A63F0>

another_cat = Cat()
print(another_cat)
# <__main__.Cat object at 0x0000021F191A64B0>
```
객체에 속성을 할당 할 수 있다.
```python
a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat
```
할당한 속성에 접근할 수 있다.
```python
print(a_cat.age) # 3
print(a_cat.name) # Mr. Fuzzybuttons
print(a_cat.nemesis)
# <__main__.Cat object at 0x0000019E59A66840>
```

nemesis 속성은 다른 Cat 객체를 참조하므로 접근할 수 있지만,
다른 객체에는 name 속성이 할당되지 않는다.
```python
a_cat.nemesis.name
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Cat' object has no attribute 'name'
```
다른 객체에 name 속성을 할당한다.
```python
a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name) # Mr. Bigglesworth
```
간단한 객체에서도 여러 속성을 저장하는 데 사용할 수 있다.
리스트나 딕셔너리와 같은 자료구조를 사용하는 대신 여러 객체를 사용하여 다른 값을 저장할 수 있다.

속성을 이야기할 때, 일반적으로 객체 속성을 의미한다.
클래스 속성도 있다.

<br/>

### 메서드
메서드는 클래스 또는 객체의 함수다.

<br/>

### 초기화
객체를 생성할 때 속성을 할당하려면 객체 초기화 메서드 `__init__()`를 사용한다.
```python
class Cat:
    def __init__(self):
        pass
```
`__init__()`는 클래스 정의에서 개별 객체를 초기화하는 특수 메서드다.
`__init__()`을 정의할 때 첫 번째 매개변수 이름은 self이어야 한다.
self는 예약어는 아니지만 일반적으로 사용한다.
```python
class Cat():
    def __init__(self, name):
        self.name = name
```
이제 name 매개변수에 문자열을 전달하여 Cat 클래스로부터 객체를 생성할 수 있다.
```python
furball = Cat('Grumpy')

print('Our latest addition: ', furball.name)
# Our latest addition:  Grumpy
```
Cat 클래스 정의에서 name 속성을 self.name으로 접근하는 것을 기억해야 한다.
모든 클래스 정의에서 `__init__()` 메서드를 가질 필요는 없다.
`__init__()`는 초기화 메서드라고 생각하면 된다.

<br/>

---

# 상속
기존 클래스를 수정하면 클래스가 더 복잡해질 것이고, 코드를 잘못 건드려 수행할 수 없게 만들 수 있다. 
이 때 상속을 사용할 수 있다.
기존 클래스에서 일부를 추가하거나 변경하여 새 클래스를 생성한다.
상속을 이용하면 새로운 클래스는 기존 클래스를 복사하지 않고, 기존 클래스의 모든 코드를 사용할 수있다.

### 부모 클래스 상속받기
기존 클래스는 부모, 슈퍼, 베이스 클래스라고 부른다.
새 클래스는 자식, 서브, 파생된 클래스라고 부른다.
```python
# 빈 클래스 Car를 정의하고
# Car의 서브 클래스 Yugo를 정의한다.
# 괄호 안에 부모 클래스의 이름을 지정한다.
class Car():
    pass

class Yugo(Car):
    pass
```

issubclass() 함수를 사용하여 다른 클래스에서 파생되었는지 확인할 수 있다.
```python
print(issubclass(Yugo, Car)) # True
```
각 클래스로부터 객체를 생성한다.
```python
give_me_a_car = Car()
give_me_a_yugo = Yugo()
```
자식 클래스는 부모 클래스를 구체화한 것이다.
give_me_a_yugo 객체는 Yugo 클래스의 인스턴스이고, Car 클래스가 할 수 있는 것을 상속받는다.
```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass
```
클래스로부터 객체를 만들고 exclaim() 메서드를 호출한다.
```python
give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
# I'm a Car!

give_me_a_yugo.exclaim()
# I'm a Car!
```

<br/>

### 메서드 오버라이드
```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
```
두 클래스의 객체를 생성한다.
```python
give_me_a_car = Car()
give_me_a_yugo = Yugo()
```
각 객체의 exclaim() 메서드를 호출한다.
```python
give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm a Yugo! Much like a Car, but more Yugo-ish
```
위 예제에서 exclaim() 메서드를 **오버라이드** 했다.
`__init__()` 메서드를 포함한 모든 메서드를 오버라이드 할 수 있다.
```python
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        seif.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
```
이러한 경우 `__init__()` 초기화 메서드는 부모 클래스의 Person과 같은 인수를 취하지만, 객체의 인스턴스 내부에서는 다른 name 값을 저장한다.
```python
print(person.name)
# Fudd
print(doctor.name)
# Doctor Fudd
print(lawyer.name)
# Fudd, Esquire
```

<br/>

### 메서드 추가하기
자식 클래스도 부모 클래스에 없는 메서드를 추가할 수 있다.
```python
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")
```
Car와 Yugo 객체를 생성한다.
```python
give_me_a_car = Car()
give_me_a_yugo = Yugo()
```

Yugo 객체는 need_a_push() 메서드 호출에 대답할 수 있다.
```python
give_me_a_yugo.need_a_push()
# A little help here?
```

그러나 제네릭 Car 객체는 그렇게 할 수 없다.
```python
give_me_a_car.need_a_push()
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Car' object has no attribute 'need_a_push'
```

<br/>

### 부모에게 도움받기: super()
자식 클래스에서 부모 클래스를 호출하고 싶다면 super() 메서드를 사용하면 된다.
```python
class Person():
    def __init__(self, name):
        self.name = name
        
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
```
자식 클래스에서 `__init__()` 메서드를 정의하면 부모 클래스의 `__init__()` 메서드를 대체하는 것이기 때문에 더이상 자동으로 부모 클래스의 `__init__()` 메서드가 호출되지 않는다.
그러므로 이것을 명시적으로 호출해야 한다.
```python
bob = EmailPerson('Bob Frapples', 'bob@rapples.com')
```

객체의 속성에 접근할 수 있다.
```python
print(bob.name) # Bob Frapples
print(bob.email) # bob@rapples.com
```
super() 메서드를 사용하여 Persoin 클래스에서 일반 Person 객체와 같은 방식으로 동작하게 만들었다.
super() 메서드에 대한 또 다른 이점은 Person 클래스의 정의가 바뀌면 Person 클래스로부터 상속받은 EmailPerson 클래스의 속성과 메서드에 변경 사항이 반영된다.

자식 클래스가 자신의 방식으로 무언가를 처리하지만, 부모 클래스로부터 무언가가 필요할 때 super() 메서드를 사용한다.

<br/>

### 다중 상속
실제로 객체는 여러 부모 클래스를 상속받을 수 있다.
클래스가 가지고 있지 않은 메서드 또는 속성을 참조하면 파이썬은 모든 부모 클래스를 조사한다.
각 파이썬 클래스에는 특수 메서드 mro()가 있다.
이 메서드는 해당 클래스 객체에 대한 메서드 또는 속성을 찾는 데 필요한 클래스의 리스트를 반환한다.
`__mro__`라는 유사한 속성은 해당 클래스의 튜플이다.
위 경우 먼저 선언된 부모 클래스를 상속받는다.
```python
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
```

Mule 클래스에서 메서드나 속성을 찾을 때 순서는 다음과 같다.
- 객체 자신(Mule 타입)
- 객체의 클래스(Mule)
- 클래스의 첫 번째 부모 클래스(Donkey)
- 클래스의 두 번째 부모 클래스(Horse)
- 부모의 부모 클래스(Animal)

선언 순서를 제외하고 Hinny 클래스도 같다.
```python
print(Mule.mro())
# [<class '__main__.Mule'>, <class '__main__.Donkey'>, 
# <class '__main__.Horse'>, <class '__main__.Animal'>, <class 'object'>]

print(Hinny.mro())
# [<class '__main__.Hinny'>, <class '__main__.Horse'>, 
# <class '__main__.Donkey'>, <class '__main__.Animal'>, <class 'object'>]
```
```python
mule = Mule()
hinny = Hinny()

print(mule.says()) # Hee-haw!
print(hinny.says()) # Neigh!
```

<br/>

### 믹스인
클래스 정의에 부모 클래스를 추가하여 상속받을 수 있지만 이를 헬퍼의 목적으로만 사용할 수 있다.
다른 상위 클래스와 메서드를 공유하지 않으면 이전 절에서 언급한 메서드 해석 순서의 모호성을 피한다.
이러한 부모 클래스를 믹스인 클래스라고도 한다.
로깅과 같은 '사이드'작업에서 이를 사용할 수 있다.
```python
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
```

<br/>

---

# 자신: self
파이썬은 적절한 객체의 속성과 메서드를 찾기 위해 self 인수를 사용한다.
```python
# a_car 객체의 Car 클래스를 찾는다.
# a_car 객체를 Car 클래스 exclaim() 메서드의 self 매개변수에 전달한다.
a_car = Car()
a_car.exclaim()
# I'm a Car!
```

<br/>

---

# 속성 접근

### 직접 접근
속성 값을 직접 가져와 설정할 수 있다.
```python
class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck('Daffy')
print(fowl.name) # Daffy

# 그러나 누군가 잘못 수정한다면?
fowl.name = 'Daphne'
print(fowl.name) # Daphne
```
다음 두 절에서 위 예제와 같이 수정하지 못하도록 속성에 대한 접근 프라이버시를 얻는 방법을 살펴본다.

### Getter/Setter 메서드
파이썬에는 private 속성이 없지만 조금의 프라이버시를 얻기 위해서 애매한 속성 이름을 가진 Getter/Setter 메서드를 작성할 수 있다.(가장 좋은 해결책은 프로퍼티를 사용하는 것이다.)
```python
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
```

<br/>

### 속성 접근을 위한 프로퍼티
속성 프라이버시를 위한 파이써닉한 방법은 프로퍼티를 사용하는 것이다.
두 방법으로 프로퍼티를 사용할 수 있다.
첫 번째 방법은 name = property(get_name, set_name) 구문을 클래스 정의 마지막 줄에 추가하는 것이다.
```python
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
```
Getter/Setter 메서드는 여전히 동작한다.
```python
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
```
그러나 이제 속성 이름을 사용하여 hidden_name 속성을 가져오거나 설정할 수 있다.
```python
don = Duck('Donald')
print(don.name)
# inside the getter
# Donald
don.name = 'Donna'
# inside the setter
print(don.name)
# inside the getter
# Donna
```

<br/>


두 번째 방법은 데커레이터를 추가하고, 두 메서드 이름을 name으로 변경한다.
- getter 메서드 앞에 @property 데커레이터를 쓴다.
- setter 메서드 앞에 @name.setter 데커레이터를 쓴다.
```python
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
```
속성처럼 name에 접근할 수 있다.
```python
fowl = Duck('Howard')
print(fowl.name)
# inside the getter
# Howard
fowl.name = 'Donald'
# inside the setter
print(fowl.name)
# inside the getter
# Donald
```

<br/>

### 계산된 값의 프로퍼티
프로퍼티는 계산된 값을 참조할 수 있다.
```python
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
```
radius 속성의 초깃값 5와 Circle 객체를 만든다.
```python
c = Circle(5)
print(c.radius) # 5
```
radius와 같은 속성을 계산된 diameter 프로퍼티로 참조할 수 있다.
```python
print(c.diameter) # 10
```
radius 속성은 언제든지 바꿀 수 있다.
```python
c.radius = 7
print(c.diameter) # 14
```
속성에 대한 setter 프로퍼티를 명시하지 않으면 외부로부터 이 속성을 설정할 수 없다.
이는 읽기전용 속성이다.
```python
c.diameter = 20
# Traceback (most recent call last):
# ~~~
# AttributeError: property 'diameter' of 'Circle' object has no setter
```

<br/>

### 프라이버시를 위한 네임 맹글링
파이썬은 클래스 정의 외부에서 볼 수 없도록 하는 속성에 대한 네이밍 컨벤션이 있다.
속성 이름 앞에 언더바 두개를 붙이면 된다.
```python
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
```
```python
fowl = Duck('Howard')
print(fowl.name)
# inside the getter
# Howard
fowl.name = 'Donald'
# inside the setter
print(fowl.name)
# inside the getter
# Donald
```
아무런 문제가 없어 보이나 `__name` 속성에 바로 접근할 수 없다.
```python
fowl.__name
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Duck' object has no attribute '__name'. Did you mean: 'name'?
```
이 네이밍 컨벤션은 속성을 private로 만들지 않았지만, 파이썬은 이 속성이 외부 코드에서 발견될 수 없도록 이름을 맹글링했다.
다음과 같이 접근할 수 있다.
```python
print(fowl._Duck__name) # Donald
```
inside the getter를 출력하지 않았다.
완벽하게 보호할 수는 없지만 네임 맹글링은 속성의 의도적인 직접 접근을 어렵게 만든다.

<br/>

### 클래스와 객체 속성
클래스에 속성을 할당할 수 있고 해당 속성을 자식 객체로 상속된다.
```python
class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color) # red
print(blueberry.color) # red
```

그러나 자식 객체의 속성을 변경하면 클래스 속성에 영향을 미치지 않는다.
```python
blueberry.color = 'blue'
print(blueberry.color) # blue
print(Fruit.color) # red
```
클래스 속성을 변경해도 기존 자식 객체는 영향을 미치지 않는다.
```python
Fruit.color = 'orange'
print(Fruit.color) # orange
print(blueberry.color) # blue

new_fruit = Fruit()
print(new_fruit.color) # orange
```

<br/>

---

# 메서드 타입
어떤 메서드는 클래스의 일부이고, 어떤 메서드는 해당 클래스에서 작성된 객체의 일부이다.
- 메서드 앞에 데커레이터가 없다면 이것은 **인스턴스 메서드**다.
첫 번째 인수는 객체 자신을 참조하는 self다.
- 메서드 앞에 @classmethod 데커레이터가 있다면 **클래스 메서드**다.
첫 번째 인수는 cls(또는 예약어인 class가 아닌 다른 것)이다.
클래스 자체를 참조한다.
- 메서드 앞에 @staticmethod 데커레이터가 있다면 **정적 메서드**다.
첫 번째 인수는 위와 같이 자신의 객체나 클래스가 아니다.

### 인스턴스 메서드
클래스 정의에서 메서드의 첫 번째 인수가 self라면 이 메서드는 인스턴스 메서드다.
일반적인 클래스를 새성할 때의 메서드 타입이다.
인스턴스 메서드의 첫 번째 매개 변수는 self이고, 파이썬은 이 메서드를 호출할 때 객체를 전달한다.

<br/>

### 클래스 메서드
대조적으로 클래스 메서드는 클래스 전체에 영향을 미친다.
클래스에 대한 어떤 변화는 모든 객체에 영향을 미친다.
@classmethod 데커레이터가 있다면 클래스 메서드다.
첫 번째 매개변수는 클래스 자신이다.
보통 cls로 쓴다.
```python
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
```
self.count(객체 인스턴스 속성)를 참조하지 않고 A.count(클래스 속성)를 참조했다.
kids() 메서드에서 A.count를 사용하지 않고 cls.count를 사용했다.

<br/>

### 정적 메서드
정적 메서드는 클래스나 객체에 영향을 미치지 못한다.
편의를 위해 존재한다.
@staticmethod 데커레이터가 있고 첫 번째 매개변수로 self나 cls가 없다.
```python
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWepon has been brought th you by Acme')

CoyoteWeapon.commercial()
# This CoyoteWepon has been brought th you by Acme
```
이 메서드를 접근하기 위해 클래스에서 객체를 생성할 필요가 없다.

<br/>

# 덕 타이핑
파이썬은 다형성을 느슨하게 구현했다.
클래스에 상관없이 같은 동작을 다른 객체에 적용할 수 있다는 의미다.
```python
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
```
파이썬은 자동으로 부모 클래스 Quote의 `__init__()` 메서드를 호출해서 인스턴스 변수 person과 words를 저장한다.
그러므로 자식 클래스에서 생성된 객체의 self.words에 접근할 수 있다.
```python
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
# Elmer Fudd says: I'm hunting wabbits.

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
# Bugs Bunny says: What's up, doc?

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())
# Daffy Duck says: It's rabbit season!
```
서로 다른 says() 메서드는 세 클래스에 대해 서로 다른 동작을 제공한다.
객체 지향 언어에서 전통적인 다형성의 특징이다.
더 나아가 파이썬은 who()와 says() 메서드를 갖고 있는 모든 객체에서 이 메서드를 실행할 수 있게 해준다.

Quoto 클래스와 관계없는 BabblingBrook 클래스를 정의해본다.
```python
class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()
```
obj 인수와 who()와 says() 메서드를 실행해본다.
```python
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
```
brook 객체는 다른 객체와 전혀 관계없다.
이러한 행위를 덕 타이핑이라고 부른다.

<br/>

---

# 매직 메서드
이 메서드의 이름은 언더바 두개로 시작하고 끝난다.
(이미 `__init__()`메서드를 사용했다.)

다음 예제는 평범한 메서드 equal()을 사용한다.
```python
class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
```
세 개의 서로 다른 텍스트 문자열로 객체를 생성한다.
```python
first = Word('ha')
second = Word('HA')
third = Word('eh')
```
문자열 'ha'와 'HA'를 소문자로 바꾸면 이 둘은 똑같다.
```python
print(first.equals(second)) # True

print(first.equals(third)) # False
```

equal() 메서드를 특수 이름의 `__eq__()` 메서드로 바꿔본다.
```python
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
```
```python
first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second) # True
print(first == third) # False
```
`__eq__()`는 같은지 판별하는 파이썬의 특수 메서드 이름이다.

> # 유용한 매직 메서드의 이름
### 비교 연산을 위한 매직 메서드
|메서드|설명|
|---|---|
|`__eq__(self, other)`|self == other|
|`__ne__(self, other)`|self != other|
|`__lt__(self, other)`|self < other|
|`__gt__(self, other)`|self > other|
|`__le__(self, other)`|self <= other|
|`__ge__(self, other)`|self >= other|
>
### 산술 연산을 위한 매직 메서드
|메서드|설명|
|---|---|
|`__add__(self, other)`|self + other|
|`__sub__(self, other)`|self - other|
|`__mul__(self, other)`|self * other|
|`__floordiv__(self, other)`|self // other|
|`__truediv__(self, other)`|self / other|
|`__mod__(self, other)`|self % other|
|`__pow__(self, other)`|self ** other|
- `__add__()`, `__sub__()` 같은 산술 연산자의 사용에는 제한이 없다.
>
### 기타 매직 메서드
|메서드|설명|
|---|---|
|`__str__(self)`|str(self)|
|`__repr__(self)`|repr(self)|
|`__len__(self)`|len(self)|
>
- 매직 메서드를 더 알고 싶다면 파이썬 문서(http://bit.ly/pydocs-smn)를 참조한다.


`__str__()` 또는 `__repr__()`을 정의되어있지 않다면 객체는 기본 문자열을 출력한다.
```python
first = Word('ha')
print(first)
# <__main__.Word object at 0x000002038EAF42C0>
```

```python
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
```

<br/>

---

# 애그리게이션과 콤퍼지션
정교한 상속 계층 구조보다 콤퍼지션 혹은 애그리게이션의 사용이 더 적절한 경우가 있다.
```python
# 오리는 조류(상속)이지만 꼬리(콤퍼지션)를 갖고 있다.
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
```
애그리게이션은 관계를 표현하지만 조금 더 느슨하다.
한 객체는 다른 객체를 사용하지만, 둘 다 독립적으로 존재한다.

<br/>

---

# 객체는 언제 사용할까?
- 비슷한 행동(메서드)을 하지만 내부 상태(속성)가 다른 개별 인스턴스가 필요할 때, 객체는 매우 유용하다.
- 클래스는 상속을 지원하지만, 모듈은 상속을 지원하지 않는다.
- 어떤 한 가지 일만 수행한다면 모듈이 가장 좋은선택일 것이다.
프로그램에서 파이썬 모듈이 참조된 횟수에 상관없이 단 하나의 복사본만 불러온다.
- 여러 함수에 인수로 전달하는 여러 변수가 있다면, 클래스를 정의하는 것이 더 좋다.
- 가장 간단한 문제 해결법을 사용한다.
딕셔너리, 리스트, 튜플은 모듈보다 더 작고 간단하며 빠르다.
그리고 일반적으로 모듈은 클래스보다 더 간단하다.
- 새로운 대안은 데이터 클래스다.

<br/>

---

# 네임드 튜플
네임드 튜플은 튜플의 서브클래스다.
이름(.name)과 위치([offset])로 값에 접근할 수 있다.

네임드 튜플을 쓰기 전에 모듈을 불러와야 한다.
```python
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
# Duck(bill='wide orange', tail='long')
print(duck.bill) # wide orange
print(duck.tail) # long
```

딕셔너리에서 네임드 튜플을 만들 수 있다.
```python
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
# Duck(bill='wide orange', tail='long')
```
`**parts`는 키워드 인수다.
parts 딕셔너리에서 키와 값을 추출하여 Duck()의 인수로 제공한다.

네임드 튜플은 불변이다.
하지만 필드를 바꿔 또 다른 네임드 튜플을 반환할 수 있다.
```python
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
# Duck(bill='crushing', tail='magnificent')
```
딕셔너리로 정의한다.
```python
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
# {'bill': 'wide orange', 'tail': 'long'}
```
딕셔너리에 필드를 추가한다.
```python
duck_dict['color'] = 'green'
print(duck_dict)
# {'bill': 'wide orange', 'tail': 'long', 'color': 'green'}
```
딕셔너리는 네임드 튜플이 아니다.
```python
duck.color = 'green'
# Traceback (most recent call last):
# ~~~
# AttributeError: 'Duck' object has no attribute 'color'
```

> ### 네임드 튜플의 특징
- 불변 객체처럼 행동한다.
- 객체보다 공간 효율성과 시간 효율성이 더 좋다.
- 딕셔너리 형식의 대괄호 대신 온점표기법으로 속성을 접근할 수 있다.
- 네임드 튜플을 딕셔너리의 키처럼 쓸 수 있다.

<br/>

---

# 데이터 클래스
파이썬 3.7부터 데이터 클래스를 지원한다.
```python
class TeenyClass():
    def __init__(self, name):
        self.name = name

teeny = TeenyClass('itsy')
print(teeny.name) # itsy
```
데이터 클래스를 사용하여 같은 작업을 한다면 조금 다르게 보인다.
```python
from dataclasses import dataclass
@dataclass
class TeenyDataClass:
    name: str

teeny = TeenyDataClass('bitsy')
print(teeny.name) # bitsy
```
@dataclass 데커레이터 외에 이름: 타입과 같은 형식의 변수 어노테이션을 사용하여 클래스 속성을 정의한다.

데이터 클래스 객체를 생성할 때, 클래스에 지정된 순서대로 인수를 제공하거나 이름이 지정된 인수를 임의의 순서로 제공한다.
```python
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
```

일반 객체와 같이 객체 속성을 참조할 수 있다.
```python
print(duck.habitat) # lake
print(snowman.teeth) # 46
```


