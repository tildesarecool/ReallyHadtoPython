
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
# would return 
# 0

# methods can also be used to find an indext
spam.index('heyas')
# would return 3

# if duplicate list encountered
# and index method  would return first one it encountered

# also append
spam = ['cat', 'dog', 'bat']
spam.append('moose')
# puts it on the end

# also insert
spam.insert (1, 'checken')

# also remove
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.remove('hi')
# as is implied. remove takes out by value of item no matter where it is 
# while del removes using index number, like
del spam[0]

# sort method

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.sort()
# will better for numbers. make in order
# for words it would be in aplha order
# also
spam.sort(reverse=True)
spam.sort()
# can't sort both ints and strings list
# will throw error

# and technically uses ascii-betical order
# just referring to cap letter strings coming before lower case
# can get around this with
spam.sort(key=str.lower)
# true alpha order

