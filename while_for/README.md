# 반복하기: while
```python
count = 1
while count <= 5:
    print(count)
    count += 1
# 1
# 2
# 3
# 4
# 5
```
반복문은 count 변수가 5에서 6으로 증가할 때까지 계속 실행한다.

<br/>

### 중단하기: break
어떤 일이 일어날 때까지 반복하고 싶지만, 어떤 일이 언제 일어나는지 확실하지 않다면 무한 반복문에 break 문을 사용한다.
```python
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
# String to capitalize [type q to quit]: test
# Test
# String to capitalize [type q to quit]: hey, it works Hey, it works
# Hey, it works hey, it works
# String to capitalize [type q to quit]: q
```

<br/>

### 건너뛰기: continue
반복문을 중단하고 싶지 않지만 다음 반복을 건너뛰어야 할 때 사용한다.
```python
while True:
    value = input("Integer, please [q to quit]:")
    if value == 'q': # 종료
        break
    number = int(value)
    if number % 2 == 0: # 짝수
        continue
    print(number, "squared is", number*number)
# Integer, please [q to quit]:1
# 1 squared is 1
# Integer, please [q to quit]:2
# Integer, please [q to quit]:3
# 3 squared is 9
# Integer, please [q to quit]:4
# Integer, please [q to quit]:5
# 5 squared is 25
# Integer, please [q to quit]:q
```

<br/>

### break 확인하기: else
while문이 모두 실행되었지만 발견하지 못했을 때는 else 문이 실행된다.
```python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: # break 문이 호출되지 않은 경우
    print('No even number found')
# No even number found
```

<br/>

---
# 순회하기: for와 in
While 문으로 문자열에 있는 문자를 출력할 수 있다.
```python
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
# t
# h
# u
# d
```
이 코드를 for와 in을 사용하면 다음과 같이 된다.
```python
for letter in word:
    print(letter)
# t
# h
# u
# d
```

<br/>

### 중단하기: break, 건너뛰기: continue
for 문의 break, continue 문은 while 문의 break, continue 문과 똑같이 동작한다.
```python
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)
# t
# h
```

<br/>

### break 확인하기: else
for 문에서 break문이 호출되지 않으면 else 문이 실행된다.
else 문은 break 문에 의해 반복문이 중단되지 않고 모든 항목을 순회했는지 확인할 때 유용한다.
```python
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")
# t
# h
# u
# d
# No 'x' in there.
```

<br/>

### 숫자 시퀀스 생성하기: range()
range() 함수는 리스트나 튜플 같은 자료구조를 생성하여 저장하지 않더라도 특정 범위 내에서 숫자 스트림을 반환한다.
이것은 컴퓨터의 메모리를 전부 사용하지 않고, 프로그램의 충돌없이 아주 큰 범위를 생성할 수 있게 해준다.
range(start, stop, step) 형식을 사용한다.
start를 생략하면 범위는 0에서 시작하며, stop은 꼭 입력해야한다.
step의 기본값은 1이며, -1로 지정하여 끝에서부터 진행할 수 있다.

zip(), range()와 같은 함수는 순회 가능한 객체를 반환한다.
또한 객체를 리스트와 같은 시퀀스로 변환할 수 있다.
```python
for x in range(0,3):
    print(x)
# 0
# 1
# 2
print(list( range(0,3) )) # [0, 1, 2]

for x in range(2, -1, -1):
    print(x)
# 2
# 1
# 0
print(list( range(2,-1, -1) )) # [2, 1, 0]

# 0에서 10까지 2씩 진행하는 짝수 리스트
print(list( range(0, 11, 2) )) # [0, 2, 4, 6, 8, 10]
```

