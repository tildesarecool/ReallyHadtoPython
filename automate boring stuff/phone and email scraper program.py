# reg ex dot-star and the caret/dollar characters
# lesson 29
# pages ??
# 


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

# notes:
# search returns match objects
# findall returns list of strings

# behavrior for regex objects that have or one groups in them (groups being with the \d\d\d inside () ) is 
# find all returns list of strings will just be text foundmatching that pattern
# see lesson 26 around 3 minutes in for phrasing with on-screen "correction"

#sfindallMatchesEx2 = phoneRegex2.findall(LongSringExample)
# returns have strings, tuples
# has zero or one groups == list of strings
# if has two or more groups list of tuples of strings

# character classses

#digitRegex = re.compile('(0|1|2|3|4|5|6|7|8|9') # same is /d
# table 7-1 in the book
# /D (cap D) is "any character not numberic between 0 and 9"
# /w is "any letter, numberic digit or underscore character" referred to as "word"
# /W (cap W) "any character that is NOT a letter, numberic digit or underscore character" 
# /s any space, tab or newline character (e.g. "matching the space characters")
# /S (cap S) any character NOT space, tab or newline character (e.g. "matching the space characters")

# make cusotm/own character classes with [] e.g [aeiou]
# a caret ^ makes a negative character class, matching anything NOT in the backets, like [^aeiou] for all non-vowels

# having period/dot means "any character not newline"
#atRegex = re.compile('.at')
#atResult = atRegex.findall('The cat in the hat sat on the flat mat')
#print(atResult)


# altered version so that output matches with whole of 'flat' instead of just the 'lat' portion of 'flat'
# this also matches spaces
#atRegex = re.compile(r'.{1,2}at')
#atResult = atRegex.findall('The cat in the hat sat on the flat mat')
#print(atResult)

# .* notation is all the stuff

#atResult = atRegex.findall('The cat in the hat sat on the flat mat')
#print(dotstarResult)
# output
# [('Al', 'Swagger')]

# notes
# (.*) is greedy mode - "match as much text as possible"
# (.*?) is non-greedy mode
# also the INGORECASE option
# ^ means string must start with the pattern, $ means the string must end with the pattern
#  both means the entire string must match the pattern
# 
# The . dot is a wildcard; it matches anything except newlines
# pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines too
# 
# pass re.I (for INGORECASE) as second argument to re.compile() to make the matching non-case-sensitive
# 
# the sub() method

# namesRegEx = re.compile(r'Agent \w+')
# nameresult = namesRegEx.findall('Agent Alice gave the secret documents to Agent Bob')
# print(nameresult)
# output
# ['Agent Alice', 'Agent Bob']


# namesRegEx = re.compile(r'Agent \w+')
# nameresult = namesRegEx.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob')
# print(nameresult)
# Successful find/replace output
# REDACTED gave the secret documents to REDACTED

#################### Using \1 \2 etc in sub()

## namesRegEx = re.compile(r'Agent (\w)\w*')
# this would just be
# # nameresult = namesRegEx.findall('Agent Alice gave the secret documents to Agent Bob')
# output 'A' and 'B' (for alice and bob)
# the \1 refers to the first group
## nameresult = namesRegEx.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob')
## print(nameresult)
# so it iwill be first letter and asterisks instead of redacted 
# output
# Agent A**** gave the secret documents to Agent B****

####################### Verbose Mode with re.VERBOSE

# verbose can be used in place of that \d\d\d in the phone numbers example

# recap

# the sub() regex method will substitute matches with some other text
# using \1, \2, and so on will substitute group 1,2, etc in regex pattern
# passing re.VERBOSE lets you add whitespace and comments to the regex string passed re.compile()
# if you want to pass multiple arguemtns (re.DOTALL, re.IGNORECASE etc) combine with the | bitwise operator
# the bitwise OR isn't really used any other place in python language
# scaping the PDF sample phone/email directory data
# not sure why he didn't make it a text file to start with but whatever i converted pdf to txt file

# 
# 
# 
#! python3

# TODO LIST
# create a regex for phone numbers
# 
# 
# 
# 
# 
# 
import re, pyperclip
phoneRegEx = re.compile(r''' 
            # types
            # 415-444-0000
            # or
            # 555-0000 or (514) 444-0000 or 555-0000 ext 12345, 234,2334
(
((\d\d\d)|(\(\d\d\d\)))?            # area code (optional) 
(\s|-)                              # frist separator
\d\d\d                              # first 3 digits
-                                   # separator
\d\d\d\d                            # last 4 digits
((ext(\.)?\s|x)                     # word part (optional)
(\d{2,5}))?                         # extension number part (optional)
)
# 
# 
# verbose mode allows for all this multi-line comments thing
''', re.VERBOSE)


# create a regex for email addresses



emailRegEx = re.compile(r''' 

[a-zA-Z0-9_.+]+                 # name part - no need to escape because 
@                               # at  symbol part
[a-zA-Z0-9_.+]+                 # domain name part
                                # 
                                # 
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract email/phone from this text

extractedPhone = phoneRegEx.findall(text)
extractedemail = emailRegEx.findall(text)



# create blank list for phone numbers
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# these didn't workthe first time, as they returned some 'tuples'
# solution is to put the whole phone number reg ex into parens to make them into one group
#print(extractedPhone)
#print(extractedemail)
# these didn't work so good, they returned some 'tuples'

# after the extra paranes to make a group and the allphonenumbers variable create
# seem to have good output and successfully display phone numbeers/emails
#print(allPhoneNumbers)
#print(extractedemail)



########################## copy extracted email/phone to clipboard

# next step is getting rid of ' quotes and commas

# one number per line
 # this will make one number per line
#phoneResults = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedemail) 
#  
allResults = ',\n'.join(allPhoneNumbers) + ',\n' + '\n'.join(extractedemail) 
pyperclip.copy(allResults)

# hey! it works!
# made a text file for the output

#print(allPhoneNumbers)
#print(extractedemail)
