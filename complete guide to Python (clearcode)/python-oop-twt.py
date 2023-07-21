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

    def talk(self): # must include 'self' so i t can access name and age
        print("Hi I am", self.name, 'and i am ', self.age, 'years old')
'''
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

'''
class Cat(Dog): # used a specific object instenad of word 'object'
    # "derived from Dog"
    def __init__(self, name, age, color):
        super().__init__(name, age) # this super thing was auto-filled by vscode - this calls the constructer of the Dog() object
        self.color = color
    
    def talk(self):
        print('Meow')

tim = Cat('tim', 5, 'blue')
'''

# prior - defining the cat object speak method: Hi I am tim and i am  5 years old
#tim.speak() 

# inherited attributes etc
# much more useful in really long things
# tim.speak would produce 'bark' so overload to say 'meow'
'''
# actually called the cat version 'talk'
tim.talk() # this one produces 'meow', so it over-wrote the dog object talk method and used the Cat object talk method
'''
########################
# video 3 in playlist 
# https://www.youtube.com/watch?v=H2SQrZK2nvM&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=3
# 6m32s
########################
'''
jim = Dog('jim', 70)
# demonstration over riding/inheritance
jim.talk() # Hi I am jim and i am  70 years old
'''

# starting new class - this time smaller and more broad
# so further classes can be derived that much easier

'''
class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color 
    
    def fileUpTank(self):
        self.gas = 100

    def emtpyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle): # derived from vehical, obviously
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep beep')
# could also inherit from car which in inherits from vehicle
class Truck(Vehicle): # derived from vehical, obviously
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('Honk honk')

'''


################## video 4/6 - overloading existing python methods

# matching page for video 4: https://www.techwithtim.net/tutorials/python-programming/classes-objects-in-python/overloading-methods

'''
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x + self.y * p.y)
    
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"


# some vars to test out examples

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7) # long time getting there, but output: (6,6) (-3,-3) (9,0)
'''

#######################

'''
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x + self.y * p.y)

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2) # the ** means 'to the power of' e.g. an exponent
    
    def __gt__(self, p):
        return self.length() > p.length() # greater than
    def __ge__(self, p): # greater than or equal to
        return self.length() >= p.length()
    def __lt__(self, p):
        return self.length() < p.length()        
    def __le__(self, p): # less than or equal to
        return self.length() <= p.length()
    def __eq__(self, p): # equal to
        return self.x == p.x and self.y == p.y 
    
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"


# some vars to test out examples

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)

# output:
#False
#True
#True

# there's a list of python methods/functions than can be overriden, only those specific ones

# this includes len or __len__
# pretty much all of them with the double underscores
'''

################# video 5/6

# going to stop here. at 2m30s or so. this is getting a little complicated. 

class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
    
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        # bark n times
        for _ in range(n):
            print("Bark")

tim = Dog("Tim")
jim = Dog('Jim')
