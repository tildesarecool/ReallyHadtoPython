# ship.py
# for the alien invasion script
# python crash course

import pygame

class Ship:
    """a class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # load ship image and gets its rect.
        # the script kept failing by saying it can't find this image
        # then i closed/re-opened just the crashcrouse subdirectory in vscode and ran alient invasion.py and it worked
        # no idea why it didn't or started to run
        
        # the book seemed to make a big thing about using a BMP file versus using a jpg or png but from this experiement it seems both filetypes load without issue
        # so i'll just use the png
        #self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('images/playerShip1_green.png')
        self.rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen.
        # pygame treats the image as rectangle
        # so rect.midbottom "bottom center of image file"
        # and this is set to the "bottom middle of the screen rectangle itself"
        # thus, the image is int he middle of the screen at the bottom
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)