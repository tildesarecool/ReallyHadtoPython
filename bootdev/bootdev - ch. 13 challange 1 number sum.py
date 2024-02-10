'''
this chapter 13 is supposed to be like a final exam of everything learned up to this point
so this challenge should not have been that hard
still took me a few tries


description:
CHALLENGES
In this chapter we are going to practice applying the skills and concepts we learned while building "Fantasy Quest"

NUMBER SUM
Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

number_sum(5) -> 1+2+3+4+5 -> 15

number_sum(3) -> 1+2+3 -> 6


'''

def number_sum(n):

    sum_tracker = 1
    num_tracker = 1

    if n > 0: # this could be != 0 or if (n) - that would probably cover negative numbers at least
        for i in range(1,n):
            sum_tracker += i
            num_tracker = (sum_tracker + i)
            #print(f"current value of i is {i} current value of sumtracker is {sum_tracker}")
            #print(f"current value of num_tracker is {num_tracker}")
    else:
        return n

    return num_tracker
    
    
