# 비교하기: if, elif, else
if와 else는 조건이 True인지 False인지 확인하는 선언문이다.
```python
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")
# Woe!

furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")
# It's a yeti.
```
위 코드에서 들여쓰기를 통해 어떻게 짝을 이루는지 알 수 있다.
Large가 True이므로 It's a yeti.가 출력되고 다음 else는 무시된다.

조건 테스트가 두 개 이상이라면 if 문, elif 문, else 문을 사용한다.
```python
color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)
# I've never heard of the color mauve
```
### 파이썬의 비교 연산자
비교 연산자는 불리언 값을 반환한다.
>
|비교 연산자|의미|
|---|---|
|==|같다.|
|!=|다르다.|
|<|보다 작다.|
|<=|보다 작거나 같다.|
|>|보다 크다.|
|>=|보다 크거나 같다.|

동시에 여러 개의 식을 비교해야 한다면 and, or, not과 같으 논리 연산자를 사용할 수 있다.
```python
x = 7
print(5 < x and x < 10) # True
print((5 < x) and (x < 10)) # True

print(5 < x or x < 10) # True
print(5 < x and x > 10) # False
print(5 < x and not x > 10) # True
```

<br/>

---

# True와 False
False 값은 명시적으로 불리언 False라고 할 필요가 없다.

|불리언|false|
|---|---|
|null|none|
|정수()|0|
|부동소수점()|0.0|
|빈 문자열|' '|
|빈 리스트|[ ]|
|빈 튜플|()|
|빈 딕셔너리|{ }|
|빈 셋|Set( )|
이 외의 다른 것들은 True로 간주된다.
```python
some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
# Hey, it's empty!
```

<br/>

---


# 여러 개 비교하기: in
if 문을 사용하여 어떤 문자가 모음인지 확인하려면 다음과 같이 할 수 있다.
```python
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
# o is a vowel
```
**멤버십 연산자** in을 사용하여 위의 식을 간단하게 할 수 있다.
```python
vowels = 'aeiou'
letter = 'o'
print(letter in vowels) # True

if letter in vowels:
    print(letter, 'is a vowel')
# o is a vowel
```
다른 몇 가지 데이터 타입에서도 멤버십 연산자를 사용할 수 있다.
```python
letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set) # True

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list) # True

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple) # True

vowel_string = "aeiou"
print(letter in vowel_string) # True

# 딕셔너리의 경우 값 대신 키(:의 왼쪽)를 본다.
vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala', 'o':'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict) # True
```

<br/>

---

# 새로운 기능: 바다코끼리 연산자
파이썬 3.8의 새로운 **바다코끼리 연산자**의 형식은 다음과 같다.
```python
이름 := 표현식
```
일반적인 할당과 테스트는 두 단계를 거친다.
```python
tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# A fitting tweet
```
바다코끼리 연산자는 할당과 테스트를 한 단계로 줄일 수 있다.
```python
tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >=0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# A fitting tweet
```
바다코끼리 연산자는 for 문과 while 문에서도 사용한다.


