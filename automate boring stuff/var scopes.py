# global variable
spam = 42
def eggs():
    # local vaariable
    spam = 42
    # not supposed to onflict since different scopes

def spam():
#    eggs = 99
 #   bacon()
    eggs = 'Hello'
    print(eggs)

def bacon():
    ham = 101
    eggs = 0


eggs = 42

spam()

print(eggs)