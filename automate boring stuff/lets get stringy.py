# lesson 19
# roughtly pages 123 - 127 of the book
# namely "advanced string syntax"

# multiple ways to print strings like with double quotes
#"that is alice's cat"
# wouldn't error

#also escape characters
# ' say hi to bob\'s mother'
# \t for tab
# \n for newline
# \\ for single back slash

print('hello there\nhow are you\ni\'m fine')

# raw strings will "literally" print any backslashes in the string and ignore escape characters
r'Hello'
# will go straight through 
r'that is carol\'s cat'

# also the previously mention triple quote '''
# no escapes for this one. also works with double quotes """
# like preformatted tag i suppose
print(''' dear alic, 
eve's cat has been arrested for extortion
seincerely, 
bob''')

# strings can use inddex, slices and not/not in operators like lists do
spam = 'hello world'
print(spam[1:5])
print(spam[-1])

