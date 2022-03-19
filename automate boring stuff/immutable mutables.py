def eggs(someParameter):
    someParameter.append('Hello') # destroys at function return

spam = [1, 2, 3] # storing reference to the list - lists are "mutable"
eggs(spam)
print(spam)

# output:
# [1, 2, 3, 'Hello']

# see changes outside function
# seems like it should be outside of scope

# python reference system...


# the copy.deepcopy function

# module called copy
import copy
# will make brand new list, return reference to new list instead

spam = [ 'A', 'B', 'C', 'D' ]
cheese = copy.deepcopy(spam)
cheese[1] = 42
cheese
# output
# ['A', 42, 'C', 'D']

spam
# output
# ['A', 'B', 'C', 'D']
# e.g. two different strings instead of modifying the same one

# "Line continuation"
# exception to the indentation blocks rule
spam = ['apples', 
        'oranges', 
        'bananas', 
        'cats']

# can use \ for continue to next line
print('Four score and seven ' + \
    'years ago')

