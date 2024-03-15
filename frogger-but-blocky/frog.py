#import rectboilerplate
from rectboilerplate import GameRect

#import pygame as pyg

from pygame.sprite import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#GREEN: str = '#008000'

class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos, 
        self.ypos = ypos, 
        self.width = width, 
        self.height = height, 
        self.color = color

        #self.frogColor = GREEN
        #frogColor = GREEN

#        xpos = (SCREEN_WIDTH // 2)
#        ypos = (SCREEN_HEIGHT - 100 )




    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        self.rect = self.draw_rect() #self.draw_rect()
        
    def update(self):



        pass