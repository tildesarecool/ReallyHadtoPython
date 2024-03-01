# attempt to make some kind of version of the very blocky version of frogger
# written by TheCodingTrain in JS/p5.js
# then re-factored in video
# https://www.youtube.com/watch?v=c6WdJltqEtM
# 29 Feb 2024 (it's a leap year)
# the GetWindowRect class is supposed to be an attempt to get a rectangle derived from the game screen much easier and universal
# included below (until I move it) is a generic shape class followed by a rectangle class derived from the shape class



import pygame as pyg
from GetWindowRect import GetWindowRect
from abc import ABC, abstractmethod



pyg.init()

dsp = pyg.display.set_mode(
    (
        1000, 
        800
    )
) # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

ACCELLERATION = 0.5

screen_rect = GetWindowRect.get_screen_rect(dsp)
window_width = screen_rect.width
window_height = screen_rect.height


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
        
        '''
class objRect(objShape):
    #rectangle: color (three number tuple), x pos: single float, y pos: single float, width: float, height: float  #
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
        '''


class objRect(objShape):
    '''rectangle: color (three number tuple), x pos: single float, y pos: single float, width: float, height: float  '''
    def __init__(self ) -> None:
        #super().__init__( self, self.color, self.xpos, self.ypos, self.width )
        pass
    
    def _draw(self, color, xpos, ypos, width,height ):
        #super()._draw()
        self.xpos, self.ypos = xpos, ypos
        self.y = ypos
        self.color = color
        self.width = width
        self.height = height
        
        self.rect = pyg.Rect(xpos,ypos,width, height)



        pyg.draw.rect(dsp,self.color, self.rect )
    

def game() -> None:
    #FirstCircle = objCircle(100, 100, (255,0,0), 15)
    #FirstRect = objRect(dsp,50,50,50)  #(dsp, (100,100), 50)
    #FirstRect._draw(dsp,(255,0,0),50,50,50)
    
    firstRect = objRect()#._draw((244,0,0), 100, 100, 300, 10)
    #secRect = objRect._draw((123,234,45), 10,790,15,15)
    #firstCircle = objCircle._draw((150,0,0), (300,300), 150 )
    #firstLine = objLine._draw((250,143,54), (900,300), (100,600), 5)
    
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
        firstRect._draw((244,0,0), 100, 100, 300, 10) #._draw()
        #firstCircle._draw()
        #firstLine._draw()
        
        #secRect._draw()
        
        

        #ball.draw()
        pyg.display.update()
        clock.tick(FPS)

game()    
pyg.quit()