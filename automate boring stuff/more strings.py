# string methods
# lesson 20
# pages 128 - 141

# strings are immutable  - "can't be modified in place"
# upper() and lower()
spam = 'HELLO WORLD'
print(spam)
# must over-write variable to make it lower/change it
# just
# spam.lower()
# won't work
spam = spam.lower()
print(spam)

# can be used for user input
#print('would like to play again? ')
#answer = input()
#if answer == 'yes':
#    print('playing again')
#else:
#    print('not playing again')


# false if input has any upper case

#print('would like to play again? ')
#answer2 = input()
#answer2 = answer2.lower()
#if answer2 == 'yes':
#    print('playing again')
#else:
#    print('not playing again')


# isupper/islower - boolean values
# will return false for just '' empty string
# same for strings of all numbers
# isupper/islower return strings
# like
# hello.upper().isupper()

# also 
# isalpha - test for letters only
# isalnum() - test for letters and numbers only
# isdecimal - numbers only - '123'.isdecimal == true
# isspace - whitespace only # 'hello world'[5].isspace() is space so it's true
# istitle - titlecase only # not sure what that is. like Star Wars? S and W caps? no idea - actually this right. I gussed right

# startswith/endswith
# yes, this printline works and just outputs 'true'
print('Hello world'.startswith('H'))

# also join strings
# returns string
acommma = ','
acommma = acommma.join(['cats', 'rats', 'bats'])
print(acommma)

# split is opposite of join
#acommma = acommma.split()
#print(acommma)

# split on a particular character in the string
acommma = acommma.split('t')
print(acommma)

# left and right justification
# ljust and rjust
# i assume i can workthis out
testMessage = '     rightside'
#testMessage.rjust(4, '*')
testMessage.center(20, '=')
print(testMessage)

# strip string methods
# mainly used for stripping out whitespaces but also 
# can be used with some characters/strings
spam = 'Hello   '
spam = spam.strip()
print(spam)
spam = 'hellotherewhateverpsamspamspam'
spam = spam.strip('amps')
print(spam)

# also replace
spam = spam.replace('l', 'XXX')
print(spam)

# there's also lstrip and rstrip
spam = spam.strip('X')
print(spam)

# pyperclip module

import pyperclip
# arbitrarily insert contents on to local clip board
pyperclip.copy('hello..................!')
clippy = pyperclip.paste()
print(clippy)
