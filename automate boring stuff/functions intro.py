# apparently this is how you do funcitons in python
# seems like a a strange thing but if it works it works


def hello():
    print('Howdy')
    print('Howdy')
    print('Hello there')

# using parameters/arguments with functions
def helloNew(name):
    print('Hello ' + name)


helloNew('Alice')
helloNew('Bob')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

# print function returns data type "None" (which is case sensitive/capital N)

# if i say 
spam = print()
# then I say
spam == None
# this would evaluate to true

# prints automatically adds a newline
print('Hello')
print('World')
# can set an end chracter with keyword
print('Hello', end='')
# there's also the sep keyword
print('cat ', 'dog', 'mouse', sep='abc')

