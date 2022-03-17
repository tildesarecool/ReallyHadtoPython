#name = ''
# while True
#while name != 'your name.':
#    print('Please type your name.')
#    name = input()
#    if name == 'your name':
#        break
#print('thank you')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))