# attempt to draw some lanes:
# first car lanes, then middle sidewalk, then river with log lanes

# I assume this will be called first so everything else will be on top of them
# just rectangles of different colors and heights - the width of the screen

from rectboilerplate import GameRect
#import pygame as pyg
from pygame.sprite import Sprite
from common import Common
cmn = Common()

class Lane(GameRect, Sprite): 
    '''Rectangles for background to represent lanes'''
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos
        self.ypos = ypos
        #self.ypos_start = ypos
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        '''
        Drawing the lane(s): on the screen
        '''
        self.rect = self.draw_rect()