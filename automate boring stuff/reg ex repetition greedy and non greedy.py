# reg ex greedy/non greedy, repetitions
# lesson 25
# pages 
# reg ex groups and pipe character
# pages 154 157

import re
# ? character appears once or not at all
#batRegex = re.compile(r'Bat(wo)?man')
#mo = batRegex.search('The Adventures of Batman')
#print(mo.group())
#mo2 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo == None)

# using prior phone number examples
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pho = phoneRegex.search('my phone number is 442-555-1122. call me tomorrow')
print(pho.group())
pho = phoneRegex.search('my phone number is 555-1122. call me tomorrow')
print(pho == None)

phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
#pho2 = phoneRegex2.search('my phone number is 442-555-1122. call me tomorrow')
pho2 = phoneRegex2.search('my phone number is 555-1122. call me tomorrow')

print(pho2.group())
print(pho2 == None)

#******************** star character

batRegex = re.compile(r'Bat(wo)*man')
#bmo = batRegex.search('The Adventures of Batwoman')
bmo2 = batRegex.search('The Adventures of Batwowowowoman')
print(bmo2)

#########################+++++++++++++++ + - "one more more"

batRegex = re.compile(r'Bat(wo)+man')
bmo3 = batRegex.search('The Adventures of Batwoman')
#bmo3 = batRegex.search('The Adventures of Batwowowowoman')
print(bmo3)

# the ?, * and + can all be escaped by adding \ to them respectively


 # --------------------------{ exectly }

haRegex = re.compile(r'(Ha){3}')
har = haRegex.search('He said HaHaHa')

print(har)



phoneRegex3 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
#pho2 = phoneRegex2.search('my phone number is 442-555-1122. call me tomorrow')
pho3 = phoneRegex3.search('my phone numbers are 111-555-1122, 334-222-3434, and 333-333-2211. call me tomorrow')

#print( pho3.group() )
print(pho3 == None)

haRegex = re.compile(r'(Ha){3,5}') # between 3 and 5 instances of match, max number returned 5
har2 = haRegex.search('He said HaHaHaHaHaHaHaHa')

print(har2)





digitRegex = re.compile(r'(\d){3,5}?') # with ? added output is 123
digi = digitRegex.search('1234567890')

print(digi.group()) # ouptput is 12345 w/out ? in regex pattern, with ? it just goes to 3 as in 123
print(digi) # output is that it's a match

# summmary
# ? = says group matches zero or one times
# * = zero or more times
# + = one or more times
# { } = match specific number of times
# { } w/ some number matches minimum and max number of times
# leaving out first or seond number in curly braces says there is no min or max
# "greedy" matching will match logest string possible
# "nongreed" matching will match shortest string possible
# putting ? after curly braces makes it do a nongreedy match
# 











