a = 7
b = a
print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>
print(type(99.9)) # <class 'float'>
print(type('abc')) # <class 'str'>

two = deux = zwei = 2
print(two) # 2
print(deux) # 2
print(zwei) # 2

x = 5
print(x) # 5
y = x
print(y) # 5
x = 29
print(x) # 29
print(y) # 5

a = [2, 4, 6]
b = a
print(a) # [2, 4, 6]
print(b) # [2, 4, 6]

a[0] = 99
print(a) # [99, 4, 6]
print(b) # [99, 4, 6]

