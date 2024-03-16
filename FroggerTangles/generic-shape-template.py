# 27 feb 2024
# this is continues from display template to draw a shape on to the screen    
# I'm using 
# https://www.youtube.com/watch?v=ZeCeEUF2J2c
# as a basis for a very basic display setup and line/circle draw in in pygame

import pygame as pyg

# Import the abc module to define abstract classes and methods
# I got this from the cheat sheet I've been using
# https://www.pythoncheatsheet.org/cheatsheet/oop-basics

from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area




pyg.init()

dsp = pyg.display.set_mode((1000, 800)) # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

ACCELLERATION = 0.5

class objShape(ABC):
    '''A very generic shape class'''
    # as mentioned above apparently this is a thing.
    # I'd like to just write the one draw method and apply it to all shape classes so this syntax seemed perfect    
    
    #def __init__(self) -> None:

    
    @abstractmethod
    def _draw(self, color, xpos, ypos, width ):
        self.xpos, self.ypos = xpos, ypos
            
        self.color = color
        self.width = width
        pass
        
class objRect(objShape):
    '''rectangle: color (three number tuple), x pos: single float, y pos: single float, width: float, height: float  '''
    def __init__( self, color, xpos, ypos, width,height ) -> None:
        #super().__init__( self, self.color, self.xpos, self.ypos, self.width )
        self.xpos, self.ypos = xpos, ypos
        self.y = ypos
        self.color = color
        self.width = width
        self.height = height
        
        self.rect = pyg.Rect(xpos,ypos,width, height)
    
    def _draw(self):
        #super()._draw()
        pyg.draw.rect(dsp,self.color, self.rect )

        
    
    #def _draw(dsp, self.color, self.xpos, self.ypos, self.width):
    #    pyg.draw.rect(dsp, self.color, (self.xpos, self.ypos), self.width)
        #pyg.Rect()


#rect = Rect(100,100,(255,0,0))


class objCircle(objShape):
    '''Circle: color (three number tuple), centerpoint coords (two number tuple), radius int/float'''
    def __init__(self, color,  centerPoint, radius ) -> None:
        #super().__init__(color, xpos, ypos, radius )
        #self.xpos, self.ypos = xpos, ypos
        #self.y = ypos
        self.color = color
        self.centerPoint = centerPoint
        self.radius = radius

        #self.circle = pyg.circle(dsp, self.color, self.centerPoint, self.radius )
        #self.rect = pyg.Rect(xpos,ypos,width, height)
    
    def _draw(self):
        #super()._draw()
        #pyg.draw.rect(dsp,self.color, self.rect )
        pyg.draw.circle(dsp, self.color, self.centerPoint, self.radius )

    
#pyg.draw.line(dsp, (0, 0, 0), (0, 400), (1024, 400), 10 )
class objLine(objShape):
    '''Line: color (three number tuple), start pos (two number tuple), end pos (two number tuple), width: integer for line thickness '''
    def __init__(self, color, startPos, endPos, width ) -> None:
        
    #super().__init__(color, xpos, ypos, radius )
    #self.xpos, self.ypos = xpos, ypos
    #self.y = ypos
        self.color = color
        self.startPos = startPos
        self.endPos = endPos
        self.width = width

        
    def _draw(self):
        pyg.draw.line( dsp, self.color, self.startPos, self.endPos, self.width)
        

        pass    
    
#    pass    
        

'''
class Ball():
    def __init__(self) -> None:
        self.y =  200
        self.velocity = 10
    def draw(self):
#                            color = red    x and y   radius
        pyg.draw.circle(dsp, (255, 0, 0), (500, int(self.y)), 15)
        
    def move(self):
        self.velocity += ACCELLERATION
        self.y += self.velocity
        if self.y >= 401:
            self.velocity = -self.velocity 
        elif self.y == 400:
            self.velocity += ACCELLERATION
        
'''

def game() -> None:
    #FirstCircle = objCircle(100, 100, (255,0,0), 15)
    #FirstRect = objRect(dsp,50,50,50)  #(dsp, (100,100), 50)
    #FirstRect._draw(dsp,(255,0,0),50,50,50)
    
    firstRect = objRect((244,0,0), 100, 100, 300, 10)
    secRect = objRect((123,234,45), 10,790,15,15)
    firstCircle = objCircle((150,0,0), (300,300), 150 )
    firstLine = objLine((250,143,54), (900,300), (100,600), 5)
    
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                return
        #ball.move()
            
            
##########################################################################            
        dsp.fill((255,255,255))
        # draw a horizontal line
        #pyg.draw.line(dsp, (0, 0, 0), (0, 400), (1024, 400), 10 )
        firstRect._draw()
        firstCircle._draw()
        firstLine._draw()
        
        secRect._draw()
        
        

        #ball.draw()
        pyg.display.update()
        clock.tick(FPS)

game()    
pyg.quit()