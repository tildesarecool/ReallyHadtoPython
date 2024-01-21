#  19 jan 2023
#  alien invasion game from the book "python crash course"
import sys, pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

# import pygame

class AlienInvasion: 
    # Overall class to manage game assets and behavior 
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock() # related to consistent frame rate - see also tick method
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (
            self.settings.screen_width, 
            self.settings.screen_height
            )
        )
        
        
        
        
        #self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create a group that holds the bullets 
        # set background color
        #self.bg_color = (230,230,230)
        

# This is the code for full screen, which looks terrible on my giant monitor - page 245 - after implementing it the books says (paraphrasing)
# "but if that doesn't work good that keep the old code" - could have said that first!
#        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

        
        
    # per the book, methods that start with a _ are "helper methods"
    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # when the update() is called on a group the group automatically calls update() for each sprite in the group
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.bullets.update() # update position of bullets on each pass through while loop
            
            # get rid of bullets that have disappeared 
            #for bullet in self.bullets.copy(): # going through each bullet in the bulllet...list? bullets created each time space bar used, anyway
            #    if bullet.rect.bottom <= 0: # rect bottom:  the bullet is a rectangle, 0 is top of screen - this checks if bottom of bullet is out of visibility
            #        self.bullets.remove(bullet)
            # print(len(self.bullets)) # exists for debugging - should reduce to 0 once all the bullets have left the screen. verified as working so removed...
            
            self._update_screen()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function
            # Watch for keyboard and mouse events.
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
# ################################################################ #
    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """repsond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed: # arbitrarily limit number of bullets on screen at once (page 251) see also bullets.py
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        # update bullet position
        self.bullets.update()
        
        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color) # 230,230,230 = light gray
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
                    
            # Make the most recently drawn screen visible
        pygame.display.flip()

                
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        