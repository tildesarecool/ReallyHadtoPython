# saves items in ordered list
# in brackets, separated by commas
spam = ['cat', 'bat', 'rat', 'elephant']

# access with name brackets, 'indexes'
# indexes start at 0
spam[0]

# can also have "list of lists"

# can also have negative numbers to start from end of list
spam[-2]

print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

# i think i missed "slices". too busy typing out code

# slice
spam[1:3] = ['CAT', 'DOG', 'MOUSE']

# slice shortcuts
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]
# will eval to ['cat', 'bat']

# deleting values from list
del spam[2] # deletes elephant, also an "unassignment" operator

# back to len
# can pass a lsit
len('Hello')
# 5
# list function that returns list version of a value passed in, like int() and str()
list('Hello')
# for instance

# in and not in
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# comes back true
'howdy' not in ['hello', 'hi', 'howdy', 'heyas']
# would be false

# a lot of functions for strings work for lists

