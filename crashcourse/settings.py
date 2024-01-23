# settings.py - settings for alien invasion script
class Settings:
    """a class to store all settings for alien invasion"""
    def __init__(self):
        """initialize game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship settings
        self.ship_speed = 4.5 # this actually only accepts ints so adjustments were made to ship.py
        # bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 300 # default value = 3 - a good value for test is 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # 60, 60, 60 is "dark gray" (apparently 000 = black and 255 255 255 = white)
        self.bullets_allowed = 9 # default value = 3 arbitrarily limit number of bulets on screen at once (page 251)
        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction 1 represents right; -1 represents left
        self.fleet_direction = 1