# this is 11 hour youtube video
# https://www.youtube.com/watch?v=mDKM-JtUhhc
# I found out this part was on youtube
# and the next part "lean python by making games"
# is on udemy
# https://www.udemy.com/course/learn-python-by-making-games/
# so it thought I'd go through the youtube part before buying it

# websites that can run python (and others) online:
# programiz.com...i don't actually see the interactive shell demonstrated in the video but i don't need it anyway
# also replit.com

#print( 7 // 2 ) # not sure i knew about this truncating decimal (not rounding) -  output is just 3


# function - 57 min or so in


# 1h 3m 22s - methods


# i skipped ahead to 02:08:45 - Lists and tuples
# hopefully i didn't skip too much intersting things
# a lot like list: tuples - immutable 

# tuples/lists
# both can contain any kind of data, including lists and tuples and bools etc - used with parans ( )

#list is similar - created with [ ] and separate values with commas

# tuples are immutable

# can append lists with list.apopend(value)
# to do same with tuples can create a new tuple with old values and some additional
# technically tuples slightly faster

# start with lists


#my_list = [1,2,3,4,5, 'word']
#print(my_list)
#print(len(my_list))

# lists with methods
#my_list.clear()
#my_list.reverse()
#print(my_list)

#my_list.append(10)
#print(my_list)


# move on to tuples

#my_tuple = (1,2,3,4,5,1.45, 'word', [7,8,9])

#print(my_tuple)


# how to pick elements from a list - how to get second element?

# each value as an index number - starting from 0

# so [1,2,3,4][1] = value of 2 as it's index 1 starting from 0

#print(my_list[0])  # 0 refers to first index/index 0

#print(my_tuple[7][0]) # my_tuple[7][0] - this returns first element in list inside the tuple, which the value 7

# can also do the [-1] so it loops round to the list element



#excercise_list = ['first entry', [123,456,[0,'Hello :)']], 'bye']
#print(len(excercise_list))
#print(excercise_list[1][2][1])

# 2:27:07 - slicing

# "how to pick multple elemetns form a list"
# [1,2,3,4] - how to get the second and third element?


# slicing involves [ ] like indexing, but you can 2 numbers separated by a colon first start/end number

# in this lsit
#test_list = [1,2,3,4,5,6,7,8,9,10]
# could use [1:2] to refer to the 2 and 3
# "python only goes to the end, does not include the end"



# print(test_list[1:2]) # returns '[2]' literally

# and [1:1]  would return '[]' literally

# but [1:2:1] would indicate the direction - which defaults to 1 - which is positive




#print(test_list[0:8]) # first 8 values in the list

#print(test_list[0:8:2]) # output is [1, 3, 5]

# using -1 in place of 2 would just be empty brackets of output, but....

#print(test_list[-1:4:-1]) # output is [10, 9, 8, 7, 6]

# can also leave value empty when using slicing, as in [1,2,3,4,5,6,7,8,9,10][::-1]

#print(test_list[::-1]) # output [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] - just uses default values, which is first value in list; end value last value in list, defautl step size +1 increment

# worktihng through with variables
#default_slicing = test_list[::]
#print(default_slicing)

# excercise 
# start from 8 and go to 2 values - pick every second value


#test_list = [1,2,3,4,5,6,7,8,9,10]

#excercise_slicing = test_list[::]


#solution_slice = excercise_slicing[-3:0:-2]

#print(solution_slice)

# list/tuples - "unpacking"
# a,b = (10,5) - assigning first/second value as one line

# another wayt o define tuples basically 

#a,b = (10,5)
#print(a)
#print(b)

#c,d = [20, 'Hello']

#print(c)
#print(d)

# "when creating tuples doesn't actually need parens"
# so these two lines are actually the same
#    a_list = (1,2,3)
#    a_list = 1,2,3

# exploring this
#health, energy, weapon = 100,50, 'sword'
#print(weapon)

# excercise
#value_1 = 10 
#value_2 = 'test'
# switch values of the two variables

#value_1, value_2 = value_2, value_1 # ...nailed it...

#print(value_1, value_2)

# stopping at 2:44:33 under sub-secion "strings are similar to lists/tuples"

# turning string into a list/tuple

#test_string = 'this is a test'
#test_list = [1,2,3,4]


#print(test_string.split('t'))
#print(test_string.split())

#print(list(test_string))

#print(tuple(test_string))

# turn a list / tuple into a string
#print(' '.join(['one','two', 'three', 'four']))
#print(' '.join(test_list)) # this throws a type error
#print(str(test_list))
#print(type(str(test_list)))

# indexing strings - same 0-based element access as list/tuple
# can also do splicing
#print(test_string[0])
#print(test_string[0:5])


# next exercise
# remove all the stuff to only get 1 2 3 4 
# "remove everything besides the numbers"
'''
test_string = 'this is a test'
test_list = [1,2,3,4]

print(type(str(test_list)))
print(str(test_list))
turnTestlistToString = str(test_list)
print(turnTestlistToString[1:-1]) # output is 1, 2, 3, 4

print(turnTestlistToString.split()) # output is ['[1,', '2,', '3,', '4]']

turnTestlistToStringWithSplit = turnTestlistToString.split(',')
print(turnTestlistToString[1:-1])
print(type(turnTestlistToStringWithSplit))
turnTestlistToStringWithJoin = ' '.join(turnTestlistToStringWithSplit)
print(type(turnTestlistToStringWithJoin))
print(turnTestlistToStringWithJoin)
print(turnTestlistToStringWithJoin[1:11])
ExerciseFinalAnswer = turnTestlistToStringWithJoin[1:11]

print(ExerciseFinalAnswer)
'''

# 2h51m51s - video answer involves strip, guess i missed that one
# he takes the original, test_list = [1,2,3,4] and converts it to a string
# with str(test_list)
# then adds the strip method - test_list = [1,2,3,4].strip('[')
# then used double strip methods so
#.strip('[').strip(']')
#then added double replace via
#.replace(',','').replace(' ','')

# so the whole thing is 
# str(test_list).strip('[').strip(']').replace(',','').replace(' ','')

''' # just wanted to do some experiments with strings and the len function; no idea if this will be useful later
test_string = 'this is a test'
lenOftestString = len(test_string)
print(test_string[1])
print(lenOftestString)
print(test_string[0:lenOftestString-4])
print(test_string[0:lenOftestString-5])
'''


#################################### dictionaries 2h53m0s ####################################

# ' complex container for other variables' 
# using a key - each value has a key
"""
#test_dict = {key:value}
test_dict = {'A':123, 'B':[1,2,3],1:True,}
print(test_dict) # output: {'A': 123, 'B': [1, 2, 3], 1: True}
print(test_dict.values()) # output: dict_values([123, [1, 2, 3], True])
# type will come back as class 'dict_values' 

# other method is keys()
print(test_dict.keys()) # output: dict_keys(['A', 'B', 1])

# also there's the items() method which returns tuples
print(test_dict.items()) # output: dict_items([('A', 123), ('B', [1, 2, 3]), (1, True)])

# there's also the len function, apparently this is how you actually use it
print(len(test_dict)) # output: 3

# converting a dictionary
print(list(test_dict)) # ['A', 'B', 1]

# same output as the list conversion
print(tuple(test_dict)) # ('A', 'B', 1)

print(str(test_dict)) # {'A': 123, 'B': [1, 2, 3], 1: True}
"""
# indexing w/dictionaries
# does not work same way as above
# name key instead
"""
print(test_dict['A']) # does crash when does not find the specified key

print(test_dict.get('A')) # get slightly better - returns message when doesn't find key
"""
# Exercise for dictionaries -
# do research and use the update method to add another key value pair

"""

dictExerAnswer = test_dict.copy()

dictExerAnswer.update({0:False}) #.update(2:False)

print(dictExerAnswer) # {'A': 123, 'B': [1, 2, 3], 1: True, 0: False}

"""


# could also use dictExerAnswer.update(C = 'test', D = '123')
#another way
#dictExerAnswer['E'] = 100

#################################### Sets - 3h4m35s - ####################################


# simple containers for other variables
# use {} - has only values/no keys and also no duplicate values allowed
"""
my_set = {1,2,3,4}
print(my_set)
print(len(my_set)) # output is 4
"""

#### methods
"""
my_set.add(5)
print(my_set) # added the 5 to the end
print(len(my_set)) # output is 5

my_set.remove(2) # remove the 2
print(my_set) # {1, 3, 4, 5}
print(len(my_set)) # back to 4
"""

# other methods: clear(), pop(), etc
# good reference:
# https://www.geeksforgeeks.org/python-set-methods/

# indexing and slicing do not work with sets
# as in 
#print(my_set[0]) # does not work

# but pop() method does work
"""
print(my_set.pop()) # output: 1

print(my_set) # output: {3, 4, 5}
"""

############### mid point exercise: 
# # Get an item by index from the set using type conversion
# use type convers to get one item from the set by index

# typecasting ftw
"""
mysetToString = str(my_set)
print(mysetToString)

# typecasting ftw -  the list-en-ning
mysetToList = list(my_set)
print(mysetToList)

print(mysetToList[1]) # output is a 4
"""

# main purpose of sets in python - 
# sets are very good when it comes to comparisions

# lots of ways to check if 2 sets have values in common or if they differ
# set1.union(set2)
# for instance

# or
# set1.intersection(set2)
# creates new set with elements present in both sets 

#################### comparison operators

"""
set1 = { 1,2,3,4,4 }
set2 = { 4,5,6,7 }
"""


"""
print(set1.union(set2)) # output: {1, 2, 3, 4, 5, 6, 7}
"""

# a ven diagram is good way to think of it
# this is everything in overlapping
"""
print(set1.difference(set2)) # output {1, 2, 3}
"""
# instead of union - these are quite rarely used
"""
print(set1 | set2) # i think logical or... output: {1, 2, 3, 4, 5, 6, 7}
print(set1 & set2) # output {4} # regular logical and?
print(set1 - set2) # output {1, 2, 3}...same as that difference method output...
"""


############### another exercise: "check if the list as duplicate values using a set" "sets are rare in python"
# this is type list, obviously
"""
test_list = [43,25,324,234,5,2,32423,542,534,324,23,54,65,323,42,4,123,123,5,1,321,3124,123,123,124,1,31,23,145,3542,43,3,21,312]
print(len(test_list))
LenOfTestlist = len(test_list)

ListToSet = set(test_list)
print(ListToSet)

print(len(ListToSet))

LenOfListtoset = len(ListToSet)

if LenOfTestlist != LenOfListtoset:
    print("Yes, there are duplicates")
else:
    print("No, there are not duplicates")

"""


################### booleans - 3h18m30s
# might just fastforward through this section or just passively watch it...

# examples...
# isnum(), check if values present is lists, tuples, set or dict

# print(1 == 1) # prints true
# print(1 == 10) # prints false

# booleans: lists/strings: evaluating with just a print statement
"""
print(1 in [1,2,3]) # true
print(1 in (1,2,3)) # true
print('e' in 'hello') # true
print(4 not in [1,2,3]) # true
"""

# data conversion (typcasting) exercise
#e_dict = { 1:'one', 2:'two', 3:'three' }

###
# check if the key 1 exists in the dict
#check if value 'four' exists in the dict
###
# "solve the 2 problems to check if a key or value is in the dict"
# (pretending the contents of the dict are unknown)

"""
print(e_dict)

print(list(e_dict))

print(list(e_dict)[0])


#print(1 in (list(e_dict)[0]))


print(str(e_dict)[1])
print(str(e_dict))

print('1' in  (str(e_dict)))

print('four' in  (str(e_dict)))

## video solution

print(1 in e_dict) # or print(1 in e_dict.keys) 

print('four' in e_dict.values())

"""


############## bool as a function - 3h27m36s
# bool() can accept any number, string, type of container and still return a value

# can accept any data type

# different rules are complex since data can converted in so many ways

# "truthy" and "falsy" (converted to true or false)

# falsy rules:
# 0 or 0.0 (int or float) will become false
# empty string
# empty tuples/dicts/lists/sets
"""
print(bool(123123409823409823409802398408)) # returns true - any/all numbers besides 0 are true, including  neg
"""
# empty string or empty lists = false
# non-empty is true

# absense of value - datatype = None
"""
print(bool(None))
"""

############# more on data types - others are sequence
#  bytes, complex numbers, memoryview

# main datatypes:
# int, float(), str(), bool(), list(), dict(), tuple(), set()

############################# Flow control - 3h33m40s

# 4 major ways that determin the flow of the code:
# if elif else
# match
# while
# for


# i'm already familiar with else/else if/elif so i'm skipping this exercise

# same with the "complex if statemnents"

# stopping at "nesting if statements" - 4h0m0s

######################################################################

# after breif stop over for a OOP playlist by "tech with tim" i'm back on this 11 hour video
# "tech with tim" talks way too fast for me

'''
if 'a' in ['a', 'b']:
    print('a is in the list') # output: a is in the list
    if 'a'.isalpha():
        print('it is a letter') # it is
'''

'''
x = 'a'    
if x in ['a', 'b', '1']:
    print('a is in the list') # output: a is in the list
    if x.isalpha():
        print('it is a letter') # it is

'''
'''
x = '1'
if x in ['a', 'b', '1']:
    print('a is in the list') # output: a is in the list
    if x.isalpha():
        print('it is a letter') # 1 is not
        
# exercise - "create a nested if statement that runs if all 3 conditions are true (money > 80 for the first one)"
money_available = 100
hungry = False
bored = True

# not exactly a taxing exercise, but great - moving on
if money_available > 80:
    if hungry == False:
        if bored == True:
            print("all of them are true")
            
'''

# match case: 4h6m14s

# similar to if statement - run if condition true, but for a set of values


# alternative to if...elif...elif...
#vscode has pointed out that 'match is a new feature for python 3.10
# also, it looks a lot like a switch
# guess i have no choice to move up to latest python or at least 3.10
# i was just staying on 3.9 because that is what kivy works with/will not work with 3.10
# but now apparently kivvy working with 3.10 anyway so I'll just upgrade to it, probably breaking everything else but here goes
'''
match mood:
    case 'hungry':
        #
    case 'hired':
        #
    case 'bored':
        #
'''
# 4h9m44s


#if mood == 'hungry':
#    print('get some food')
# 

'''
mood = 'bored'

match mood:
    case 'hungry':
        print('get some food')
    case 'thirsty':
        print('get some water')
    case 'tired':
        print('get some sleep')
    case _:
        print('any other mood - default value if not matches')
'''

# exercise
# create variable with an integer between 1 and 5, call it grade
# create match/case that writes 'very good' when grade is 1
# and 'very bad' when grade is between 2 and  5 
# should be some default behaivor if you get an unexpected value

# not exactly difficult. probably should have just skipped it. it's fine.
# I did succefully upgrade to 3.11.4 and remove 3.9. 
# still had to manually remove the variables for 3.9
# and make sure pip still worked
# actually i deleted that folder so i probably lost what ever i installed with pip for 3.9
# but i'm sure it's fine

'''

grade = 's'

match grade:
    case 1:
        print('very good')
    case 2:
        print('not as good')
    case 3:
        print('worse than 2')
    case 4:
        print('needs improvement')
    case 5:
        print('woe woe woe. bad')
    case _:
        print('have you ever heard the old robot saying DOES NOT COMPUTE') # without default it just wouldn't run
        

'''

######################### while loop - 4h11m50s

# easy example -
'''
x = 0
while x < 10:
    x += 1
    print('loop')

'''
'''
x = 0
while x < 10:
    x += 1
    print(x)
    if x == 5:
        print('value is 5')
'''

# there's also keywords break and continue
'''
x = 0
while x < 10:
    x += 1
    print(x)
    if x == 5:
        #break # just stops at 5
        continue
    print('value is 5')

'''

# exercise part 1:
# use a while loop to create a list with only even values from 0 to 100
# exercise part 2:
# "do not add the value 58"


# part 1 was incredibly easy
'''
evenList = []

x = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        evenList.append(x)

print(evenList)
'''

# wow, this part 2 wasn't exactly challenging. a simple and added to the condition? hmmm.
'''
evenList = []

x = 0
while x <= 100:
    x += 1
    if x % 2 == 0 and x != 58:
        evenList.append(x)

print(evenList)
'''



########################## For loops - 4h27m32s
# i think this time i'll just jump to the exercise because wow is this boring
# actually range function/object is more interesting
#form:
# for x in [1, 2, 3]:

# example:
#basic_list = [1,2,3]
#for x in basic_list:
#    print(x)
# works with strings, lists, dictionaries, sets, etc

# basic_set = {1,2,3}
# for x in basic_set:
#    print(x)

#basic_dict = {1: 'one', 2: 'two', 3: 'three'}
#for x in basic_dict.items(): # works with .items and .values for different results/tuple versus strings
#    print(x)

# for loops "need some kind of iterable"

# this is where a "range" (which is its own data type) comes in, such as  
# range(3) - creates a range object

'''
basic_num = 3
for x in range(basic_num):
    print(x)
'''

# output:
# 0
# 1
# 2

# range form:
# print(range(start,end,step))
# good example:
# print(range(10,20,2))
#    print(x)

# exercise
practice_list = [[10,40,20,50], [2,42,10], [101,10,4] ] # nested lists
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100
# hint: use nested for loops, also at least one if statement

#print(practice_list[0][1])


'''
x = 0
y = 0
z = 0
#print(type(y))

for x in practice_list[0]:
    if x >= 10 and x <= 99:
        print(f'value of x is {x}')
        print('---')
    for y in practice_list[1]:
        if y >= 10 and y <= 99:
            print(f'value of y is {y}')
            print('---')

    for z in practice_list[2]:
        if z >= 10 and z <= 100:
            print(f'value of z is {z}')
            print('---')
    #print(practice_list[0][0])
    #x += 1
    #if x != y:
    #    pass
    #print(type(len(practice_list)))
    #print(practice_list)
'''
    
# well i sort of got
# video solution:
# I think i like his more
'''
for nested_list in practice_list:
    for value in nested_list:
        if value > 100:
            break
        if value < 50:
            if value < 10:
                continue
            print(value)
'''

# seems like good place to stop
# 04:42:42 - Flow + linebreaks
