# 파이썬 데이터는 객체다
파이썬에서 객체는 최소한 다음을 포함하는 데이터이다.
- 타입 정의
- 다른 객체와 구별하기 위한 고유 ID
- 타입과 연관된 값
- 객체의 사용 빈도를 추적하는 참조 횟수

### 타입
|이름|타입|가변|예제|
|---|---|---|---|
|불리언|bool|아니오|True, False|
|정수|int|아니오|47, 25000,25_000|
|부동소수점|float|아니오|3.14, 2.7e5|
|복소수|complex|아니오|3j, 5 + 9j|
|텍스트 문자열|str|아니오|'alas', "alack", '''a verse attack'''|
|리스트|list|예|['Winken', 'Blinken', 'Nod']|
|튜플|tuple|아니오|(2, 4, 8)|
|바이트|bytes|아니오|b'ab/xff|
|바이트 배열|bytearray|예|bytearray(...)|
|셋|set|예|set([3, 5, 7])|
|프로즌 셋|frozenset|아니오|frozenset(['Elsa', 'Otto'])|
|딕셔너리|dict|예|{'game': 'bingo', 'dog': 'dingo', 'drummer': 'Ringo'}|

>### 가변성
- 타입에 따라 데이터 값을 변경하거나 일정하게 유지할 수 있다.
- 파이썬은 강타입 언어다. ( 값은 변경 가능하지만 객체의 타입은 변경할 수 없다. )

<br/>

---
# 파이썬에서 데이터 값을 명시하는 방법
- 리터럴
- 변수

### 변수
파이썬 변수 이름에는 몇 가지 규칙이 있다.
- 소문자, 대문자, 숫자, 언더바( _ )만 사용할 수 있다.
- 대소 문자를 구분한다.
- 숫자가 아닌 문자나 언더바로 시작한다.
- 언더바로 시작하는 이름은 특별하게 취급한다.
- 파이썬 예약어(키워드)는 사용할 수 없다.
> ### 예약어
||||||
|---|----|---|---|---|
|False|await|else|import|pass|
|None|break|except|in|raise|
|True|class|finally|is|return|
|and|continue|for|lambda|try|
|as|def|from|nonlocal|while|
|assert|del|global|not|with|
|async|elif|if|or|yield|

### 할당
파이썬은 =를 사용해 변수에 값을 할당한다.

### 변수는 장소가 아니라 이름이다
변수는 단지 이름이다.
할당은 값을 복사하지 않는다.
단지 데이터를 포함하는 객체에 이름을 붙인다.
이름은 객체 자체가 아닌 객체에 대한 참조이다.
파이썬은 더 이상 필요하지 않은 공간의 메모리를 재사용하는 가비지 컬렉터가 있다.
```python
a = 7
b = a
print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>
print(type(99.9)) # <class 'float'>
print(type('abc')) # <class 'str'>
```

### 여러 이름 할당하기
```python
two = deux = zwei = 2
print(two) # 2
print(deux) # 2
print(zwei) # 2
```

### 복사
기존 변수 a를 새 변수 b에 할당하면, 변수 b는 변수 a와 같은 객체를 가리키게 된다.
a 또는 b 태그(변수)를 선택하여 두 변수를 출력하면 같은 객체를 얻는다.
정수와 같이 객체가 불변한 경우 값을 변경할 수 없으므로, 두 이름 모두 읽기 전용이 된다.
```python
x = 5
print(x) # 5
y = x
print(y) # 5
x = 29
print(x) # 29
print(y) # 5

```
두 이름이 모두 가변 객체를 가리킨다면 두 이름 중 하나를 통해 객체 값을 변경할 수 있으며, 두 이름을 사용할 때 변경된 값이 사용된다. (리스트는 가변 값의 배열이다.)
```python
a = [2, 4, 6]
b = a
print(a) # [2, 4, 6]
print(b) # [2, 4, 6]

a[0] = 99
print(a) # [99, 4, 6]
print(b) # [99, 4, 6]
```
리스트는 여전히 리스트 타입이지만, 리스트 값은 변할 수 있다.



