#  19 jan 2023
#  alien invasion game from the book "python crash course"
import sys, pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff

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
        self.aliens = pygame.sprite.Group() # brought in for chapter 13 for the alien stuff
        
        self._create_fleet()  # brought in for chapter 13 for the alien stuff - helper method for lots of aliens
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
            self._update_aliens() # added for making fleet of aliens move, chapter 13
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
    
    def _update_aliens(self):
        """update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
                
    def _create_fleet(self):  # brought in for chapter 13 for the alien stuff - called above rungame method
        """create the fleet of aliens"""
        # create an alien and keep adding aliens until there's no room left
        # spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        
        #current_x = alien_width
        current_x, current_y = alien_width, alien_height
        
        while current_y <  (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
            #self._create_alien(current_x)
                current_x += 2 * alien_width
            # Finished a row; reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
            

    def _create_alien(self, x_position, y_position):
        '''create an alien as place it in the row'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien) 
        #new_alien.x = current_x
        #new_alien.rect.x = current_x
        #self.aliens.add(new_alien)
        #current_x += 2 * alien_width           
        
    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_screen(self):
        """update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color) # 230,230,230 = light gray
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen) # added in chapter 13 to put the alien up on screen (pg. 258)
                    
            # Make the most recently drawn screen visible
        pygame.display.flip()

                
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        