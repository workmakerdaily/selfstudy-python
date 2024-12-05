print(bool(True)) # True
print(bool(1)) # True
print(bool(45)) # True
print(bool(-45)) # True

print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False

print(5) # 5
print(0) # 0
# print(05)
# SyntaxError: leading zeros in decimal integer literals are not permitted; 
# use an 0o prefix for octal integers

print(123) # 123
print(+123) # 123
print(-123) # -123
print(1,000,000) # 1 0 0
print(1_000_000) # 1000000

# print(5 / 0) # ZeroDivisionError: division by zero

a = 95
print(a - 3) # 92

print(divmod(9,5)) # (1, 4)

print(2 + 3 * 4) # 14

print(10) # 10
print(0b10) # 2
print(0o10) # 8
print(0x10) # 16

value = 65
print(bin(value)) # 0b1000001
print(oct(value)) # 0o101
print(hex(value)) # 0x41

print(chr(65)) # A
print(ord('A')) # 65

print(int(True)) # 1
print(int(False)) # 0

print(bool(1)) # True
print(bool(0)) # False

print(int(98.6)) # 98
print(int(1.0e4)) # 10000

# print(int('98.6'))
# ValueError: invalid literal for int() with base 10: '98.6'

print(4 + 7.0) # 11.0

print(5e0) # 5.0
print(5e1) # 50.0
print(5.0e1) # 50.0
print(5.0 * (10 ** 1)) # 50.0

print(float(True)) # 1.0
print(float(False)) # 0.0

print(float(98)) # 98.0
print(float('99')) # 99.0

print(float('98.6')) # 98.6
print(float('-1.5')) # -1.5
print(float('1.0e4')) # 10000.0