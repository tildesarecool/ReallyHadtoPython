# reg ex dot-star and the caret/dollar characters
# lesson 27
# pages 159 - 163
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

from http import server
import re
beginWithHelloRegex = re.compile(r'^Hello') # begins with, not matching in middle
#beginsResult = beginWithHelloRegex.search('Hello there!')
# print(beginsResult) # came back with match

beginsResult = beginWithHelloRegex.search('He said "Hello!"') # result is not match

endsWithHelloRegex = re.compile(r'world!$') 
endsResult = endsWithHelloRegex.search('Hello World!a;sldjfkasl;dfj') # returns not match or "none"
#print(endsResult)

# notes:
# ^both$ means pattern must match entire string
allDigitsRegEx = re.compile(r'^\d+$') 
allDigitsResult = allDigitsRegEx.search('29348572309457') # returns  match for only numbers, returns none as soon as a letter is in there
#print(allDigitsResult) 


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


nameRegEx = re.compile(r'First Name: (.*) Last Name: (.*)')
dotstarResult = nameRegEx.findall('First Name: Al Last Name: Swagger')
#atResult = atRegex.findall('The cat in the hat sat on the flat mat')
#print(dotstarResult)
# output
# [('Al', 'Swagger')]

# notes
# (.*) is greedy mode - "match as much text as possible"
# (.*?) is non-greedy mode


serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')

greedResult = nongreedy.findall(serve)
# print(greedResult)
# output is 
# ['To serve humans']
# "stop there becuase not greedy"


greedy = re.compile(r'<(.*)>')
yesgreedResult = greedy.findall(serve)
#print(yesgreedResult)
# output
# ['To serve humans> for dinner.']

# making dot match newlines too - with re.DOTALL

prime = "serve public trust \n protect innocent \n upohold the law"

#dotStar = re.compile(r'.*')
#dotStarFindings = dotStar.search(prime)
#print(dotStarFindings) # matches only "serve public trust"

#adding options to the re.compile = DOTALL means "match everything as much as possible" and is "greedy"
dotStar = re.compile(r'.*', re.DOTALL)
dotStarFindings = dotStar.search(prime)
#print(dotStarFindings) # matches only "serve public trust"
# output matches
# serve public trust \n protect innocent \n upohold>

# also the INGORECASE option



#vowelRegEx = re.compile(r'[aeiou]')
#vowelResult = vowelRegEx.findall('Al, why does your book talking about robocopy so much?')
#print(vowelResult)

vowelRegEx = re.compile(r'[aeiou]', re.IGNORECASE)
vowelResult = vowelRegEx.findall('Al, why does your book talking about robocopy so much?')
print(vowelResult)
# output
# ['A', 'o', 'e', 'o', 'u', 'o', 'o', 'a', 'i', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']

# ^ means string must start with the pattern, $ means the string must end with the pattern
#  both means the entire string must match the pattern
# 
# The . dot is a wildcard; it matches anything except newlines
# pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines too
# 
# pass re.I (for INGORECASE) as second argument to re.compile() to make the matching non-case-sensitive
# 
# 
# 
# 
# 
# 
# 
# 




















