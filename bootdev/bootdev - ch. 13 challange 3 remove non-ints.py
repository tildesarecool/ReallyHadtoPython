'''
This one I did solve on the first try in a few minutes. 
Just recording it here in case i need reference. or something.

description:
REMOVE NUMBERS
Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

remove_nonints(['1', 1, '3', '400', 4, 500])
# Remaining list after removing nonints = [1, 4, 500]
Copy icon
You can check the type of a variable using type() function.

if type(variable) == int:
Copy icon
Do not change the input nums list, return a new list with only the integers.


'''

def remove_nonints(nums):

    nonint_tracker = []
    
    for intsinlist in nums:
        if type(intsinlist) == int:
            nonint_tracker.append(intsinlist)
    
    #print(f"new nonint_tracker is {nonint_tracker}")

    return nonint_tracker
    
    
