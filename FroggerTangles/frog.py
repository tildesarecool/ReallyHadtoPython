#import rectboilerplate
#from common import dsp

from rectboilerplate import GameRect

import pygame as pyg

from pygame.sprite import Sprite


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
        self.width = width
        self.height = height
        self.color = color
        
        self.moving_left = False
        self.moving_right = False
        
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
            
        if self.moving_left:
            self.xpos -= 3


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