# The solution to this particular puzzle (you're welcome)

def find_max(nums):
    max_so_far = float("-inf")
    max_tracker = -10

    for i in range(0, len(nums)  ):
        print(f"i is {nums[i]}")
        if nums[i] > max_so_far:
            #max_tracker = nums[i]
            print(f"nums i is  {nums[i]}, max tracker is {max_tracker}")
            if nums[i] > max_tracker:
                print(f"nums i is greater than max tracker - nums i is {nums[i]}, max tracker is {max_tracker}")
                max_so_far = nums[i]
    return max_so_far

