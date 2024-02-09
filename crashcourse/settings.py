# settings.py - settings for alien invasion script
# modified for chapter 14/pg 284
class Settings:
    """a class to store all settings for alien invasion"""
    def __init__(self):
        """initialize game's [static] settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship settings
        #self.ship_speed = 4.5 # this actually only accepts ints so adjustments were made to ship.py
        self.ship_limit = 3
        # bullet settings
        #self.bullet_speed = 6.0
        self.bullet_width = 300 # default value = 3 - a good value for test is 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # 60, 60, 60 is "dark gray" (apparently 000 = black and 255 255 255 = white)
        self.bullets_allowed = 9 # default value = 3 arbitrarily limit number of bulets on screen at once (page 251)
        # alien settings
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # default value = 10 - setting this to 100 for debug purposes
        
        # how quickly the game speeds up 
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase 
        self.score_scale = 1.5
        
        
        self.initialize_dynamic_settings()
        
        
        # fleet direction 1 represents right; -1 represents left
        #self.fleet_direction = 1
        
    def initialize_dynamic_settings(self):
        """initialize settinsg that change throughout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        # fllet direction represents right; -1 represents left
        self.fleet_direction = 1
        
        # scoring settings
        self.alien_points = 50
        
    def increase_speed(self):
        """increase speed and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)