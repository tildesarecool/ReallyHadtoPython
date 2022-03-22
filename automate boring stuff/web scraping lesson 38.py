# web browser module
# lesson 38 / chapter ?
# pages 233 - 236
# decided to skip ahead to webscraping. just skipped over some further filesystem stuff and the debugger stuff


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

from audioop import add
from ntpath import join
import webbrowser, sys, pyperclip # sys == command line arguments, argv
# even when run from console this pops up new tab with URL
#webbrowser.open('https://www.drudgereport.com') # also, returns true

# idea is to use run box to use something like
# mapit <some address> to auto open in google maps

sys.argv

# check if command line arguments were passed

if len(sys.argv) > 1:
# want to convert something like
# ['mapit.py', '870', 'valencia', 'st.'] to -> '870 valencia st.'

    address = ''.join(sys.argv[1:]) # slicing
    #print(address) # was just testing before using webbrowser open below
else:
    # assuming data is on clipboard

    address = pyperclip.paste()

# he figured out that the address
# https://www.google.com/maps/place/2012+Smith+Flat+Rd,+Placerville,+CA+95667/@38.7333222,-120.7567376,17z/data=!3m1!4b1!4m5!3m4!1s0x809a507c51d4b1b3:0x7f41d3d54c8bbaa1!8m2!3d38.733318!4d-120.7545489
# could be shortened down to 
# https://www.google.com/maps/place/2012+Smith+Flat+Rd,+Placerville,+CA+95667/
# (which is still the case)
# he also found if spaces are used in place of + the URL still works (also still the case)

# so can start with
# https://www.google.com/maps/place/
# then just a plain street address
webbrowser.open('https://www.google.com/maps/place/' + address) # this actually works

# in the video he suggests using a batch file
# I'd probably use a different method
# to get the arguments passed in though, 
# # I'd use that py.exe follwoed by the path to the py script
# followed by %* which apparently grabs the arguemnts (and was covered in lesson 22 pers this video)

# did find I have to use the quotes
# automate boring stuff\web scraping lesson 38.py "1134 wall street, placerville, ca, 95667"

