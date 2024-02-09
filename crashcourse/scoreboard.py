import pygame.font
from pygame.sprite import Group # part of the inheritance at end of chapter 14 (and below)
from ship import Ship # part of the inheritance at end of chapter 14 (and below)



class Scoreboard:
    """A class to report scoring information"""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game # part of the inheritance at end of chapter 14 (and below)
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 
        self.stats = ai_game.stats
        
        # font settings for score info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the intitial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships() # part of the inheritance at end of chapter 14 (and below)
        
    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        
        # the ':,' part of this is a "formal specifier" that "modifies the way a variable's values are presented" (pg. 291/92)
        # in this case it should put in the commas at the appropraite places in numbers like 1,000,000 automatically (this worked)
        score_str = f"{rounded_score:,}" 
        
        #score_str = str(self.stats.score)
        
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect) # draws info to screen
        self.ships.draw(self.screen) # part of the inheritance at end of chapter 14 
        # pg. 298
        # "to display the ships on the screen, well draw on the group and pygame draws each ship"
        # seems very succinctly put
        
    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}" # see above for the thing
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        
    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score: # is the current score greater than established "high score"?
            self.stats.high_score = self.stats.score # if it is make current score the new high score
            self.prep_high_score() # then render that high score to the screen
            
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 # ten pixels down from top of screen
        
    def prep_ships(self): # part of the inheritance at end of chapter 14 (and below)
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
                