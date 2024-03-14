import rectboilerplate
from rectboilerplate import GameRect

import pygame as pyg

from pygame.sprite import Sprite


#GREEN: str = '#008000'

class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, frogColor) -> None:
        GREEN: str = '#008000'
        super().__init__(self)
        Sprite.__init__(self)
        self.xpos: int = xpos, 
        self.ypos: int = ypos, 
        self.width: int = width, 
        self.height: int = height, 
        self.frogColor = frogColor

        self.frogColor = GREEN
        frogColor = GREEN

        xpos = (SCREEN_WIDTH // 2)
        ypos = (SCREEN_HEIGHT - 100 )




    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        self.rect = self.draw_rect()
        
    def update(self):



        pass