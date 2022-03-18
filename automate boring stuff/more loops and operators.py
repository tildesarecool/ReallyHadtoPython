# normal for loop
from re import A


for i in [0, 1, 2, 3]:
    print(i)

# other way with range
range(4)

# fun with ranges and lists
list(range(0, 100, 2))
# count by 2s from 0 to 100. or rather 98

supplies = ['pen', 'staplers', 'binders', 'flamethrowers']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#output of above:

#Index 0 in supplies is: pen
#Index 1 in supplies is: staplers
#Index 2 in supplies is: binders
#Index 3 in supplies is: flamethrowers

# multiple assignments "trick"

cat = ['fat', 'orange', 'loud']
# could use 3 separate vars
# but instead
size, color, dispotion = cat

# size would just get assignment 'fat'

# can also do swap variables
a = 'AAA'
b = 'BBB'
a, b = b, A

# augmented assignment operators

spam = 42
# increase by 1, could use spam = spam + 1
# but
spam += 1
# also works
# but spam++ does not work

