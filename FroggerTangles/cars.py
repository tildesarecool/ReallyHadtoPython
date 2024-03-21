#import rectboilerplate
#from common import dsp

from rectboilerplate import GameRect

#import pygame as pyg

from pygame.sprite import Sprite

from common import Common

cmn = Common()



class Car(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos
        self.ypos = ypos
        #self.ypos_start = ypos
        self.width = width
        self.height = height
        self.color = color
        

        
        self.moving_left = True
        self.moving_right = False

        


    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        self.rect = self.draw_rect()
        self.update()
        
    def update(self):
#        if self.moving_right:
            
#            if self.xpos <= float(cmn.SCREEN_WIDTH - self.width):
#                self.xpos += 7
                
#            elif self.xpos >= float(cmn.SCREEN_WIDTH - self.width - 5):
#                self.xpos = float(cmn.SCREEN_WIDTH - self.width - 5)
##################################################

        if self.moving_left:
            #self.xpos -= 3
            if self.xpos > 0:
                self.xpos -= 5
                #print(f"Current x position is {self.xpos}")
                #print(f"Current rect right value is {self.rect.right}")
            #elif self.rect.left <= 1.0 or self.xpos <= 1.0:
                #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
                #print(f"Current x position is in else is {self.xpos}")
                #self.rect.left = cmn.SCREEN_WIDTH - 2
            #    self.rect.x = cmn.SCREEN_WIDTH - 2
            #    self.xpos = self.rect.x
