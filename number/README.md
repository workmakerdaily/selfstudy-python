# 불리언
불리언 데이터 타입의 유일한 값은 True와 False이다.
파이썬 특수 함수 bool()은 모든 파이썬 데이터 타입을 불리언으로 변환한다.

0이 아닌 값은 True로 간주한다.
```python
print(bool(True)) # True
print(bool(1)) # True
print(bool(45)) # True
print(bool(-45)) # True
```
0인 값은 False로 간주한다.
```python
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
```

<br/>

---
# 정수
### 리터럴 정수
대화식 인터프리터에서 연속된 숫자는 리터럴 정수로 간주한다.
0을 다른 숫자 앞에 넣을 수는 없다.
```java
print(5) # 5
print(0) # 0
print(05)
# SyntaxError: leading zeros in decimal integer literals are not permitted; 
# use an 0o prefix for octal integers
```

숫자 앞에 기호가 없으면 양수를 의미하며 +기호를 붙여도 여전히 양수이다.
음수는 -기호를 붙인다.
```python
print(123) # 123
print(+123) # 123
print(-123) # -123
```
정수에 쉼표(,)를 사용할 수 없다.
백만이라는 숫자 대신에 튜플을 얻는다.
그러나 언더바( _ )를 사용하면 숫자를 구분할 수 있다.
```python
print(1,000,000) # 1 0 0
print(1_000_000) # 1000000
```
첫 번째 숫자 이후 모든 위치에 언더바가 사용하능하며 언더바는 결과 출력 시 무시된다.

### 정수 연산자
|연산자|설명|예|결과|
|---|---|---|---|
|+|더하기|5 + 8|13|
|-|빼기|90 - 10|80|
|*|곱하기|4 * 7|28|*
|/|부동소수점 나누기|7 / 2|3.5|
|//|정수 나누기(소수점 이하 버림)|7 // 2|3|
|%|나머지|7 % 3|1|
|**|지수|3 ** 4|81|**
0으로 나누면 예외가 발생한다.
```python
print(5 / 0) # ZeroDivisionError: division by zero
```
> ### 소수점을 제외한 몫과 나머지를 동시에 얻는 방법
```python
print(divmod(9,5)) # (1, 4)
```

### 정수와 변수
정수 값이 할당된 변수와 리터럴 정수를 혼합하여 사용할 수 있다.
```python
a = 95
print(a - 3) # 92
```

### 연산 순서
```python
print(2 + 3 * 4) # 14
```
연산 순서 규칙을 모두 외울 필요는 없다.
먼저 수행하고자 하는 계산식에 괄호를 붙이면 된다.


### 진수
정수 앞에 진수를 붙이지 않으면 10진수로 간주한다.
> 
- 2진수 : 0b 혹은 0B
- 8진수 : 0o 혹은 0O
- 16진수 : 0x 혹은 0X
```python
print(10) # 10
print(0b10) # 2
print(0o10) # 8
print(0x10) # 16
```

10진수에서 다른 진수로 계산할 수 있다. (계산 결과는 문자열로 반환된다.)
```python
value = 65
print(bin(value)) # 0b1000001
print(oct(value)) # 0o101
print(hex(value)) # 0x41
```

chr() 함수는 정수를 단일 문자열로 변환하며 ord()함수는 반대로 단일 문자열을 정수로 반환한다.
```python
print(chr(65)) # A
print(ord('A')) # 65
```

### 타입 변환
다른 파이썬 데이터 타입을 정수 타입으로 변환하려면 int()함수를 사용한다.
소수점이 있다면 소수점 이하 숫자는 버리고 정수만 반환한다.
```python
print(int(True)) # 1
print(int(False)) # 0
```
bool()함수를 사용하면 정수에 해당하는 불리언 값을 반환한다.
```python
print(bool(1)) # True
print(bool(0)) # False
```

부동소수점 숫자를 정수로 변환하면 소수점을 버리고 정수를 출력한다.
```python
print(int(98.6)) # 98
print(int(1.0e4)) # 10000

print(bool(1.0)) # True
print(bool(0.0)) # False
```

int() 함수에 숫자가 아닌 다른 것을 변환하면 예외가 발생한다.
```python
print(int('98.6'))
# ValueError: invalid literal for int() with base 10: '98.6'
```

숫자 타입을 섞어서 사용하면, 파이썬은 자동으로 타입 변환을 한다
```python
print(4 + 7.0) # 11.0
```

### 부동소수점 숫자
부동소수점 숫자는 문자 e와 정수인 지수를 포함할 수 있다.
```python
print(5e0) # 5.0
print(5e1) # 50.0
print(5.0e1) # 50.0
print(5.0 * (10 ** 1)) # 50.0
```
부동소수점 숫자로 타입 변환을 위해서 float() 함수를 사용한다.
불리언 값을 정수처럼 간주한다.
```python
print(float(True)) # 1.0
print(float(False)) # 0.0
```
정수에서 부동소수점 숫자로 변환할 때는 간단하게 소수점이 붙는다.
```python
print(float(98)) # 98.0
print(float('99')) # 99.0
```

유효한 부동소수점 수(숫자, 기호, 소수점, 지수)가 있는 문자열을 부동소수점 수로 변환할 수 있다.
```python
print(float('98.6')) # 98.6
print(float('-1.5')) # -1.5
print(float('1.0e4')) # 10000.0
```









