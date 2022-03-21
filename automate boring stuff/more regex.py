# reg ex start
# lesson 24
# pages 
# reg ex groups and pipe character

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


import re

usermessage = 'Call me 555-513-3311 tomorrow, or at 412-555-9933 etc'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # returns reg ex object
mo = phoneNumRegex.search(usermessage ) # returns a match object
#print(mo.group())
# only output is first number in that usermessage string
##### GROUPS
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # paranthesis to group area code and the rest of the 7
mo2 = phoneNumRegex2.search(usermessage ) # returns a match object
# same output as above
# which is that first phone number in phone number format and nothing else.
#print(mo2.group())
#this will return just that 555 area code and nothing else
#print(mo2.group(1))

# parens have special properties in regex so search them have to escape them
usermessage3 = 'Call me (555) 513-3311 tomorrow, or at 412-555-9933 etc'
phoneNumRegex3 = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)') # paranthesis to group area code and the rest of the 7
mo3 = phoneNumRegex3.search(usermessage3 ) # returns a match object
print(mo3.group())
# output this time round is 
# (555) 513-3311

######################## PIPES
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # pipes for matching one of many possible groups
batmo = batRegex.search('Batman lost a wheel, also, Batcopter')
print(batmo.group())


#mo = phoneNumRegex.search(usermessage) # returns "match object"
#print(mo.group())
# mo.group

# the fine all method instead, returns list of strings ofmatches

#mo2 = phoneNumRegex.findall(usermessage) # returns "match object"
#print(mo2) # returns both matches in list form