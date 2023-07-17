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


test_list = [1,2,3,4,5,6,7,8,9,10]

excercise_slicing = test_list[::]


solution_slice = excercise_slicing[-3:0:-2]

print(solution_slice)

# list/tuples - "unpacking"
# a,b = (10,5) - assigning first/second value as one line

# another wayt o define tuples basically 

a,b = (10,5)
print(a)
print(b)

c,d = [20, 'Hello']

print(c)
print(d)

# "when creating tuples doesn't actually need parens"
# so these two lines are actually the same
#    a_list = (1,2,3)
#    a_list = 1,2,3

# exploring this
health, energy, weapon = 100,50, 'sword'
print(weapon)

# excercise
value_1 = 10 
value_2 = 'test'
# switch values of the two variables

value_1, value_2 = value_2, value_1 # ...nailed it...

print(value_1, value_2)

# stopping at 2:44:13 under sub-secion "strings are similar to lists/tuples"