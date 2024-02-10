'''
I was actually having issues with this one
then took a break for a little while
and when i came up it took only a couple of minutes to solve
so I guess sometimes i just need a break

description:
MINIMUM NUMBER IN PYTHON
ASSIGNMENT
Write a function called find_min() that finds the smallest number in a list

find_min([1, 3, -1, 2]) -> -1

find_min([18, 3, 7, 2]) -> 2

POSITIVE INFINITY
Since you're trying to keep track of the smallest number, start with a really big number. Python has a built-in constant that represents positive infinity.

min = float("inf")


'''

def find_min(nums):

    min = float("inf") # for some reason this seems like a weird line. not sure why.
#    num_tracker = 0
    for digit in nums:
        if digit < min:
            min = digit
#            print(f"min is {min}")
#    print(f"min outside for is {min}")

    return min
    
