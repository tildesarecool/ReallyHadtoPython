#  19 jan 2023
#  alien invasion game from the book "python crash course"
import sys, pygame
from settings import Settings
from ship import Ship

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
        # set background color
        #self.bg_color = (230,230,230)
        
    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw screen during each pass through the loop
            self.screen.fill(self.settings.bg_color) # 230,230,230 = light gray
            self.ship.blitme()
                    
            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function
                
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        