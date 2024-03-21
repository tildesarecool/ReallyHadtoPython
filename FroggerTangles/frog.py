#import rectboilerplate
#from common import dsp

from rectboilerplate import GameRect

import pygame as pyg

from pygame.sprite import Sprite

from common import Common

cmn = Common()

#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600
#GREEN: str = '#008000'
#from common import defineColors

#BLACK, SILVER, GREY, GREEN, WHITE, BLUEISH = defineColors()


class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos
        self.ypos = ypos
        self.ypos_start = ypos
        self.width = width
        self.height = height
        self.color = color
        
        self.move_amount = 7  # Amount to move at a time
        self.move_counter = 0  # Counter to track movement
        
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
# gpt suggested these changes: the self.image lines here in __init__ and moving the self.rect line up here
# i asked gpt if i could just use simple rectangle rather making it a surface so I'm going to try it that way first
        #self.image = pyg.Surface((width, height))
        #self.image.fill(color)
        #self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        self.rect = self.draw_rect()
        #self.update()
        
    def update(self):
#        for event in pyg.event.get():
            #if event.type == pyg.QUIT:
            #        return
        keys = pyg.key.get_pressed()
        if keys[pyg.K_a]:
            self.moving_left = True
        else:
            self.moving_left = False
##################################################
            
        keys = pyg.key.get_pressed()
        if keys[pyg.K_d]:
            self.moving_right = True
            #print(f"screen width is {SCREEN_WIDTH}")
        else:
            self.moving_right = False
##################################################


        keys = pyg.key.get_pressed()
        if keys[pyg.K_w]:
            self.moving_up = True
            #print(f"screen height is {SCREEN_HEIGHT}")
        else:
            self.moving_up = False
            
##################################################

        keys = pyg.key.get_pressed()
        if keys[pyg.K_s]:
            
            self.moving_down = True
           # print(f"screen height is {cmn.SCREEN_HEIGHT}")
        else:
            self.moving_down = False
            
##################################################
            
        if self.moving_right:
            
            if self.xpos <= float(cmn.SCREEN_WIDTH - self.width):
                self.xpos += 7
                
            elif self.xpos >= float(cmn.SCREEN_WIDTH - self.width - 5):
                #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
                #print(f"Current x position is in else is {self.xpos}")
                self.xpos = float(cmn.SCREEN_WIDTH - self.width - 5)
##################################################

        if self.moving_left:
            #self.xpos -= 3
            if self.xpos > 0:
                self.xpos -= 7
                #print(f"Current x position is {self.xpos}")
                #print(f"Current rect right value is {self.rect.right}")
            elif self.xpos <= 5.0:
                #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
                #print(f"Current x position is in else is {self.xpos}")
                self.xpos = 5.0

##################################################

        if self.moving_up:
            if self.ypos >= 5:
                #self.ypos -= 3.0
                #self.ypos -= cmn.cellHeight
                self.ypos -= 7.0
                self.moving_up = False
            elif self.ypos >= self.ypos_start:
                self.ypos = self.ypos_start
                self.moving_up = False



#            if self.ypos <= self.ypos_start:
#                self.ypos -= 3.0
#                print(f"Current ypos is {self.ypos}, rect top is {self.rect.top}")

#            elif self.ypos <= 2.0:
#                print(f"self.ypos <= 2 value is true here, at {self.ypos}")
                #self.ypos = 5
#                self.ypos = 2.0

##################################################

        if self.moving_down:
            #print(f"Value of self.ypos_start is {self.ypos_start} ")
            #print(f"Value of self.ypos is {self.ypos} ")
            #if self.ypos <= SCREEN_HEIGHT + self.height:#self.ypos_start:
            if self.ypos <= self.ypos_start - 5:
                self.ypos += 7
            elif self.rect.bottom >= self.ypos_start:
                #print(f"Value of self.ypos_start is {self.ypos_start} ")
                #print(f"Value of self.ypos is {self.ypos} ")
                #print(f"Current y position is in else is {self.ypos}")
                #print(f"self.rect.bottom value is {self.rect.bottom}")
                #self.ypos = float(self.ypos_start - 5)
                self.rect.bottom = float(self.ypos_start - 1)
                #self.ypos = 5.0

            #elif self.rect.bottom <= (SCREEN_HEIGHT + self.height + 50):
                #self.ypos = self.ypos_start
                #self.rect.bottom = self.ypos_start + 1
                


##################################################


'''
class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos, 
        self.ypos = ypos, 
        self.width = width, 
        self.height = height, 
        self.color = color

    def draw(self):
        
        #Drawing the frog: start at bottom/middle
        
        self.rect = self.draw_rect() #self.draw_rect()
        
    def update(self):



        pass
        
'''