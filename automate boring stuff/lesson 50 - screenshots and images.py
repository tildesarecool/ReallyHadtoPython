# lesson 50 / chapter 18
# chapter 18/last chapter - screenshots/images
# I skipped ahead again because the in between chapters didn't seem that interesting
# I'm just assuming the informaiton in this video will be as out dated as the selenium one
# so I'll just take notes on some detials
# documentation/info at 
# https://pyautogui.readthedocs.io/en/latest/
# first, can install with 
# pip install pyautogui
# output:
# Successfully installed PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyrect-0.2.0 pyscreeze-0.1.28



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

############ PyAuutoGUI

# import pyautogui

#print(pyautogui.size()) # this works

#print(pyautogui.position()) # this works

#pyautogui.moveTo(10,10, duration=1.5) # move to position over 1.5 seconds

#pyautogui.moveRel(200, 0, duration=2)

#pyautogui.moveRel(0, 200, duration=2)

# there's also
#pyautogui.click(100,100)

# also dragRel and 

# also this will show live cords
# running this resulted in raised exception:
#     raise PyScreezeException('The Pillow package is required to use this function.')
#pyautogui.displayMousePosition() 

# so I'll try installing whatever pillow is  with pip

# well it says "Successfully installed pillow-9.0.1" so i guess it worked
# this works...shows mouse x and y cords and also RGB live in the console 
# pyautogui.displayMousePosition()  # just installed pillow. NO extra import line required (doesn't work in idle)

############ PyAuutoGUI - lesson 49

#import pyautogui
# pyautogui.typewrite() # types out messages, be sure to make sure clicks first to make focus, then type out

# I learned that in idle you can do two different 
# commands on one line by separating with a ;
# so this will work
# pyautogui.click(100,-100); pyautogui.typewrite('Hello World')
# i have the idle screen on the left so this just 
# moves it over there/clicks first 
# then types in the message

# these lines move the mouse over to left, clicks, then types in the text with 0.3 sec interval
# pyautogui.click(100,200) 
#pyautogui.typewrite('Hello World', interval=0.3)

# to put in a list of different characters, use 
# ... I don't seem to have pewrite as a thing and there's no suggestion for a module
# to install...but it 'would' look like this
#pewrite(['a', 'b', 'left', 'X', 'Y'], interval=1) # 

# pyautogui.KEYBOARD_KEYS # makes list of all the possible keyboard key names
# including \t for tab, alt and altleft, browsersearch, actually a 'tab' as well
# some volume controls, fn, space, the windows keys, numlock...
# the keys defined with pyautogui.KEYBOARD_KEYS  should work with
# pyautogui.press('F1') for instance
#pyautogui.press('f1') # and this did work


# can also use the hotkey for multikple keys
#pyautogui.hotkey('ctrl', 'o') # example ctrl and o

############ PyAuutoGUI - lesson 50

import pyautogui

# can use screenshot functions to image objects
# requires 'pillow'
# pyautogui.screenshot() # returns pillow image object
#pyautogui.screenshot('C:\\Users\\Keith\\Documents\\repos\\ReallyHadtoPython\\automate boring stuff\\test-screenshot.png') # yes, this did work


# pyautogui.screenshot()
# to locate par tof screen, use locateonscreen
# well i literally took a screenshot with alt+printscreen and saved it as a ping to the repo
# then used the exacxt same code as the isntructor
#and there's no exception thrown but there is no ouptut, including idle, so i have no idea what's going on 
# it's suposed to return cords of where it finds the image
# maybe if i just put it on the root of C:?
#imageCoords = pyautogui.locateOnScreen('C:\\Users\\Keith\\Documents\\repos\\ReallyHadtoPython\\automate boring stuff\\whole-calc.png') # returns cords of where found matching image

#print(imageCoords)

#imageCoords = pyautogui.locateOnScreen('c:\\whole-calc.png') # returns cords of where found matching image

#print(imageCoords) # just returns 'None' so whatever
# this also return 'None'
# print(pyautogui.locateCenterOnScreen('c:\\whole-calc.png'))

# if it /did/ work, i could pass the cords to the moveto/click functions

# this takes a while to work depending on resolution
# must be pixel-perfect

# i should probably try it with something other than calc



