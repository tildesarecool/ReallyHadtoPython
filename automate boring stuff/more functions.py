def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: you tried to deivide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0)) # crashes without try/except clause
print(div42by(1))

# cats excample
#use try/except for input validation

print('How many cats do you have? ')
numCats = input()
try:
    if int(numCats) >= 4 or int(numCats) <= 0:
        print('That is a lot of cats.')
    else:
        print('That is not a lot of cats')
except ValueError:
    print('You did not enter a number.')

