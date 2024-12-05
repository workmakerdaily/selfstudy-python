print("'Nay!' said the naysayer. 'Neigh?' said the horse.")
# 'Nay!' said the naysayer. 'Neigh?' said the horse.

print('''Boom!''') # Boom!
print("""Eek!""") # Eek!

poem = '''There was a Young Lady of Norway,
    Who casually sat in a doorway;
    When the door squeezed her flat,
    She exclaimed, "What of that?"
    This courageous Young Lady of Norway.'''
print(poem)
# There was a Young Lady of Norway,
#     Who casually sat in a doorway;
#     When the door squeezed her flat,
#     She exclaimed, "What of that?"
#     This courageous Young Lady of Norway.

# poem = 'There was a young lady of Norway,
# SyntaxError: unterminated string literal (detected at line 19)

print('Give', "us", '''some''', """space""") # Give us some space

print(type(str(98.6))) # <class 'str'>

palindrome = 'A man, \nA plan, \nA canal:\nPanama'
print(palindrome)
# A man,
# A plan,
# A canal:
# Panama

print('\tabc') #         abc
print('a\tbc') # a       bc
print('ab\tc') # ab      c

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony) # "I did nothing!" he said. "Or that other thing."

speech = 'The backslash (\\) bends over backwards to please you.'
print(speech) # The backslash (\) bends over backwards to please you.

info = r'Type a \n to get a new line in a normal string'
print(info) # Type a \n to get a new line in a normal string

poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
print(poem)
# Boys and girls, come out to play.
# The moon doth shine as bright as day.

print('Release the kraken! ' + 'No, wait!')
# Release the kraken! No, wait!

vowels = ('a'
        "e" '''i'''
        'o' """u""")
print(vowels) # aeiou

start = 'Na ' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
# Na Na Na Na
# Na Na Na Na
# HeyHeyHey
# Goodbye.

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0]) # a
print(letters[1]) # b
print(letters[-1]) # z
print(letters[-2]) # y

# print(letters[100])
# IndexError: string index out of range

name = 'Henny'
print(name.replace('H', 'P')) # Penny
print('P' + name[1:]) # Penny
print(name) # Henny

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:]) # abcdefghijklmnopqrstuvwxyz
print(letters[20:]) # uvwxyz
print(letters[10:]) # klmnopqrstuvwxyz
print(letters[12:15]) # mno
print(letters[-3:]) # xyz
print(letters[18:-3]) # stuvw
print(letters[-6:-2]) # uvwx
print(letters[::7]) # ahov
print(letters[4:20:3]) # ehknqt
print(letters[19::4]) # tx
print(letters[:21:5]) # afkpu
print(letters[-1::-1]) # zyxwvutsrqponmlkjihgfedcba
print(letters[::-1]) # zyxwvutsrqponmlkjihgfedcba
print(letters[-50:]) # abcdefghijklmnopqrstuvwxyz
print(letters[-51:-50]) # ''
print(letters[:70]) # abcdefghijklmnopqrstuvwxyz
print(letters[70:71]) # ''

print(len(letters)) # 26

empty = ''
print(len(empty)) # 0

tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
# ['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']

print(tasks.split())
# ['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
# Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
# a marmoset goes into a bar...

print(setup.replace('a ', 'a famous ', 100))
# a famous duck goes into a famous bar...

world = " earth "
print(world.strip()) # 'earth'
print(world.strip(' ')) # 'earth'
print(world.lstrip()) # 'earth '
print(world.rstrip()) # ' earth'

print(world.strip('!')) # ' earth '

blurt = "What the...!!?"
print(blurt.strip('.?!')) # What the

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13]) # All that doth
print(len(poem)) # 250
print(poem.startswith('All')) # True
print(poem.endswith('That\'s all, folks!')) # False

word = 'the'
print(poem.find(word)) # 73
print(poem.index(word)) # 73

print(poem.rfind(word)) # 214
print(poem.rindex(word)) # 214

word = "duck"
print(poem.find(word)) # -1
# print(poem.index(word)) # ValueError: substring not found

word = 'the'
print(poem.count(word)) # 3

print(poem.isalnum()) # False

setup = 'a duck goes into a bar...'

print(setup.capitalize()) # A duck goes into a bar...
print(setup.title()) # A Duck Goes Into A Bar...
print(setup.upper()) # A DUCK GOES INTO A BAR...
print(setup.lower()) # a duck goes into a bar...
print(setup.swapcase()) # A DUCK GOES INTO A BAR...

print(setup.center(30)) # '  a duck goes into a bar...   '
print(setup.ljust(30))  # 'a duck goes into a bar...     '
print(setup.rjust(30))  # '     a duck goes into a bar...'


print('%s' % 42) # 42
print('%d' % 42) # 42
print('%x' % 42) # 2a
print('%o' % 42) # 52

print(type('%s' % 42)) # <class 'str'>
print(type('%d' % 42)) # <class 'str'>
print(type('%x' % 42)) # <class 'str'>
print(type('%o' % 42)) # <class 'str'>

print('%s' % 7.03) # 7.03
print('%f' % 7.03) # 7.030000
print('%e' % 7.03) # 7.030000e+00
print('%g' % 7.03) # 7.03

print('%d%%' % 100) # 100%

actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
# My wife's favorite actor is Richard Gere

print("Our cat %s weighs %s pounds" % (cat, weight))
# Our cat Chester weighs 28 pounds

thing = 'woodchuck'
print('%s' % thing) # 'woodchuck'
print('%12s' % thing)  # '   woodchuck'
print('%+12s' % thing) # '   woodchuck'
print('%-12s' % thing) # 'woodchuck   '
print('%12.3s' % thing)  # '         woo'
print('%-12.3s' % thing) # 'woo         '

thing = 98.6
print('%f' % thing) # '98.600000'
print('%12f' % thing)  # '   98.600000'
print('%+12f' % thing) # '  +98.600000'
print('%-12f' % thing) # '98.600000   '
print('%.3f' % thing) # '98.600'
print('%12.3f' % thing)  # '      98.600'
print('%-12.3f' % thing) # '98.600      '

thing = 9876
print('%d' % thing) # '9876'
print('%12d' % thing)  # '        9876'
print('%+12d' % thing) # '       +9876'
print('%-12d' % thing) # '9876        '
print('%.3d' % thing) # '9876'
print('%12.3d' % thing)  # '        9876'
print('%-12.3d' % thing) # '9876        '

thing = 'woodchuck'
print('{}'.format(thing)) # 'woodchuck'

thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))
# The woodchuck is in the lake.
print('The {1} is in the {0}.'.format(thing, place))
# The lake is in the woodchuck.

print('The {thing} is in the {place}.'.format(thing='duck', place='bathtub'))
# The duck is in the bathtub.

d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))
# The duck is in the bathtub.

thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
# 'The wraith is at the window'
print('The {:10s} is at the {:10s}'.format(thing, place))
# 'The wraith     is at the window    '
print('The {:<10s} is at the {:<10s}'.format(thing, place))
# 'The wraith     is at the window    '
print('The {:^10s} is at the {:^10s}'.format(thing, place))
# 'The   wraith   is at the   window  '
print('The {:>10s} is at the {:>10s}'.format(thing, place))
# 'The     wraith is at the     window'
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))
# 'The !!wraith!! is at the !!window!!'

thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
# The wereduck is in the werepond

print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
# The Wereduck is in the             werepond

print(f'The {thing:>20} is in the {place:.^20}')
# The             wereduck is in the ......werepond......

print(f'{thing =}, {place =}')
# thing ='wereduck', place ='werepond'

print(f'{thing[-4:] =}, {place.title() =}')
# thing[-4:] ='duck', place.title() ='Werepond'

print(f'{thing = :>4.4}')
# thing = were