# ship.py
# for the alien invasion script
# python crash course

import pygame

class Ship:
    """a class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # load ship image and gets its rect.
        # the script kept failing by saying it can't find this image
        # then i closed/re-opened just the crashcrouse subdirectory in vscode and ran alient invasion.py and it worked
        # no idea why it didn't or started to run
        
        # the book seemed to make a big thing about using a BMP file versus using a jpg or png but from this experiement it seems both filetypes load without issue
        # so i'll just use the png
        #self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen.
        # pygame treats the image as rectangle
        # so rect.midbottom "bottom center of image file"
        # and this is set to the "bottom middle of the screen rectangle itself"
        # thus, the image is int he middle of the screen at the bottom
        self.rect.midbottom = self.screen_rect.midbottom
        
        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        #  Movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """update the ship's position based ont he movement flags."""
        # Update the ship's x value, not the rect
        #if self.moving_right:
        if self.moving_right and self.rect.right < self.screen_rect.right: # right hand side is max x value - screen_rect.right
            self.x += self.settings.ship_speed
            #self.rect.x += 1
        #if self.moving_left:
        if self.moving_left and self.rect.left > 0: # left side is coord 0
            self.x -= self.settings.ship_speed
            #self.rect.x -= 1
        # update rect object from self.x
        self.rect.x = self.x

        
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)