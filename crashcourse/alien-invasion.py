#  19 jan 2023
#  alien invasion game from the book "python crash course"
import sys, pygame
from time import sleep # added page 272
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
from button import Button
from scoreboard import Scoreboard

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
        
        # create an instance to store game statistics
        # and create a scoreboard
        
        # create instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create a group that holds the bullets 
        self.aliens = pygame.sprite.Group() # brought in for chapter 13 for the alien stuff
        
        self._create_fleet()  # brought in for chapter 13 for the alien stuff - helper method for lots of aliens

        # start alien invasion in an inactive state
        #self.game_active = True # this addition correlates to edits in _ship_hit() below
        
        #start alien invasion in an inactive state - pg 278 says to make this inactive so can add title screen
        # i assume i'm supposed to just edit this line to false
        # the aliens are still animated with this false but the bullet from the ship fires and stays in place visible.
        # not sure if that's what's supposed to happen but game active is false
        self.game_active = False
        
        # make play button 
        self.play_button = Button(self, "Play")
        

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
            if self.game_active: # added this if as part of "identifying when parts of the game should run" pg 275 - also indented method calls
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        #if self.play_button.rect.collidepoint(mouse_pos):
        if button_clicked and not self.game_active:
            # reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # reset the game statistics 
            self.stats.reset_stats()
            self.sb.prep_score() # added pg 289
            self.sb.prep_level() # added pg. 295
            self.sb.prep_ships()
            self.game_active = True
            # get rid of any remaining bullets and alines
            self.bullets.empty()
            self.aliens.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            #Hide the mouse cursor
            pygame.mouse.set_visible(False)
        
        
        
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
                
        self._check_bullet_alien_collisions()
                
        # check for any bullets that have hit aliens
        # if so, get rid of teh bullet and the alien
    def _check_bullet_alien_collisions(self): # this method added as part of refactoring starting on page 269
        """respond to bullet-alien collisions"""
        #remove any bullets and aliens that have colided
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True ) # added as part of bullets/collision, pg. 267
        # per the book:
        # for a high powered bullet that can travel to the top of screen/destroy all enemies it encounters, set the first boolean to false
        # and keep the second boolean true.  would make that bullet active until it reached the top of the screen
        if collisions: # if the collisions dictionary even exists
            for aliens in collisions.values(): # go through the values in the dictionary
                self.stats.score += self.settings.alien_points * len(aliens) # add score by points aliens are worth times how big that alien value is
            self.sb.prep_score()
            self.sb.check_high_score() # added in association with high score updates in scoreboard.py - pg. 293

        # part of spawning new fleet once fleet destroyed - pg. 268
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # increase level - as displayed on screen, pg. 295
            self.stats.level += 1
            self.sb.prep_level()
    
    def _update_aliens(self):
        """update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # look for alien ship collisions - pg 271
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # spritecollideany - two arguments are a sprite and a sprite group: if the self.ship group collides with aliens group...hit
            # print("Ship hit!!!") # this was just here for testing
            self._ship_hit()
        
        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
            
            
    def _ship_hit(self):
        """respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0: # part of game over edits, pg 274 (also with all the indenting)
            # decrement ships left - method added per book pg 272
            # and update scoreboard (pg. 298)
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
                
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
    
    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        # added pg 273/4 to check if fleet has reached bottom of screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height: # to spell this out: alien reaches bottom of screen when alien's rect.bottom value >= screen's height
                self._ship_hit()
                break
        
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
        
        # draw the score information
        self.sb.show_score()
        
        # Make the most recently drawn screen visible
        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()

                
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        