# this is small side track (from the 12 hour clearcode video) to an oop video by Tech With Tim (late 2018)
# https://www.youtube.com/watch?v=v_Jp11xqCzg&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt
# this is a whole playlist actually...
# look like episodes are 12 - 15 min each

# twt is a seemingly good channel, actually...he'll do 12 hour live streams creating a whole game from scratch
# seems excessive

# starting with classes...

# types like int are inferred via defined classes
# same for other types

# functions
'''
def func (x):
    return x + 1

print(func(5)) # returns 6
'''

# next is video 2 / classes
'''
class Dog(object):
    # the __initi__ will be defined in most if not all classes - this will automatically run every time type Dog is created
    def __init__(self, name, age):
        # self refers to instantiated instance of type dog
        #print("Nice you made a dog")
        self.name = name
        # self refers to instantiation
        # self has to be there as parameter (except in rare circumstances)
        self.age = age

    def speak(self): # must include 'self' so i t can access name and age
        print("Hi I am", self.name, 'and i am ', self.age, 'years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

        
tim = Dog('Tim', 5) # (before speak method) this assigment alone produces Nice you made a dog
fred = Dog('Fred', 4) # (before speak method) this assigment alone produces Nice you made a dog

tim.speak() # Hi I am Tim and i am  5 years old
fred.speak() # Hi I am Fred and i am  4 years old

tim.change_age(9)
tim.speak() # Hi I am Tim and i am  9 years old

# to just access atrributes
print(tim.age)
print(tim.name)

# can create multiple instances of classes

tim.add_weight(70)
print(tim.weight) # returns 70
'''
################# third video - inheritance #################


class Dog(object):
    # the __initi__ will be defined in most if not all classes - this will automatically run every time type Dog is created
    def __init__(self, name, age):
        # self refers to instantiated instance of type dog
        #print("Nice you made a dog")
        self.name = name
        # self refers to instantiation
        # self has to be there as parameter (except in rare circumstances)
        self.age = age

    def talk(self): # must include 'self' so i t can access name and age
        print("Hi I am", self.name, 'and i am ', self.age, 'years old')

'''
class Cat(object):
        # this was all copy/pasted from the dog object
        # to demonstrate this should not be necessary
        # next example utilizes inheritance
    def __init__(self, name, age, color):
        # self refers to instantiated instance of type dog
        #print("Nice you made a dog")
        self.name = name
        # self refers to instantiation
        # self has to be there as parameter (except in rare circumstances)
        self.age = age
        self.color = color

    def speak(self): # must include 'self' so i t can access name and age
        print("Hi I am", self.name, 'and i am ', self.age, 'years old')

'''

class Cat(Dog): # used a specific object instenad of word 'object'
    # "derived from Dog"
    def __init__(self, name, age, color):
        super().__init__(name, age) # this super thing was auto-filled by vscode - this calls the constructer of the Dog() object
        self.color = color
    
    def talk(self):
        print('Meow')

tim = Cat('tim', 5, 'blue')
# prior - defining the cat object speak method: Hi I am tim and i am  5 years old
#tim.speak() 

# inherited attributes etc
# much more useful in really long things
# tim.speak would produce 'bark' so overload to say 'meow'

# actually called the cat version 'talk'
tim.talk() # this one produces 'meow', so it over-wrote the dog object talk method and used the Cat object talk method

########################
# video 3 in playlist 
# https://www.youtube.com/watch?v=H2SQrZK2nvM&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=3
# 6m32s
########################