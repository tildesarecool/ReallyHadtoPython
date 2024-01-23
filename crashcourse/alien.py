import pygame
from pygame.sprite import Sprite
# this file added in chapter 13, if that wasn't obvious
class Alien(Sprite):
    """a class to represent a singal alient in the fleet"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        # load the laien image and set its rect attribute - apparently using the / for the path to the image is really important
        self.image = pygame.image.load('images/alien.png') # still have to make rotated 90 degrees version
        
        self.rect = self.image.get_rect()
        
        # start each new alien near the top of the left of the screen
        # I guess 0,0 position
        # for horizontal i guess it'd be the top right corner
        # so vertical/y would 0 and horizontal/x would be (get screen width) - for top vertically and all the way on the right
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
        # #################################################################### #
        # what would the y coord look like?
        # self.y = float(self.rect.y)
        # ya, seems right
        
        