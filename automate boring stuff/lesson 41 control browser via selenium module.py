# web browser module + parsing html w/beautiful soup module + selenium
# lesson 41 / chapter ?
# pages 249 - 
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

# import webbrowser, sys, pyperclip # sys == command line arguments, argv
# even when run from console this pops up new tab with URL
#webbrowser.open('https://www.drudgereport.com') # also, returns true

# idea is to use run box to use something like
# mapit <some address> to auto open in google maps

# sys.argv

# check if command line arguments were passed

#if len(sys.argv) > 1:
# want to convert something like
# ['mapit.py', '870', 'valencia', 'st.'] to -> '870 valencia st.'

 #   address = ''.join(sys.argv[1:]) # slicing
    #print(address) # was just testing before using webbrowser open below
#else:
    # assuming data is on clipboard

#    address = pyperclip.paste()

# he figured out that the address
# https://www.google.com/maps/place/2012+Smith+Flat+Rd,+Placerville,+CA+95667/@38.7333222,-120.7567376,17z/data=!3m1!4b1!4m5!3m4!1s0x809a507c51d4b1b3:0x7f41d3d54c8bbaa1!8m2!3d38.733318!4d-120.7545489
# could be shortened down to 
# https://www.google.com/maps/place/2012+Smith+Flat+Rd,+Placerville,+CA+95667/
# (which is still the case)
# he also found if spaces are used in place of + the URL still works (also still the case)

# so can start with
# https://www.google.com/maps/place/
# then just a plain street address
#webbrowser.open('https://www.google.com/maps/place/' + address) # this actually works

# in the video he suggests using a batch file
# I'd probably use a different method
# to get the arguments passed in though, 
# # I'd use that py.exe follwoed by the path to the py script
# followed by %* which apparently grabs the arguemnts (and was covered in lesson 22 pers this video)

# did find I have to use the quotes
# automate boring stuff\web scraping lesson 38.py "1134 wall street, placerville, ca, 95667"

############# downlaod from web via requests module
# requests module is third party so must install via pip
# since pip was already setup, I used this commmand:
###### pip install requests
# and it worked


#from asyncore import write # this seems to keep inserting itself. so I'll leave it
#import webbrowser, sys, pyperclip, requests # sys == command line arguments, argv

#res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # returns 'response object'
#print(res.status_code) # this actually worked just show '200'

# he mentioned more information on http requests at URL
# https://docs.python-requests.org/en/latest/

# in idle, can use that 'import requests' and that res variable/call to get
# then usee res.status_code to confirm it worked 
# if it returns '200' that it was successful

# print(len(res.text)) # returns number of characters in that text file - 178978
#print(res.text[:500]) # returns first 500 characters of file

# use 
#res.raise_for_status()
# in order to get info on error

#badRes = requests.get('https://automatetheboringstuff.com/234234234234a;lsdkfjasdf;lkj.txt')
#badRes.raise_for_status()
# when i push F5 is vscode the 'compiler' or whatever just give me a read flag about the unfound url/file
# but in idle there's a whle thing  of red text that includes HTTPError: 404 client error: not found etc
# can wrap line
# badRes.raise_for_status()
# in try/except to respond when that happens

################### open() function
####### open(filename, 'wb') for write-binary mode

#playFile = open('RomeoAndJuliet.txt', 'wb') # still has to be "write binary mode" even for plain text to maintain unicoding formatting

#for chunk in res.iter_content(100000):
#    playFile.write(chunk) # returns int for how many bytes wrote to file

# I did this idle since it was easier to immediately see output
# output:
# 100000
# 78978

#playFile.close()

# requests module good when have exact url 
# but when have to login or figuring out
# well just jump to selenium next to lesson

# recap
# requests.get() returns response object
# raise_for_status() response meothod will reaise esxception if download fails (use in combo w/ try/except)
# can save a downlaod file to hard drive with calls to 
# iter_content() method

######################### web scraping #########################

# first brought up developer tools with F12
# can also "inspect"
# installed with command:
#### pip install beautifulsoup4

############# selenium installation/lesson 41 #############
# installed with command
### pip install -U selenium
# which worked
# but since i need a "web driver"
# I got the chromedriver

# today at least chrome is version99.0.4844.51 so I downlad the zip from here
# https://chromedriver.storage.googleapis.com/index.html?path=99.0.4844.51/

#import bs4, requests # webbrowser, sys, pyperclip, requests # sys == command line arguments, argv
from selenium import webdriver
browser = webdriver.Firefox() # starts the browser in "selenium mode" (robot icon to left of URL in URL bar)
browser.get('https://drudgereport.com') # once firefox open this sends it to specified URL. but needs both

# body > tt:nth-child(1) > b:nth-child(1) > tt:nth-child(3) > b:nth-child(1) > center:nth-child(29) > font:nth-child(1) > font:nth-child(1) > a:nth-child(3)

#elem = browser.find_element_by_css_selector('body > tt:nth-child(1) > b:nth-child(1) > tt:nth-child(3) > b:nth-child(1) > center:nth-child(29) > font:nth-child(1) > font:nth-child(1) > a:nth-child(3)')

# After looking at the documetnation
# https://www.selenium.dev/documentation/webdriver/elements/finders/
# found out that the browser.find_element_by_css_selector is deprecated
# then I further found out I need this extra import line
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
# because otherwise it will just keep saying that 'By' is undefined
# this line worked without any errors in idle
elem = browser.find_element(by=By.CSS_SELECTOR, value='body > tt:nth-child(1) > b:nth-child(1) > tt:nth-child(3) > b:nth-child(1) > center:nth-child(29) > font:nth-child(1) > font:nth-child(1) > a:nth-child(3)')
################# elem = browser.find_element(by=By.CSS_SELECTOR, value='body > tt:nth-child(1) > b:nth-child(1) > tt:nth-child(3) > b:nth-child(1) > center:nth-child(29) > font:nth-child(1) > font:nth-child(1) > a:nth-child(3)')
# also, it's much easier to "copy css path" or whatever from firefox's dev tools than chrome's
# I had up to this point and ran it on the command shell and no errors
#elem.click()
# then I did 
elems = browser.find_elements(by=By.CSS_SELECTOR, value='p')
print(len(elems)) # for cli - returns 4 just like idle and no errors
# it's drudge though so it came back as 4 paragraphs

# sinca all the information in video is outdated there's no reason to try and follow it
# I'll just watch it and take note of what seems more interesting for what i can do
# but really this is just fyi stuff

# looks like browser.back, browser.forward, browser.refresh and browser.quit are all things
# all web elements have a text member variable that contains a string of the text inside of that element
# one approach is just to grab the html tag/element which contains the whole web page
# 