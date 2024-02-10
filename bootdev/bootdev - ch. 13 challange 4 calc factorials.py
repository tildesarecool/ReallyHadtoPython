'''
this is my non working progress on this one so far.
i realized i've been doing it long enough I don't think I'm making progress
so I'll pick it up later or tomorrow


description:
FACTORIAL
Complete the factorial() function. It should calculate the factorial of a number. A factorial of a number is the product of all positive integers less than or equal to that number.

For example:

4! = 4 * 3 * 2 * 1 = 24

The ! symbol denotes a factorial

TIP: A SPECIAL CASE FOR ZERO
The value of 0! is 1. This keeps factorials consistent with the convention for an empty product.


'''

def factorial(num):

    if num == 0:    
       # print("num is 0")
        return 1
    
    number_tracker = num 
    num_list = []

    itracker = 0
    newtracker = 1
    newvalue = 0
    product_tracker = 0
    while (number_tracker > 0):
        num_list.append(number_tracker)
        number_tracker -= 1
       # print(f"while loop number_tracker is {number_tracker}")

    for intnum in range(len(num_list)):
        #if intnum < :
        print(f"intnum for loop  is {intnum}")
        newvalue = num_list[itracker]
        #(intnum * intnum) * (intnum - 1)
        print(f"itracker = num_list[itracker] for loop  is {newvalue}")
        itracker += 1
        product_tracker = newvalue * (newvalue - 1)
        print(f"product_tracker for loop  is {product_tracker}")

    print(f"final number_tracker is {number_tracker}")
    print(f"final num_list is {num_list}")
    print(f"final newtracker is {newtracker}")
    
