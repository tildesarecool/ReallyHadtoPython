# reg ex start
# lesson 23
# pages 147 - 151

# pattern matching...

# example is phone numbers
# 3 number - dash - 3 numbers - dash - four numbers 

# a non-reg expression
# arbitrary overly long non-regex example for fun
def isPhoneNumber(text): # returns true if in regular phon number format
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

returnedvalue = isPhoneNumber('916-555-1144')
print(returnedvalue) # returns true

# to use reg ex
import re
# usually pass in raw strings to re.complie()

usermessage = 'Call me 555-513-3311 tomorrow, or at 412-555-9933 etc'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(usermessage) # returns "match object"
#print(mo.group())
# mo.group

# the fine all method instead, returns list of strings ofmatches

mo2 = phoneNumRegex.findall(usermessage) # returns "match object"
print(mo2) # returns both matches in list form
# output:
# ['555-513-3311', '412-555-9933']

# interesting notes on reg expressions
# reg ex use backslash like \d, requiring use of raw strings: r'\d'
# import the re module first
# imoprt re
# 
# call re.compile() funciton to create reg ex object
# call the regex object's search() method to create a match object
# call match object's group() method to get the matched string
# 
# \d is the regex for a numberic digit character
# 
# 
# 
# 