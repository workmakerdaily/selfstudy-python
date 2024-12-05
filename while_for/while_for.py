# 반복하기: while
count = 1
while count <= 5:
    print(count)
    count += 1
# 1
# 2
# 3
# 4
# 5

# 중단하기: break
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())
# String to capitalize [type q to quit]: test
# Test
# String to capitalize [type q to quit]: hey, it works Hey, it works
# Hey, it works hey, it works
# String to capitalize [type q to quit]: q

# 건너뛰기: continue
# while True:
#     value = input("Integer, please [q to quit]:")
#     if value == 'q': # 종료
#         break
#     number = int(value)
#     if number % 2 == 0: # 짝수
#         continue
#     print(number, "squared is", number*number)
# Integer, please [q to quit]:1
# 1 squared is 1
# Integer, please [q to quit]:2
# Integer, please [q to quit]:3
# 3 squared is 9
# Integer, please [q to quit]:4
# Integer, please [q to quit]:5
# 5 squared is 25
# Integer, please [q to quit]:q

# break 확인하기: else
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

# 순회하기: for와 in

### while
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
# t
# h
# u
# d

### for와 in
for letter in word:
    print(letter)
# t
# h
# u
# d

# 중단하기: break
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)
# t
# h

# break 확인하기: else
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

# 숫자 시퀀스 생성하기: range()
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

print(list( range(0, 11, 2) )) # [0, 2, 4, 6, 8, 10]