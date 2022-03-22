# filenames and absolute/relative file paths
# lesson 30 / chapter 8 
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

# in windows paths have to be escaped
# like c:\\spam
# can always use the raw string like r'c:\spam\eggs.png

# for windows could use this to build up a path
#winPath ='\\'.join(['folder1', 'folder2', 'folder3', 'file.png']) # windows only
#print(winPath)
# output:
# folder1\folder2\folder3\file.png
# ideal would want this to work on more than just windows

from decimal import ROUND_DOWN
from math import floor
import os
from unicodedata import decimal
# this includes os.path.join
#os.path.join('folder1', 'folder2', 'folder3', 'file.png')

#print(os.sep)

#curpath = os.getcwd() # get current working directory
#print(curpath)

#changeToWindows =
#os.chdir(curpath + '..') # not sure how to use this function. doesn't seem to do anything
#changeToWindows

# there's also
#os.path.abspath() # returns abosluate path of what you pass in, like a file name
# and
#os.path.isabs() # I assume returns whether or not a path is an absolute (string)
# functions

#os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
# returns folder2\\spam.png

# also 
#os.path.dirname('c:\\folder1\\folder2\\spam.png') # just returns c:\\folder1\\folder2
# and
#os.path.basename('c:\\folder1\\folder2') # just 'folder2', thing after final slash


#os.path.exists('c:\\folder1\\folder2\\spam.png') # standard ifexist sort of text

# these two seems kind of self-explanatory
#os.path.isfile() # is file?
#os.path.isdir() # is directory?

#os.path.getsize() # pass in file and it returns int size in bytes

#getlist = os.listdir('.') # pass in folder and it will return list of strings that inculdes files/folders
#print(getlist)
# this did return list of files/folders inside current directory which was c:\Python310

#samplePath = 'C:\\Users\\Keith\\Documents\\repos\\ReallyHadtoPython\\automate boring stuff'
samplePath = 'c:\windows\system32'

totalSize = 0
for filename in os.listdir(samplePath):
    if not os.path.isfile(os.path.join(samplePath, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(samplePath, filename))

calcSize = int(totalSize) / 1024

#round(calcSize)
#floor(int(calcSize))

#round(int(calcSize))

#print(calcSize) # has long decimal value, not sure how to cut that off yet. and haven't looked it up

os.makedirs() # used to create folders, relative or absolute