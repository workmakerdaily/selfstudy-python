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

x = 7
print(5 < x and x < 10) # True
print((5 < x) and (x < 10)) # True

print(5 < x or x < 10) # True
print(5 < x and x > 10) # False
print(5 < x and not x > 10) # True

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
# Hey, it's empty!

letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
# o is a vowel

vowels = 'aeiou'
letter = 'o'
print(letter in vowels) # True

if letter in vowels:
    print(letter, 'is a vowel')
# o is a vowel

letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set) # True

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list) # True

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple) # True

vowel_string = "aeiou"
print(letter in vowel_string) # True

vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala', 'o':'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict) # True

tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# A fitting tweet

tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >=0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# A fitting tweet