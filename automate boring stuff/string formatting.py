# string formatting extras - using %s
# lesson 21
# making concatenating strings easier
# interprolation?
# %s are called conversion specifiers
name = 'bob'
place = 'pville'
time = 'twelve'
mymessage = 'hello %s how are you %s please bring %s' % (name, place, time) # comma separated list of variables
print(mymessage)
# seems like easier version  then using the + signs to combine strings
